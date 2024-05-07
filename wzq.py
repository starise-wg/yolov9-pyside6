import platform
from pathlib import Path
import sys
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import numpy as np
import torch
from PySide6.QtWidgets import QFileDialog, QHBoxLayout, QDialog
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from yolov9Qt import Ui_MainWindow
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtGui, QtCore

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLO root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode


class MyThread(QThread):
    # 原图
    send_raw = Signal(np.ndarray)
    # 发送检测结果图
    send_detect_img = Signal(np.ndarray)
    # 发送检测的类别信息，速度等
    send_detect_info = Signal(str)
    # 发送检测速度
    send_speed = Signal(str)
    # 发送进度条百分比
    send_percent = Signal(int)
    # 检测到的目标数量
    send_detect_num = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化参数
        self.weights ='yolov9-c.pt'
        self.source = 'data/images'
        self.data = ROOT / 'data/coco.yaml'
        self.imgsz = (640, 640)
        self.conf = 0.25
        self.iou = 0.45
        self.max_det = 1000
        self.device = ''
        self.view_img = False
        self.save_txt = False
        self.save_conf = False
        self.save_crop = False
        self.nosave = False
        self.classes = None
        self.agnostic_nms = False
        self.augment = False
        self.visualize = False
        self.update = False
        self.project = ROOT / 'runs/detect'
        self.name = 'exp'
        self.exist_ok = False
        self.line_thickness = 3
        self.hide_labels = False
        self.hide_conf = False
        self.half = False
        self.dnn = False
        self.vid_stride = 1
        self.play = True
        self.end_loop = False
        self.is_save = Qt.Checked
    @smart_inference_mode()
    def run(self):
        source = str(self.source)
        current_frame = 0  # 初始化计数器，用于计算视频的进度
        # 重置进度条
        self.send_percent.emit(0)
        save_img = not self.nosave and not source.endswith('.txt')  # save inference images
        is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
        webcam = source.isnumeric() or source.endswith('.txt') or (is_url and not is_file)
        screenshot = source.lower().startswith('screen')
        if is_url and is_file:
            source = check_file(source)  # download

        # 如果选择保存，创建保存的文件夹
        if self.is_save == Qt.Checked:
            save_dir = increment_path(Path(self.project) / self.name, exist_ok=self.exist_ok)  # increment run
            (save_dir / 'labels' if self.save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

        # 加载模型
        device = select_device(self.device)
        model = DetectMultiBackend(self.weights, device=device, dnn=self.dnn, data=self.data, fp16=self.half)
        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(self.imgsz, s=stride)  # check image size

        # 根据检测资源的类型，加载数据
        bs = 1  # batch_size
        if webcam:
            view_img = check_imshow(warn=True)
            dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=self.vid_stride)
            bs = len(dataset)
        elif screenshot:
            dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=self.vid_stride)
        vid_path, vid_writer = [None] * bs, [None] * bs

        # Run inference
        model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
        for path, im, im0s, vid_cap, s in dataset:
            count_label=""
            #当按下暂停的时候，执行下面的遍历，不再执行数据遍历for循环
            while not self.play:
                #判断有没有终止程序
                if self.end_loop:
                    # 如果是摄像头，设置状态，停止线程
                    if webcam:
                        dataset.stop_threads = True
                    break
            #当按下终止检测按钮时，执行下面的方法，跳出循环
            if self.end_loop:
                # 如果是摄像头，设置状态，停止线程
                if webcam:
                    dataset.stop_threads = True
                break
            # 更新当前检测数量索引
            current_frame += 1
            if vid_cap is not None:
                # 计算视频检测进度并发送当前检测的进度百分比
                progress_percentage = int(
                    current_frame / int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)) * 100)
                self.send_percent.emit(progress_percentage)
            else:
                # 计算图片检测进度并发送当前检测的进度百分比
                progress_percentage = int(
                    current_frame / int(len(dataset)) * 100)
                self.send_percent.emit(progress_percentage)
            with dt[0]:
                im = torch.from_numpy(im).to(model.device)
                im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim
            # Inference
            with dt[1]:
                visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if self.visualize else False
                pred = model(im, augment=self.augment, visualize=visualize)

            # NMS
            with dt[2]:
                pred = non_max_suppression(pred, self.conf, self.iou, self.classes, self.agnostic_nms, max_det=self.max_det)


            # Process predictions
            for i, det in enumerate(pred):  # per image
                seen += 1
                if webcam:  # batch_size >= 1
                    p, im0, frame = path[i], im0s[i].copy(), dataset.count
                    s += f'{i}: '
                else:
                    p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

                # 发送原图
                self.send_raw.emit(im0)
                p = Path(p)  # to Path
                if self.is_save==Qt.Checked:
                    save_path = str(save_dir / p.name)  # im.jpg
                    txt_path = str(save_dir / 'labels' / p.stem) + (
                        '' if dataset.mode == 'image' else f'_{frame}')  # im.txt
                s += '%gx%g ' % im.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                imc = im0.copy() if self.save_crop else im0  # for save_crop
                annotator = Annotator(im0, line_width=self.line_thickness, example=str(names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                        count_label+=f"{names[int(c)]}:{n}  \n"
                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if self.save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            line = (cls, *xywh, conf) if self.save_conf else (cls, *xywh)  # label format
                            with open(f'{txt_path}.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')

                        if save_img or self.save_crop or view_img:  # Add bbox to image
                            c = int(cls)  # integer class
                            label = None if self.hide_labels else (names[c] if self.hide_conf else f'{names[c]} {conf:.2f}')
                            annotator.box_label(xyxy, label, color=colors(c, True))
                        if self.save_crop:
                            save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)
                #发送检测个数
                self.send_detect_num.emit(len(det))  # 发送统计检测个数

                # 添加标注框和置信度
                im0 = annotator.result()
                #发送检测结果图
                self.send_detect_img.emit(im0)
                if self.view_img:
                    if platform.system() == 'Linux' and p not in windows:
                        windows.append(p)
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                    cv2.imshow(str(p), im0)
                    cv2.waitKey(1)  # 1 millisecond

                # 判断是否保存
                if self.is_save==Qt.Checked:
                    if dataset.mode == 'image':
                        cv2.imwrite(save_path, im0)
                    else:  # 'video' or 'stream'
                        if vid_path[i] != save_path:  # new video
                            vid_path[i] = save_path
                            if isinstance(vid_writer[i], cv2.VideoWriter):
                                vid_writer[i].release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                            vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                        vid_writer[i].write(im0)

            #pycharm底部控制台输出检测信息
            # LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")
            # 实时发送检测速度，小数点采取四舍五入，保留一位小数
            self.send_speed.emit(f"{dt[1].dt * 1E3:.1f}")
            info=(f"正在使用{str(device)}检测资源\n"
                  f"当前的置信度为：{self.conf}\n"
                  f"当前的IOU为：{self.iou}\n"
                  f"您选择{'保存' if self.is_save==Qt.Checked else '不保存'}文件夹，{'保存的位置为:'+str(save_dir) if self.is_save == Qt.Checked else ''}\n"
                  f"检测到的物体和数量如下：\n{count_label}")


            #发送检测信息，展示在图形界面右下角
            self.send_detect_info.emit(info)
        # Print results
        # t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
        #
        # LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}' % t)
        # if self.save_txt or save_img:
        #     s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if self.save_txt else ''
        #     LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
        if self.update:
            strip_optimizer(self.weights[0])  # update model (to fix SourceChangeWarning)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  # 加载pyside6的UI
        self.methoBinding()  # pyside6和python方法绑定
        self.camera_isOpen = False
        self.my_thread = MyThread()
        self.my_thread.iou = 0.25
        self.my_thread.conf = 0.7
        self.my_thread.weights = "yolov9-c.pt"
        self.my_thread.is_save = Qt.Checked
        self.my_thread.play = True
        self.my_thread.end_loop = False
        self.my_thread.send_raw.connect(lambda x: self.show_detect(x, self.label_raw))
        self.my_thread.send_detect_img.connect(lambda img: self.show_detect(img, self.label_result))
        self.my_thread.send_detect_info.connect(lambda info: self.show_detect_info(info))
        self.my_thread.send_speed.connect(lambda speed: self.show_speed(speed))
        self.my_thread.send_detect_num.connect(lambda num: self.show_detect_num(num))
        self.my_thread.send_percent.connect(lambda percent: self.progressBar.setValue(percent))
        self.load_config()

    def methoBinding(self):
        self.Button_checkImg.clicked.connect(self.select_images)  # 检测图片
        self.Button_openCamera.clicked.connect(self.open_camera)  # 检测摄像头
        self.Button_checkVideo.clicked.connect(self.select_video)  # 检测视频
        #self.Button_rtmpStream.clicked.connect(self.pull_stream) # 拉取视频流
        self.Button_select_folder.clicked.connect(self.select_folder)  # 检测文件夹
        self.Button_select_w_p.clicked.connect(self.select_weights)  # 选择权重
        self.pushButton_bofang.clicked.connect(self.play_and_pause)  # 播放暂停
        self.doubleSpinBox_conf.valueChanged.connect(lambda x: self.change_conf(x))  # 调整置信度
        self.doubleSpinBox_iou.valueChanged.connect(lambda x: self.change_iou(x))  # 调整iou

        self.horizontalSlider_conf.valueChanged.connect(lambda x: self.change_hor_conf(x))
        self.horizontalSlider_iou.valueChanged.connect(lambda x: self.change_hor_iou(x))
        self.checkBox_isSave.clicked.connect(self.save_result)  # 选择是否保存
        self.pushButton_stop.clicked.connect(self.end_thread)  # 终止检测

    # 从源码目录下的config.json中读取配置
    def load_config(self):
        # 读取 JSON 文件
        with open("config.json", "r") as jsonfile:
            loaded_config = json.load(jsonfile)
            # 获取参数值
            self.my_thread.weights = loaded_config["weights"]
            self.my_thread.conf = loaded_config["conf"]
            self.my_thread.iou = loaded_config["iou"]
            # self.my_thread.is_alarm = loaded_config["is_alarm"]
            self.my_thread.is_save = loaded_config["is_save"]
        # 把读取的值，传递展现到pyside组件上
        self.doubleSpinBox_conf.setProperty("value", self.my_thread.conf)
        self.doubleSpinBox_iou.setProperty("value", self.my_thread.iou)
        self.line_weights.setText(self.my_thread.weights)

        # 判断复选框的勾选状态
        if self.my_thread.is_save == "checked":
            self.checkBox_isSave.setCheckState(Qt.Checked)
            self.my_thread.is_save = Qt.Checked

    # 显示检测的个数
    def show_detect_num(self, num):
        self.label_detect_num.setText(str(num))

    # 显示速度
    def show_speed(self, speed):
        self.label_speed.setText(speed)

    # 右下角的检测结果信息展示
    def show_detect_info(self, info):
        self.result_info.clear()
        self.result_info.append(info)


    # 控制暂停和播放
    def play_and_pause(self):
        # 如果检测的资源为空，提示先选择资源
        if self.my_thread.source == "":
            QMessageBox.information(self, '错误提示', '你还没选择检测的资源呢！')
            return
        if self.my_thread.play:
            # 原来是播放的，现在暂停了
            self.my_thread.play = False
        else:
            # 原来是暂停的，现在播放了
            self.my_thread.play = True
        # 更新播放和暂停的图标
        self.update_play_icon()

    # 选择检测图片
    def select_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                    "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
                                                    options=options)
        if image_path:
            self.end_thread()
            self.my_thread.source = image_path
            self.star_thread()

    # 勾选或者取消保存结果
    def save_result(self):
        self.my_thread.is_save = self.checkBox_isSave.checkState()

    # 检测视频
    def select_video(self):

        options = QFileDialog.Options()
        video_path, _ = QFileDialog.getOpenFileName(self, '选择视频', '',
                                                    'Videos (*.mp4 *.avi *.mkv);;All Files (*)', options=options)
        if video_path:
            self.end_thread()
            self.my_thread.source = video_path
            self.star_thread()


    # 检测文件夹
    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "", options=options)
        if folder_path:
            self.end_thread()
            self.my_thread.source = folder_path
            self.star_thread()

    # 检测摄像头
    def open_camera(self):
        self.dialog = QDialog(self.centralwidget)  # 创建摄像头弹窗
        self.dialog.setWindowTitle("请选择你的摄像头")  # 设置弹窗标题
        self.dialog.resize(400, 200)

        # 判断摄像头开启状态，如何开着设置为关，反之则开
        if self.camera_isOpen == True:
            # 开着的，现在关闭
            self.camera_isOpen = False
            # 跳出循环结束
            self.end_thread()
        else:
            num, deviceList = self.get_camera_num()
            # 如果没有摄像头，弹出提示框
            if num == 0:
                QMessageBox.warning(self, "出错啦", "<p>未检测到有效的摄像头</p>")
            # 如果有摄像头，弹出按钮，点击按钮后赋值对应的摄像头并打开开始检测
            else:
                self.camera_isOpen = True
                # 设置水平布局
                h_layout = QHBoxLayout(self.dialog)
                for xuhao in deviceList:
                    button = QPushButton(f'摄像头{xuhao}', self.dialog)
                    button.clicked.connect(lambda: self.click_camera(xuhao))
                    h_layout.addWidget(button)  # 为按钮添加布局
                # 显示对话框
                self.dialog.exec()

    # 选择对应的摄像头
    def click_camera(self, device):
        # 关闭对话框
        self.dialog.close()
        self.end_thread()
        self.my_thread.source = device
        self.star_thread()

    # 修改置信度
    def change_conf(self, x):
        self.my_thread.conf = round(x, 2)
        # 修改滑杆的值
        self.horizontalSlider_conf.setValue(x * 100)

    # 修改滑杆置信度的值
    def change_hor_conf(self, x):
        # 修改置信度的值和按钮的值
        conf = x * 0.01
        self.my_thread.conf = conf
        self.doubleSpinBox_conf.setValue(conf)

    # 修改IOU
    def change_iou(self, x):
        self.my_thread.iou = round(x, 2)
        # 修改滑杆的值
        self.horizontalSlider_iou.setValue(x * 100)

        # 修改滑杆iou的值

    def change_hor_iou(self, x):
        # 修改置信度的值和按钮的值
        iou = x * 0.01
        self.my_thread.iou = iou
        self.doubleSpinBox_iou.setValue(iou)

    # 结束线程
    def end_thread(self):
        self.my_thread.play = False
        self.my_thread.end_loop = True
        self.update_play_icon()
        self.my_thread.wait()
        # self.label_result.setPixmap(QtGui.QPixmap("test.png"))

    # def stop_thread(self):
    #
    #     self.stop_queue.put(True)
    #     self.join()  # Wait for the thread to finish

    # 启动线程
    def star_thread(self):
        self.my_thread.play = True
        self.my_thread.end_loop = False
        self.update_play_icon()
        self.my_thread.start()

    def show_detect(self, image, qt):
        try:
            ih, iw, _ = image.shape
            w = qt.geometry().width()
            h = qt.geometry().height()
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(image, (nw, nh))
            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(image, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            qt.setPixmap(QPixmap.fromImage(img))
            qt.setAlignment(Qt.AlignCenter)
        except Exception as e:
            print(repr(e))

    # 获取电脑摄像头的数量
    def get_camera_num(self):
        num = 0  # 计数器，用于记录找到的摄像头数量
        deviceList = []  # 列表，用于存储找到的摄像头设备索引

        for i in range(3):  # 遍历预设的摄像头数量范围,因为电脑一般不超过3个摄像头
            stream = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # 使用OpenCV库创建一个视频捕获对象，指定设备索引和捕获模式
            exists = stream.grab()  # 尝试从摄像头捕获一帧图像是否存在
            stream.release()  # 释放视频捕获对象
            if not exists:  # 如果未能成功捕获图像，则跳过当前设备继续循环
                continue
            else:
                num += 1  # 如果成功捕获图像，数量+1
                deviceList.append(i)  # 把对应的索引加入设备列表中
        return num, deviceList

    def select_weights(self):
        options = QFileDialog.Options()
        weights_path, _ = QFileDialog.getOpenFileName(self, '选择pt权重', '', 'pt (*.pt)', options=options)
        if weights_path:
            self.end_thread()
            self.line_weights.setText(weights_path)
            self.my_thread.weights = weights_path

    # 更新播放和暂停的图标
    def update_play_icon(self):
        icon = QtGui.QIcon()
        if self.my_thread.play:
            # 如果现在是播放着的，那么显示的是暂停的图标
            icon.addPixmap(QtGui.QPixmap("icon/暂停.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            # 如果现在是播放着的，那么显示的是暂停的图标
            icon.addPixmap(QtGui.QPixmap("icon/播放.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bofang.setIcon(icon)
        self.pushButton_bofang.setIconSize(QtCore.QSize(32, 32))

    # 关闭窗口事件
    def closeEvent(self, event):
        confirm = QMessageBox.question(self, '关闭程序', '确定关闭？',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # 确认关闭，保存用户数据
            config = dict()  # 创建一个空的字典
            config["conf"] = self.my_thread.conf
            config["iou"] = self.my_thread.iou
            config["weights"] = self.my_thread.weights
            if self.my_thread.is_save == Qt.Checked:
                config["is_save"] = "checked"
            else:
                config["is_save"] = "Unchecked"

            # 将修改后的配置参数写入 JSON 文件
            with open("config.json", "w") as jsonfile:
                json.dump(config, jsonfile, indent=4)
            # 退出循环，关闭流，防止摄像头等检测资源保存出错
            self.end_thread()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec())

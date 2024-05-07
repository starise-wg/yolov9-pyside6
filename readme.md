# 基于yolov9&pyside6 GUI实现目标检测系统v1.0

原创作者：**微智启软件工作室**

CSDN、B站：微智启工作室

技术客服QQ：3447362049

源码已申请版权，学术研究无限制，禁止商用盗卖，否则将承担法律侵权风险；如需合作请联系我们授权、备案。

**留言/举报邮箱：3447362049@qq.com**
## 环境配置+运行

1、在anaconda新建独立环境

`conda create -n yolo9 python=3.8 -y`

2、在新建的环境里面安装依赖

`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/  `

3、右键运行wzq.py

说明:如果默认采用上面的pip安装依赖，默认会安装CPU版。
如需安装GPU版，可以卸载torch和torchvision再重新安装，安装代码如下：

`conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch -y`

## 功能
该系统采用yolov9-c模型，可以检测80个物体，如需自定义检测，可以利用yolov9官方源码训练权重来识别。

目前支持单图、多图（文件夹）、视频、摄像头检测

可以选择是否保存检测结果

支持动态调制置信度和iou的值

右侧会显示检测的个数以及检测的结果类别统计

======================================

更多介绍，可以查阅CSDN：http://t.csdnimg.cn/tAbUY

如有未知问题或者bug，欢迎咨询技术客服QQ:3447362049
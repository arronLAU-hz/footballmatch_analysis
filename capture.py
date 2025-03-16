import cv2  # 导入 OpenCV 库，用于图像处理
import mss  # 导入 mss 库，用于屏幕截图
import numpy as np  # 导入 NumPy 库，用于数组操作

with mss.mss() as sct:  # 创建 mss 屏幕截图对象，使用 with 语句确保资源在使用完毕后正确释放
    # 监控器坐标，根据游戏窗口调整
    monitor = {"top": 100, "left": 100, "width": 800, "height": 600}
    # 定义要捕获的屏幕区域，以字典形式存储：
    # "top": 100,  # 距离屏幕顶部的像素数
    # "left": 100, # 距离屏幕左侧的像素数
    # "width": 800, # 捕获区域的宽度（像素）
    # "height": 600 # 捕获区域的高度（像素）

    while "Screen capturing":  # 进入无限循环，持续进行屏幕捕获
        # 获取屏幕截图
        sct_img = sct.grab(monitor)  # 使用 sct.grab() 函数捕获指定区域的屏幕图像，返回一个 mss 图像对象
        img = np.array(sct_img)  # 将 mss 图像对象转换为 NumPy 数组，方便 OpenCV 处理
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)  # 将图像的颜色空间从 RGBA 转换为 RGB，OpenCV 常用 RGB 格式

        # 在这里进行后续的图像处理和分析
        cv2.imshow("PES 2013 Capture", img)  # 使用 OpenCV 显示捕获的图像，窗口标题为 "PES 2013 Capture"

        if cv2.waitKey(25) & 0xFF == ord("q"):  # 等待 25 毫秒（控制帧率），并检测是否按下 'q' 键
            cv2.destroyAllWindows()  # 如果按下 'q' 键，关闭所有 OpenCV 显示窗口
            break  # 退出循环，结束程序

# 参数单位：
# "top", "left", "width", "height" 的单位都是像素（pixels）。q
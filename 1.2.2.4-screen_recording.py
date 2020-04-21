from PIL import ImageGrab
import numpy as np
from cv2 import cv2
import datetime
from pynput import keyboard
import threading

flag = False

def video_record():
    
    print("start recording at %s!" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    p = ImageGrab.grab()  # 获得当前屏幕
    a, b = p.size  # 获得当前屏幕的大小
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 帧率为12
    video = cv2.VideoWriter('%s.avi' % datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), fourcc, 12, (a, b))
    while True:
        img = ImageGrab.grab()
        img_cvt = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        video.write(img_cvt)
        if flag:
            print("stop recording!")
            break
    video.release()


def on_press(key):
    """
    :param key:
    :return:
    """
    global flag
    if key == keyboard.Key.esc:
        flag = True
        print("stop monitor！")
        return False  # 返回False，键盘监听结束.


if __name__ == '__main__':
    th = threading.Thread(target=video_record)
    th.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# 问题：获取频率可能取决于处理器速度，在我的笔记本上FPS约为10，比较低；由于以上原因写入文件回放会出现快放/慢放问题；码率太高。
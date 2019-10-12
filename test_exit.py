
# import signal
# import sys
# import time
# def handler(signal_num,frame):
#     print("\nYou Pressed Ctrl-C.")
#     sys.exit(signal_num)
# signal.signal(signal.SIGINT, handler)
# # 正常情况可以开始你自己的程序了。
# # 这里为了演示，我们做一个不会卡死机器的循环。
# while 1:
#     time.sleep(10)
# # 当你按下Ctrl-C的时候，应该会输出一段话，并退出.

import time
import sys
import os
def restart_program():
     python = sys.executable
     print("info:", os.execl(python, python, * sys.argv))
     #os.execl方法会代替自身进程，以达到自重启的目的。


if __name__ == "__main__":
     print('start...')
     print('pid : ', os.getpid())
     # print(u"3秒后,程序将结束...".encode("utf8"))
     print("3秒后,程序将结束...")
     time.sleep(3)
     restart_program()
     # os._exit(0)

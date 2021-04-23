# from google.colab import drive
import os

from .launcher import launcher

import sys
import os, subprocess

# p=subprocess.Popen('env',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
# oldEnv=p.communicate()[0]
# p=subprocess.Popen('source /tmp/test/setenv.sh ; env',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
# newEnv=p.communicate()[0]
# for newStr in newEnv.split('\n'):
#     flag = True
#     for oldStr in oldEnv.split('\n'):
#         if newStr == oldStr:
#             #not exported by setenv.sh
#             flag = False
#             break
#     if flag:
#         #exported by setenv.sh
#         print newStr


def auth():
    # email = input("Введите E-mail: ")
    # token = input("Введите Token: ")
    # drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())
    print(f"export EMAIL={email}")
    print(f"export TOKEN={token}")


def gdmount():
    pass

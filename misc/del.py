#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.startswith(".m4a"):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))
# test
if __name__ == "__main__":
    path = 'D:/undergraduatestudy/语音关键词录制-20230617/邱祎祎/'
    del_files(path)
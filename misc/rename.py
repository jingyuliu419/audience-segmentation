# # coding=utf-8
# import os
# import xlwt  # 操作excel模块
# import sys
#
# file_path = sys.path[0] + '\\filenamelist.xls'  # sys.path[0]为要获取当前路径，filenamelist为要写入的文件
# f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 新建一个excel
# sheet = f.add_sheet('sheet1')  # 新建一个sheet
# pathDir = os.listdir(sys.path[0])  # 文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录
#
# i = 0  # 将文件列表写入test.xls
# for s in pathDir:
#     sheet.write(i, 0, s)  # 参数i,0,s分别代表行，列，写入值
#     i = i + 1
#
# print(file_path)
# print(i)  # 显示文件名数量
# f.save(file_path)
import os


def re_fileName(path):
    fileList = os.listdir(path)
    num = 1
    for file in fileList:
        used_fileName, extension = os.path.splitext(file)
        new_file = str(num) + extension;
        os.rename(file, new_file)
        print("文件%s重命名成功，新的文件名为：%s" % (path + file, path + new_file))
        num += 1


if __name__ == '__main__':
    #     path="C:/Users/Administrator/Desktop/old/"        # 目标路径
    #     path = "C:\\Users\\Administrator\\Desktop\\old\\" # 目标路径
    path = r'D:/undergraduatestudy/语音关键词录制-20230617/吴菁岳-语音提示词-/'# 获取当前目录
    re_fileName(path)

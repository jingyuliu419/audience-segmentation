rows = 33
cols = 10

# 创建一个空的二维列表
my_list = [[] for _ in range(rows)]

# 使用两个嵌套的循环生成连续数字并添加到二维列表中
num = 0
for row in range(rows):
    for col in range(cols):
        my_list[row].append(num)
        num += 1

# 打印生成的二维列表
for row in my_list:
    print(row)
# print(my_list[1])


import shutil
import os
rows = 33
cols = 10

# 创建一个空的二维列表
my_list = [[] for _ in range(rows)]

# 使用两个嵌套的循环生成连续数字并添加到二维列表中
num = 0
for row in range(rows):
    for col in range(cols):
        my_list[row].append(num)
        num += 1

path_0=r"D:\undergraduatestudy\赵凝"
path=path_0.replace('\\','/')
path1_0=r"D:\undergraduatestudy\zn\新建文件夹"
path1=path1_0.replace('\\','/')

# filter=[".mav"] #设置过滤后的文件类型 当然可以设置多个类型

filenames=os.listdir(path)#获取需转文件名称数列
filenames1=os.listdir(path1)#获取要转入文件夹名称数列
for filename in filenames:
    filename=str(filename)
    if filename  not in ["new","test - 副本.py", "语音 播放遍历.py", "赵凝-语音关键词.wav", "filenamelist.xls", "获取文件名.py",'新建 文本文档.txt']:
        date=int(filename[:-4])
        print("{0}\n".format(date))
    # print(filename[:-4])
    j=0
    i=0
    while(j < 33):
        for filename1 in filenames1:
            filename1 = str(filename1)
            f = open('D:/undergraduatestudy/新建 文本文档.txt', encoding="UTF-8")

            data2 = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
            data2 = [x.strip() for x in data2]
            f.close()  # 关
            # a = ["new","test - 副本.py", "语音 播放遍历.py", "赵凝-语音关键词.wav", "filenamelist.xls", "获取文件名.py",'新建 文本文档.txt']
            # data2.extend(a)
            # print(filename1)
            # temp=filename.split('.')
            # print(filename[:-4]==filename1)
            for i in my_list[j]:

                # print("{0},{1}".format(filename,filename1))
                shutil.move(path + "/{0}".format(filenames[i]), path1 + "/{0}".format(data2[j]))
                i = i + 1
            else:
                print("失败将{0}移入{1}".format(filename, filename1))
        j=j+1

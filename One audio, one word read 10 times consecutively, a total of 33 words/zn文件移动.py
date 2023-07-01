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

f = open('D:/undergraduatestudy/新建 文本文档.txt', encoding="UTF-8")
dirs = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
dirs = [x.strip() for x in dirs]
f.close()  # 关
print(dirs)
i=0
j=0#33组
for dir in dirs:#33个文件夹
    for filename in filenames:#10个音频
        if int(filename[:-4]) in my_list[j]:
            shutil.move(path + "/"+filename, path1 + "/"+dir)
        else:
            print("失败将{0}移入{1}".format(filename, dir))
    j=j+1


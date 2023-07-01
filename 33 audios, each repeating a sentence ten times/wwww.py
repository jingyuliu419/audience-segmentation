# import shutil
# import os
# path=r"D:/undergraduatestudy/邱祎祎"
# path1=r"D:/undergraduatestudy/邱祎祎/新建文件夹"
#
# filter=[".mav"] #设置过滤后的文件类型 当然可以设置多个类型
#
# def all_path(dirname):
#
#     result = []#所有的文件
#
#     for maindir, subdir, file_name_list in os.walk(dirname):
#
#         for filename in file_name_list:
#             apath = os.path.join(maindir, filename)#合并成一个完整路径
#             ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
#
#             if ext in filter:
#                 result.append(apath)
#                 print(result)
#
#     return result
# def all_path1(dirname1):
#
#     result = []#所有的文件
#
#     for maindir, subdir, file_name_list in os.walk(dirname1):
#
#         for filename in file_name_list:
#             apath = os.path.join(maindir, filename)#合并成一个完整路径
#             # ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
#             result.append(apath)
#     return result
# filenames=all_path(path)
# filenames1=all_path1(path1)
# print(filenames)
# for filename in filenames:
#     filename=str(filename)
#     for filename1 in filenames1:
#         filename1 = str(filename1)
#         # temp=filename.split('.')
#         if filename==filename1:
#             print("{0},{1}".format(filename,filename1))
#             shutil.move('filename','filenames1')
import shutil
import os
path_0=r"D:\undergraduatestudy\梅坤"#需转文件地址
path=path_0.replace('\\','/')
path1_0=r"D:\undergraduatestudy\mk\新建文件夹"#要转入文件地址
path1=path1_0.replace('\\','/')

# filter=[".mav"] #设置过滤后的文件类型 当然可以设置多个类型

filenames=os.listdir(path)#需转文件名称
filenames1=os.listdir(path1)#需转入文件夹名称
for filename in filenames:
    filename=str(filename)
    # print(filename[:-4])
    for filename1 in filenames1:
        filename1 = str(filename1)
        # print(filename1)
        # temp=filename.split('.')
        # print(filename[:-4]==filename1)
        if filename[:-4]==filename1:
            # print("{0},{1}".format(filename,filename1))
            shutil.move(path+"/{0}".format(filename),path1+"/{0}".format(filename1))
        else:
            print("失败将{0}移入{1}".format(filename,filename1))
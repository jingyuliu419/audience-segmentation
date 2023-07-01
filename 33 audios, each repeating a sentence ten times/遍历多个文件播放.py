from pydub import AudioSegment
from pydub.silence import split_on_silence
import pyaudio
import wave
import os
chunk = 1024
path = os.getcwd()
path_0 = path.replace('\\','/')#到达人名文件夹
filter=[".py"]
filenames=os.listdir(path_0)#获取新建文件夹名
for filename in filenames:
    filename = str(filename)
    if filename in ["test.py","语音 播放遍历.py"]:
        continue
    else:
        path1 = path_0 + '/' + filename  # 到达新建文件夹
        # print("path1:"+path1)
        filenames1 = os.listdir(path1)  # 获取新建文件子文件夹名
        for filename1 in filenames1:
            filename1 = str(filename1)
            if filename1 not in filter:
                path3 = path1 + '/' + filename1  # 到达新建文件夹子文件夹
                # print("path3:" + path3)
                filenames2 = os.listdir(path3)  # 获取新建文件夹子文件夹名
                for filename2 in filenames2:
                    # filename2 = str(filename2)
                    # print("filename2:"+filename2)
                    f = open('C:/Users/liujiahao/PycharmProjects/pythonProject/新建 文本文档.txt',encoding="ANSI")

                    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
                    data=[x.strip() for x in data]
                    f.close()  # 关
                    a=["test.py","语音 播放遍历.py","心跳停了.wav","filenamelist.xls","获取文件名.py"]
                    data.extend(a)
                    # print(data)
                    # print(filename2 in data)
                    if filename2 in data:continue
                    print(filename2)
                    path4 = path3 + '/' + filename2
                    # print("path4:" + path4)
                    wf = wave.open(path4, 'rb')
                    p = pyaudio.PyAudio()
                    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)

                    data1 = wf.readframes(chunk)

                    while len(data1) > 0:
                        stream.write(data1)
                        data1 = wf.readframes(chunk)

                    stream.stop_stream()
                    stream.close()
                    p.terminate()

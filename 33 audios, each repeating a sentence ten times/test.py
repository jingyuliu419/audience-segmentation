from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
path = os.getcwd()
path_0 = path.replace('\\','/')#到达人名文件夹
filter=[".py"]
filenames=os.listdir(path_0)#获取新建文件夹名
for filename in filenames:
    filename = str(filename)
    if filename=="test.py":
        continue
    else:
        path1 = path_0 + '/' + filename  # 到达新建文件夹
        print("path1"+path1)
        filenames1 = os.listdir(path1)  # 获取新建文件子文件夹名
        for filename1 in filenames1:
            filename1 = str(filename1)
            if filename1 not in filter:
                path3 = path1 + '/' + filename1  # 到达新建文件夹子文件夹
                print(path3)
                filenames2 = os.listdir(path3)  # 获取新建文件夹子文件夹名
                for filename2 in filenames2:
                    filename2 = str(filename2)
                    path4 = path3 + '/' + filename2  # 到达新建文件夹子文件夹文件
                    print(path4)
                    #filenames3 = os.listdir(path4)  # 获取新建文件夹子文件夹的文件
                    # filename3 = filenames3[0]
                    # path5 = path4 + '/' + filename3
                    sound = AudioSegment.from_mp3(path4)
                    loudness = sound.dBFS
                    # print(loudness)
                    chunks = split_on_silence(sound,
                                              # must be silent for at least half a second,沉默半秒
                                              min_silence_len=430,

                                              # consider it silent if quieter than -16 dBFS
                                              silence_thresh=-45,
                                              keep_silence=400

                                              )
                    #print('总分段：', len(chunks))
                    # 放弃长度小于0.02秒的录音片段
                    for i in list(range(len(chunks)))[::-1]:
                        if len(chunks[i]) <= 20 or len(chunks[i]) >= 10000:
                            chunks.pop(i)
                    #print('取有效分段(大于2s小于10s)：', len(chunks))
                    if len(chunks)<10:
                        print(path4)
                        print('取有效分段(大于2s小于10s)：', len(chunks))
                    for i, chunk in enumerate(chunks):
                        chunk.export(
                            path3+'/'+filename2[:-4]+'{0}.wav'.format(i),
                            format="wav")
                        # print(i)


    #if filename not in filter:

        #path2 = all_path(path1)  # 到达新建文件夹
        # path3=all_path(path2)#到达新建文件夹子文件夹
        # path4=all_path(path3)#到达新建文件夹子文件夹的文件


# '''
# for x in range(0,int(len(sound)/1000)):
#     print(x,sound[x*1000:(x+1)*1000].max_dBFS)
# '''


import numpy as np
import cv2
import os,sys
from PIL import Image
import shutil
from tqdm import tqdm
from argparse import ArgumentParser

def rename_video(path):
    # image_path=os.path.join(path,"images/")
    fileList= os.listdir(path)
    index=0
    print ("image_path:",path)
    for f in fileList:
        if f.endswith('.mp4'):

            print("image_path[index]:",fileList[index])
            oldname=path+ os.sep + fileList[index]   # os.sep添加系统分隔符
    
            #设置新文件名
            newname=path + os.sep +'cam'+str(index).zfill(2)+'.mp4'
    
            os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
            index+=1
            print(oldname,'======>',newname)





if __name__ == '__main__':
    parser = ArgumentParser(description="Extract images from dynerf videos")
    parser.add_argument("-i","--datadir", default='data/dynerf/cut_roasted_beef', type=str)
    args = parser.parse_args()

    # print("args.datadir:", args.datadir)

    rename_video(args.datadir)
    # load_images_path(args.datadir)


    # create_colmap_images(args.datadir)

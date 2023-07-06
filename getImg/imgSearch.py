import os
from PIL import Image

#  压缩图片
def compressImage(src_path, dst_path):
    # 获取目录下全部文件
    for filename in os.listdir(src_path):
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        srcFile = os.path.join(src_path, filename)
        dstFile = os.path.join(dst_path, filename)
        if os.path.isfile(srcFile):
            try:
                img = Image.open(srcFile)
                print(img.size)
                if img.size[0] >= 1920 and img.size[1] > 1080:
                    box = (0, 0, 1920, 1080)
                    region = img.crop(box)
                    region.save(dstFile)
            except Exception:
                print(dstFile + "失败！")
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == '__main__':
    compressImage("./images", "./back")

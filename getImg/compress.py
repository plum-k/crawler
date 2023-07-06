from PIL import Image
import os

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
                img.save(dstFile, quality=20)
            except Exception:
                print(dstFile + "失败！")
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == '__main__':
    compressImage("./images", "./out")

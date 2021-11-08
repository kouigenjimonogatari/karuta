import cv2
import glob
import os
from PIL import Image

files = glob.glob("../../viewer/static/data/karuta/raw/*.jpg")

for file in files:

    opath = file.replace("raw", "image")

    if os.path.exists(opath):
        continue

    # 画像の読み込み
    img = cv2.imread(file, 0)

    ret, img_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

    # 二値化画像の表示
    cv2.imwrite(opath, img_thresh)

    imgfile = Image.open(opath).convert('RGB')
    imgfile.save(opath.replace(".jpg", ".webp"),'webp')
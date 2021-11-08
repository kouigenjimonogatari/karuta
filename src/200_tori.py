import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import Image
import pandas as pd

inputPath = "data/genji.csv"

# 使うフォント，サイズ，描くテキストの設定
ttfontname = "/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc"
fontsize = 140

df = pd.read_csv(inputPath)

index2 = 0

for index, row in enumerate(df.itertuples()):
    index = row[0]

    if index < 15:
        continue

    text = row[6]

    if pd.isnull(text):
        continue

    text = text.replace(" ", "")
    
    index2 += 1

    # 画像サイズ，背景色，フォントの色を設定
    canvasSize    = (600, 800)
    backgroundRGB = (255, 255, 255)
    textRGB       = (0, 0, 0)

    # 文字を描く画像の作成
    img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
    draw = PIL.ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = PIL.ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)

    count = 0

    for col in range(3):
        for row in range(5):

            if len(text) == count:
                break
            
            ch = text[count]

            count += 1

            textTopLeft = (430 - 200 * col, 10 + 160 * row) # 前から1/6，上下中央に配置
            draw.text(textTopLeft, ch, fill=textRGB, font=font)

    opath = "../docs/tori/{}.png".format(str(index2).zfill(3))

    img.save(opath)

    imgfile = Image.open(opath).convert('RGB')
    imgfile.save(opath.replace(".png", ".webp"),'webp')
#!/usr/bin/env python
import DaVinciResolveScript as dvr_script
import pathlib
from PIL import Image, ImageDraw, ImageFont

def makeMetaString(list):
    str = ""
    for row in list:
        if (row[1] != ""):
            str += "{} : {}\n".format(row[0], row[1])

    return str

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
mediastorage = resolve.GetMediaStorage()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    # パス取得
    filePath = clip.GetClipProperty("File Path")

    # メタ情報取得 BRAW
    meta = []
    meta.append(["Camera", clip.GetMetadata("Camera Type")])
    meta.append(["Lens", clip.GetMetadata("Lens Type")])
    meta.append(["Aperture", clip.GetMetadata("Camera Aperture")])
    meta.append(["ISO", clip.GetMetadata("ISO")])
    meta.append(["Shutter Speed", clip.GetMetadata("Shutter")])
    meta.append(["Focal Point", clip.GetMetadata("Focal Point (mm)")])
    meta.append(["Distance", clip.GetMetadata("Distance")])
    meta.append(["FPS", clip.GetClipProperty("FPS")])
    meta.append(["WB", clip.GetMetadata("White Point (Kelvin)")])
    meta.append(["Tint", clip.GetMetadata("White Balance Tint")])

    metaStr = makeMetaString(meta)

    # 画像生成(日本語非対応)
    # todo フォントMacはどうするか
    font = ImageFont.truetype("meiryo.ttc", 32)
    # todo サイズは自動調整したい
    im = Image.new("RGB",(900,400), "black")
    draw = ImageDraw.Draw(im)
    draw.text((0,0), metaStr, font=font)

    # アルファチャンネル作成
    alpha = im.convert("L")
    im.putalpha(alpha)

    # 動画ファイルの拡張子だけ変更した名前で画像を置く
    savePath = pathlib.PurePath(filePath).with_suffix(".png")
    im.save(str(savePath))

    # メディアプール登録
    # mediastorage.AddItemListToMediaPool(savePath)
    # mediastorage.AddItemsToMediaPool(savePath)




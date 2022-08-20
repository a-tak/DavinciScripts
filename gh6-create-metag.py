#!/usr/bin/env python
import DaVinciResolveScript as dvr_script
import pathlib
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
from pyexifinfo import information

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

    # movだけを対象にする
    if pathlib.Path(filePath).suffix.lower() != ".mov" :
        continue
    
    # メタ情報取得
    meta = []
    data = information(filePath)
    meta.append(["Camera", data.get("EXIF:Model")])
    meta.append(["Lens", data.get("Composite:LensID")])
    meta.append(["Aperture", data.get("Composite:Aperture")])
    meta.append(["ISO", data.get("EXIF:ISO")])
    meta.append(["Shutter Speed", data.get("Composite:ShutterSpeed")])
    meta.append(["Focal Point", data.get("Composite:FocalLength35efl")])
    meta.append(["Distance", data.get("Composite:HyperfocalDistance")])
    meta.append(["FPS", clip.GetClipProperty("FPS")])
    
    # ホワイトバランスだけはXMLから取得
    xml = ET.fromstring(data.get("QuickTime:PanasonicSemi-ProMetadataXml"))
    for item in xml.iter("{urn:schemas-Professional-Plug-in:P2:CameraMetadata:v1.2}WhiteBalanceColorTemperature"):
        meta.append(["WB", item.text])

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
    savePath = str(pathlib.PurePath(filePath).with_suffix(".png"))
    im.save(savePath)

    # メディアプール登録
    mediastorage.AddItemListToMediaPool(savePath)




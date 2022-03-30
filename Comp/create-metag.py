#!/usr/bin/env python
import DaVinciResolveScript as dvr_script
import pathlib
from PIL import Image, ImageDraw

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    # パス取得
    filePath = clip.GetClipProperty("File Path")
    # filebase = pathlib.PurePath.name(filePath)
    # folder = pathlib.Path(filePath).parent

    # メタ情報取得
    camera = clip.GetMetadata("Camera Type")
    lens = clip.GetMetadata("Lens Type")
    f = clip.GetMetadata("Camera Aperture")
    iso = clip.GetMetadata("ISO")
    shutter = clip.GetMetadata("Shutter")
    focalPoint = clip.GetMetadata("Focal Point (mm)")
    distance = clip.GetMetadata("Distance")
    tint = clip.GetMetadata("White Balance Tint")
    wb = clip.GetMetadata("White Point (Kelvin)")

    # 画像生成(日本語非対応)
    im = Image.new("RGB",(300,300), "blue")
    draw = ImageDraw.Draw(im)
    draw.text((0,0), "Camera : {}".format(camera))
    # 動画ファイルの拡張子だけ変更した名前で画像を置く
    savePath = pathlib.PurePath(filePath).with_suffix(".png")
    print(savePath)
    im.save(str(savePath))

    # メディアプール登録


#!/usr/bin/env python
import DaVinciResolveScript as dvr_script
from pyexifinfo import information

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    filePath = clip.GetClipProperty("File Path")
    print(filePath)
    meta = information(filePath)
    # print(meta)
    print(meta["QuickTime:CameraType"]) # カメラ
    print(meta["QuickTime:LensType"])   # レンズ
    print(meta["QuickTime:VideoFrameRate"]) # FPS



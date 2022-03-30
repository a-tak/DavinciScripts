#!/usr/bin/env python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    print(clip.GetMetadata("Camera Type"))
    print(clip.GetMetadata("Lens Type"))
    print(clip.GetMetadata("Camera Aperture"))
    print(clip.GetMetadata("ISO"))
    print(clip.GetMetadata("Shutter"))
    print(clip.GetMetadata("Focal Point (mm)"))
    print(clip.GetMetadata("Distance"))
    print(clip.GetMetadata("White Balance Tint"))
    print(clip.GetMetadata("White Point (Kelvin)"))


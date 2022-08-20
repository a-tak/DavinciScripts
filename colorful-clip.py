#!/usr/bin/env python
import DaVinciResolveScript as dvr_script
resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()
color = ["Orange","Blue","Apricot","Navy","Yellow","Teal","Brown","Lime","Purple","Beige","Olive","Violet","Green","Chocolate","Pink","Tan"]
i = 0
for clip in folder.GetClipList():
    clip.SetClipColor(color[i])
    i+=1
    if len(color) < i+1:
        i=0

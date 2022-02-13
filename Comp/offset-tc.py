#!/usr/bin/env python
import sys
import DaVinciResolveScript as dvr_script
from timecode import Timecode

# ここにタイムコードとフレームレートを手打ち(笑)
videoTc = "12:44:29:44"
audioTc = "12:44:39:36"
fps=59.94

diff = Timecode(fps, audioTc) - Timecode(fps, videoTc)
print("DiffTC",diff)

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    startTc = clip.GetClipProperty("Start TC")
    changedTc = Timecode(fps, Timecode(fps, startTc)) + diff
    print(clip.GetName(), startTc, changedTc)
    clip.SetClipProperty("Start TC", str(changedTc))

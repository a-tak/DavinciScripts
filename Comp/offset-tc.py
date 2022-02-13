#!/usr/bin/env python
import sys
import DaVinciResolveScript as dvr_script
from timecode import Timecode

# ここにタイムコードとフレームレートを手打ち(笑)
videoTc = "12:44:39:36"
audioTc = "12:46:36:38"
videoFps=59.94
audioFps=60

diff = Timecode(videoFps, audioTc) - Timecode(audioFps, videoTc)
print("DiffTC",diff)

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    startTc = clip.GetClipProperty("Start TC")
    changedTc = Timecode(videoFps, Timecode(videoFps, startTc)) + diff
    print(clip.GetName(), startTc, changedTc)
    clip.SetClipProperty("Start TC", str(changedTc))

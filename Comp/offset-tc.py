#!/usr/bin/env python
import sys
import DaVinciResolveScript as dvr_script
from timecode import Timecode

# ここにタイムコードとフレームレートを手打ち(笑)
videoTimeCode = "12:40:15:49"
audioTimeCode = "12:44:39:36"
fps=59.94

videoTc = Timecode(fps, videoTimeCode)
audioTc = Timecode(fps, audioTimeCode)

diff =  audioTc - videoTc

resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediapool = project.GetMediaPool()
folder = mediapool.GetCurrentFolder()

for clip in folder.GetClipList():
    startTc = clip.GetClipProperty("Start TC")
    if videoTc.frames > audioTc.frames:
        changedTc = Timecode(fps, Timecode(fps, startTc)) - diff
    else:
        changedTc = Timecode(fps, Timecode(fps, startTc)) + diff
    print(clip.GetName(), startTc, str(changedTc))
    clip.SetClipProperty("Start TC", str(changedTc))

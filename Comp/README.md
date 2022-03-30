# Scripts

## colorful-clip

開いているビンのクリップに別々の色を付けてクリップを見分けやすくします

## offset-tc

クリップのタイムコードを一括でずらすスクリプト

### 注意

* 実行後は取消できないので注意が必要です
  * 元のTCに戻す場合はおそらくメディアプールに素材を再度投入し直す必要があります
* DaVinci Resolve 17.4.4のScripting APIではバグがあるようでSetClipPropertyでStart TCを指定した際に開始フレームではなく現在のフレームのタイムコードを変更してしまいます。各クリップの再生ヘッドを先頭に持ってこないと正しく処理されません。

### 使い方

* 動画が入っているビンに移動して実行すること
* ソースのvideoTcに動画のタイムコード、audioTcに音声のタイムコード、fpsにフレームレートを入れる
* 差分を計算し動画のタイムコードを音声のタイムコードに合うようにオフセットかけます

### 必要モジュール

```powershell
pip install timecode
```

## create-metag(作成途中)

動画のメタデータ情報の画像を生成する。
現在、メタデータの取得まで。

### 使い方(予定)

* 動画が入っているビンに移動して実行すること
* 同じビンにクリップメイト同じ画像が登録される

####  Pythonモジュール
```powershell
pip install Pillow
```

### ExifInfoで取得できるメタデータサンプル

```
{'SourceFile': 'E:/DaVinci Resolve Data/2022-03-27_?_?C?ƈ??S?s?̍??`???????W/BMPCC/A071_03270652_C013.braw', 'ExifTool:ExifToolVersion': 12.4, 'ExifTool:Warning': 'FileName encoding not specified', 'File:Directory': 'E:/DaVinci Resolve Data/2022-03-27_?_?C?ƈ??S?s?̍??`???????W/BMPCC', 'File:FileAccessDate': '2022:03:30 20:35:16+09:00', 'File:FileCreateDate': '2022:03:27 06:52:53+09:00', 'File:FileModifyDate': '2022:03:27 06:52:53+09:00', 'File:FileName': 'A071_03270652_C013.braw', 'File:FilePermissions': '-rw-rw-rw-', 'File:FileSize': '393 MiB', 'File:FileType': 'MOV', 'File:FileTypeExtension': 'mov', 'File:MIMEType': 'video/quicktime', 'QuickTime:AnalogGain': 1, 'QuickTime:AnalogGainIsConstant': '(Binary data 2 bytes, use -b option to extract)', 'QuickTime:AnamorphicEnable': '(Binary data 2 bytes, use -b option to extract)', 'QuickTime:AspectRatio': '2.35:1', 'QuickTime:AudioBitsPerSample': 16, 'QuickTime:AudioChannels': 2, 'QuickTime:AudioFormat': 'in24', 'QuickTime:AudioSampleRate': 48000, 'QuickTime:Balance': 0, 'QuickTime:BitDepth': 0, 'QuickTime:BrawCodecBitrate': '(Binary data 4 bytes, use -b option to extract)', 'QuickTime:BrawCompressionRatio': 'Q3', 'QuickTime:CameraId': '07d7ff6c-2be9-40d6-b5e3-aa7b1e0cf463', 'QuickTime:CameraNumber': 'A', 'QuickTime:CameraType': 'Blackmagic Pocket Cinema Camera 4K', 'QuickTime:ClipNumber': 'A071_03270652_C013', 'QuickTime:CompressorID': 'brvo', 'QuickTime:CreateDate': '2022:03:26 21:52:53', 'QuickTime:CropOrigin': '(Binary data 8 bytes, use -b option to extract)', 'QuickTime:CropSize': '(Binary data 8 bytes, use -b option to extract)', 'QuickTime:CurrentTime': '0 s', 'QuickTime:DateRecorded': '2022:03:27', 'QuickTime:DayNight': 'day', 'QuickTime:Duration': '12.83 s', 'QuickTime:Endianness': 'Little-endian (Intel, II)', 'QuickTime:Environment': 'exterior', 'QuickTime:FirmwareVersion': 7.3, 'QuickTime:FormatFrameRate': '(Binary data 4 bytes, use -b option to extract)', 'QuickTime:GenBalance': 0, 'QuickTime:GenFlags': '0 0 0', 'QuickTime:GenGraphicsMode': 'ditherCopy', 'QuickTime:GenMediaVersion': 0, 'QuickTime:GenOpColor': '32768 32768 32768', 'QuickTime:GoodTake': False, 'QuickTime:GraphicsMode': 'ditherCopy', 'QuickTime:HandlerClass': 'Data Handler', 'QuickTime:HandlerDescription': 'Apple Alias Data Handler', 'QuickTime:HandlerType': 'Metadata Tags', 'QuickTime:HandlerVendorID': 'Apple', 'QuickTime:ImageHeight': 2176, 'QuickTime:ImageWidth': 4128, 'QuickTime:LensType': 'OLYMPUS M.12-100mm F4.0', 'QuickTime:Manufacturer': 'Blackmagic Design', 'QuickTime:MatrixStructure': '1 0 0 0 1 0 0 0 1', 'QuickTime:MediaCreateDate': '2022:03:26 21:52:53', 'QuickTime:MediaDataOffset': 16, 'QuickTime:MediaDataSize': 411652080, 'QuickTime:MediaDuration': '12.83 s', 'QuickTime:MediaHeaderVersion': 0, 'QuickTime:MediaModifyDate': '2022:03:26 21:52:53', 'QuickTime:MediaTimeScale': 30, 'QuickTime:ModifyDate': '2022:03:26 21:52:53', 'QuickTime:MovieHeaderVersion': 0, 'QuickTime:MulticardTimecode': '(Binary data 4 bytes, use -b option to extract)', 'QuickTime:MulticardVolumeCount': '(Binary data 4 bytes, use -b option to extract)', 'QuickTime:MulticardVolumeNumber': '(Binary data 4 bytes, use -b option to extract)', 'QuickTime:NextTrackID': 4, 'QuickTime:OpColor': '32768 32768 32768', 'QuickTime:OtherFormat': 'tmcd', 'QuickTime:Post_3dlutEmbeddedBmdGamma': '', 'QuickTime:Post_3dlutEmbeddedData': '(Binary data 431244 bytes, use -b option to extract)', 'QuickTime:Post_3dlutEmbeddedName': 'Blackmagic Gen 5 Film to Extended Video.cube', 'QuickTime:Post_3dlutEmbeddedSize': '(Binary data 2 bytes, use -b option to extract)', 'QuickTime:Post_3dlutEmbeddedTitle': 'Gen 5 Film to Extended Video', 'QuickTime:Post_3dlutMode': 'Disabled', 'QuickTime:PosterTime': '0 s', 'QuickTime:PreferredRate': 1, 'QuickTime:PreferredVolume': '100.00%', 'QuickTime:PreviewDuration': '0 s', 'QuickTime:PreviewTime': '0 s', 'QuickTime:PurchaseFileFormat': 'in24', 'QuickTime:ReelName': 71, 'QuickTime:Scene': 1, 'QuickTime:SelectionDuration': '0 s', 'QuickTime:SelectionTime': '0 s', 'QuickTime:ShotType': 'WS', 'QuickTime:ShutterType': 'Angle', 'QuickTime:SourceImageHeight': 2176, 'QuickTime:SourceImageWidth': 4128, 'QuickTime:Take': 13, 'QuickTime:TimeCode': 3, 'QuickTime:TimeScale': 30, 'QuickTime:ToneCurveContrast': 1, 'QuickTime:ToneCurveHighlights': 1, 'QuickTime:ToneCurveMidpoint': 0.409007728099823, 'QuickTime:ToneCurveSaturation': 1, 'QuickTime:ToneCurveShadows': 1, 'QuickTime:ToneCurveVideoBlackLevel': '(Binary data 2 bytes, use -b option to extract)', 'QuickTime:TrackCreateDate': '2022:03:26 21:52:53', 'QuickTime:TrackDuration': '12.83 s', 'QuickTime:TrackHeaderVersion': 0, 'QuickTime:TrackID': 1, 'QuickTime:TrackLayer': 0, 'QuickTime:TrackModifyDate': '2022:03:26 21:52:53', 'QuickTime:TrackVolume': '0.00%', 'QuickTime:VideoFrameRate': 30, 'QuickTime:ViewingBmdgen': '(Binary data 2 bytes, use -b option to extract)', 'QuickTime:ViewingGamma': 'Blackmagic Design Film', 'QuickTime:ViewingGamut': 'Blackmagic Design', 'QuickTime:XResolution': 72, 'QuickTime:YResolution': 72, 'Composite:AvgBitrate': '257 Mbps', 'Composite:ImageSize': '4128x2176', 'Composite:LensID': 'OLYMPUS M.12-100mm F4.0', 'Composite:Megapixels': 9.0, 'Composite:Rotation': 0}
```

## property-list

クリップのプロパティー名とメタデータ名を確認する為のスクリプト

↓結果。これが全てではない可能性はある

### プロパティー
```
{
  "Alpha mode": "None",
  "Angle": "",
  "Audio Bit Depth": "32",
  "Audio Ch": "2",
  "Audio Codec": "AAC",
  "Audio Offset": "",
  "Bit Depth": "8",
  "Camera #": "",
  "Clip Color": "",
  "Clip Name": "GX010184.MP4",
  "Comments": "",
  "Data Level": "Auto",
  "Date Added": "土 2月 5 2022 21: 47: 06",
  "Date Created": "土 2月 5 2022 13: 37: 18",
  "Date Modified": "Sat Feb  5 13: 37: 26 2022",
  "Description": "",
  "Drop frame": "0",
  "Duration": "00: 00: 06: 59",
  "Enable Deinterlacing": "0",
  "End": "418",
  "End TC": "13: 36: 36: 20",
  "FPS": 59.94,
  "Field Dominance": "Auto",
  "File Name": "GX010184.MP4",
  "File Path": "C:\\DaVinci Resolve\\folder\\GoPro\\GX010184.MP4",
  "Flags": "",
  "Format": "QuickTime",
  "Frames": "419",
  "Good Take": "",
  "H-FLIP": "オフ",
  "IDT": "",
  "In": "",
  "Input Color Space": "プロジェクト",
  "Input LUT": "",
  "Input Sizing Preset": "None",
  "Keyword": "",
  "Noise Reduction": "",
  "Offline Reference": "",
  "Out": "",
  "PAR": "Square",
  "Proxy": "None",
  "Proxy Media Path": "",
  "Reel Name": "",
  "Resolution": "3840x2160",
  "Roll/Card": "",
  "S3D Sync": "",
  "Sample Rate": "48000",
  "Scene": "",
  "Sharpness": "",
  "Shot": "",
  "Slate TC": "13: 36: 29: 21",
  "Start": "0",
  "Start KeyKode": "",
  "Start TC": "13: 36: 29: 21",
  "Synced Audio": "",
  "Take": "",
  "Type": "ビデオ + オーディオ",
  "Usage": "0",
  "V-FLIP": "オフ",
  "Video Codec": "H.265 Main L6.0",
  "Super Scale": 1
}
```
### メタデータ
```
{'Camera #': 'A',
'Camera Aperture': 'f10.0',
'Camera FPS': '30.000',
'Camera Firmware': '7.3',
'Camera ID': '07d7ff6c-2be9-40d6-b5e3-aa7b1e0cf463',
'Camera Manufacturer': 'Blackmagic Design',
'Camera Type': 'Blackmagic Pocket Cinema Camera 4K',
'Clip Number': 'A071_03270652_C013',
'Codec Bitrate': '252508080',
'Color Space Notes': 'Blackmagic Design',
'Compression Ratio': 'Q3',
'Date Recorded': '2022: 03: 27',
'Day / Night': 'day',
'Distance': '2925mm',
'Environment': 'exterior',
'Focal Point (mm)': '23mm',
'Gamma Notes': 'Blackmagic Design Film',
'Good Take': 'false',
'ISO': '800',
'LUT Used': 'Blackmagic Gen 5 Film to Extended Video.cube',
'Lens Type': 'OLYMPUS M.12-100mm F4.0',
'ND Filter': '0',
'Reel Number': '71',
'Scene': '1',
'Shot Type': 'WS',
'Shutter': '270°',
'Shutter Type': 'Angle',
'Take': '13',
'White Balance Tint': '10',
'White Point (Kelvin)': '5600'
}
```
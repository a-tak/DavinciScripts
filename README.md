# DaVinci Resolve Python Scripts

## はじめに

Windows環境での使い方を記載。Macの場合は[こちら](https://note.com/littlebuddha/n/nf7325e8c16ea)参考にされると良いかもしれません。

DaVinci Resolve 17 Studioで動作確認しています。

## Pythonインストール

Python 3.6系を必ずインストール。3.10などでは動作しない。

Chocolateyを使用する場合を以下に記載するが、誤ってアップグレードすると3.6系より最新に更新されてしまうのでお勧めしない。

```powershell
choco install -y python3 -Version 3.6.8
```

## 環境変数設定

以下のドキュメントに沿って環境変数を指定。

`C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\README.txt`

ただし、PYTHONPATHについては絶対パスじゃない動作しなかったので以下のように設定した。

`%PYTHONPATH%;C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules`

## 作成したスクリプトの置き場

先のドキュメントの記載に間違いがあり以下に配置する必要がある。

`C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\`

このリポジトリはこのScripts配下を再現している。

## 環境設定の変更

`環境設定` > `システム` > `一般` > `一般環境設定` > `外部スクリプトに使用` を `ローカル` に変更

## スクリプトの実行

`ワークスペース` の `スクリプト` から実行可能

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

### 使い方(予定)

* 動画が入っているビンに移動して実行すること
* 画像が生成されるのでメディアプールに登録して利用する

####  Pythonモジュール
```powershell
pip install Pillow
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
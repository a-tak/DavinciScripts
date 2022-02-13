# Scripts

## colorful-clip

開いているビンのクリップに別々の色を付けてクリップを見分けやすくします

## offset-tc

クリップのタイムコードを一括でずらすスクリプト

### 注意

* 実行後は取消できないので注意が必要です
  * 元のTCに戻す場合はおそらくメディアプールに素材を再度投入し直す必要があります

### 使い方

* 動画が入っているビンに移動して実行すること
* ソースのvideoTcに動画のタイムコード、audioTcに音声のタイムコード、fpsにフレームレートを入れる
* 差分を計算し動画のタイムコードを音声のタイムコードに合うようにオフセットかけます

### 必要モジュール

```powershell
pip install timecode
```

## property-list

クリップのプロパティー名を確認する為のスクリプト

↓結果。これが全てではない可能性はある

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
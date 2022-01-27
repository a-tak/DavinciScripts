# DaVinci Resolve Python Scripts

## はじめに

Windows環境での使い方を記載。Macの場合は[こちら](https://note.com/littlebuddha/n/nf7325e8c16ea)参考にされると良いかもしれません。

## Pythonインストール

Python 3.6系を必ずインストール。3.10などでは動作しない。

Chocolateyを使用する場合

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

## スクリプトの実行

`ワークスペース` の `スクリプト` から実行可能

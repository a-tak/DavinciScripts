#!/usr/bin/env python
from time import time
import DaVinciResolveScript as dvr_script
import pathlib
from PIL import Image, ImageDraw, ImageFont

class MetaImageCreator():
    def execute(self):
        resolve = dvr_script.scriptapp("Resolve")
        projectManager = resolve.GetProjectManager()
        project = projectManager.GetCurrentProject()
        timeline = project.GetCurrentTimeline()
        mediastorage = resolve.GetMediaStorage()
        mediaPool = project.GetMediaPool()

        print(timeline.GetName())

        # TODO どのトラックを対象にするかがコード埋め込み
        for item in timeline.GetItemListInTrack("video", 1):
            mediaPoolItem = item.GetMediaPoolItem()
            filePath = mediaPoolItem.GetClipProperty("File Path")

            # brawだけを対象にする
            if pathlib.Path(filePath).suffix.lower() != ".braw" :
                continue

            # メタ情報取得 BRAW
            meta = self.makeBrawMetaList(mediaPoolItem)
            metaStr = self.makeMetaString(meta)
            savePath = self.createImage(metaStr, filePath)

            # メディアプール登録
            # ToDo 現在トップに登録されてしまう
            mediaPoolItems = mediastorage.AddItemListToMediaPool(savePath)
            if len(mediaPoolItems) != 1:
                raise Exception("AddItemListToMediaPoolの登録に失敗しました {}個の登録".format(len(mediaPoolItems)))

            # タイムラインへ登録
            self.addMetadataImage(timeline, item, mediaPool, mediaPoolItems[0])
    
    def addMetadataImage(self, timeline, sourceItem, mediaPool, metadataItem):
        """タイムラインにメタデータ画像を追加する

        Args:
            timeline (Timeline): 追加対象のタイムライン
            sourceItem (TimelineItem): メタデータ生成元の動画
            mediaPool(mediaPool): メディアプールオブジェクト
            metadataItem (MediaPoolItem): メタデータの画像
        """
        
        mediaPool.AppendToTimeline(metadataItem)
        print(metadataItem.GetName())


    def makeMetaString(self, list):
        str = ""
        for row in list:
            if (row[1] != ""):
                str += "{} : {}\n".format(row[0], row[1])

        return str

    def makeBrawMetaList(self, mediaPoolItem):
        """BRAWメタデータ画像用の文字列を生成する

        Args:
            mediaPoolItem (mediaPoolItem): 画像を生成したいDaVinci Resolveのメディアプールアイテム

        Returns:
            str: 結果のメタデータの文字列
        """
        meta = []
        meta.append(["Camera", mediaPoolItem.GetMetadata("Camera Type")])
        meta.append(["Lens", mediaPoolItem.GetMetadata("Lens Type")])
        meta.append(["Aperture", mediaPoolItem.GetMetadata("Camera Aperture")])
        meta.append(["ISO", mediaPoolItem.GetMetadata("ISO")])
        meta.append(["Shutter Speed", mediaPoolItem.GetMetadata("Shutter")])
        meta.append(["Focal Point", mediaPoolItem.GetMetadata("Focal Point (mm)")])
        meta.append(["Distance", mediaPoolItem.GetMetadata("Distance")])
        meta.append(["FPS", mediaPoolItem.GetClipProperty("FPS")])
        meta.append(["WB", mediaPoolItem.GetMetadata("White Point (Kelvin)")])
        meta.append(["Tint", mediaPoolItem.GetMetadata("White Balance Tint")])

        return meta

    def createImage(self, metaStr, filePath):
        """文字列の画像化

        Args:
            metaStr (str): 画像化する文字列
            filePath (str): 書き出し先のフルパス。拡張子は自動でpngに変更される。

        Returns:
            str: 保存された画像のフルパス
        """
        # 画像生成(日本語非対応)
        # todo フォントMacはどうするか
        font = ImageFont.truetype("meiryo.ttc", 32)
        # todo サイズは自動調整したい
        im = Image.new("RGB",(900,400), "black")
        draw = ImageDraw.Draw(im)
        draw.text((0,0), metaStr, font=font)

        # アルファチャンネル作成
        alpha = im.convert("L")
        im.putalpha(alpha)

        # 動画ファイルの拡張子だけ変更した名前で画像を置く
        savePath = str(pathlib.PurePath(filePath).with_suffix(".png"))
        im.save(savePath)

        return savePath            

if __name__ == "__main__":
    mainObj = MetaImageCreator()
    mainObj.execute()
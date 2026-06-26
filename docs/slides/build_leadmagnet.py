# -*- coding: utf-8 -*-
"""リードマグネット（FP専用オープンチャット参加者へのウェルカム・プレゼント）pptx ビルド。
   紺×金エンジン `_build_slides.py` を再利用。Day1-3 とは独立。
   データ＝ `_leadmagnet_data.py` の DECK。"""
import _build_slides as eng
from _leadmagnet_data import DECK

# このデッキ用にラベル/フッターを差し替え（day=0 を間借り）
eng.DAY_LABEL[0] = "FP法人開拓"
eng.DAY_DATE[0] = "FP専用オープンチャット 参加者限定"
eng.FOOTER_BRAND = ""   # フッターのブランド表記は出さない（大吉塾／マスターコースを削除）

if __name__ == "__main__":
    eng.build_day(
        0, DECK,
        "リードマグネット_FPが仕事を取れない理由.pptx",
        "FPが法人で“仕事を取れない”理由 ― 取れる人は、何が違うのか",
    )

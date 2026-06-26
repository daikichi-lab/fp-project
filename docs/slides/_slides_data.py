# -*- coding: utf-8 -*-
"""スライドデータ（未来会計版・完全版／2026/6/23）。
   Day別に分割した `_day1_data` / `_day2_data` / `_day3_data` を集約して
   `_build_slides.py` へ DAY1 / DAY2 / DAY3 を供給する。
   投影文字＝全角引用符“ ”。notes＝読み上げ台詞。対応台本：docs/04_台本_Day1〜3.md。"""

from _day1_data import DAY1
from _day2_data import DAY2
from _day3_data import DAY3

__all__ = ["DAY1", "DAY2", "DAY3"]

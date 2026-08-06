# docs/ — deck の素材と作り方

このリポジトリで**スライド（.pptx）を作るときのフロー**をまとめる。`docs/` は
**中身（原稿・素材）だけ**を置く場所で、色やレイアウトは持たない。見た目は
`theme.json`、生成物は `outputs/` が受け持つ。

> このリポジトリは業務・マーケ設計ドキュメントが本体（`00`〜`08`）。ここで言う
> 「deck」は、その設計から起こすセミナー登壇スライドや特典 pptx（例：`outputs/Day1_セミナースライド.pptx`）
> を指す。

## パイプライン（4スキル・この順で流す）

```
theme-init  →  deck-strategy  →  create-deck  →  deck-review
 (見た目)       (構成)            (生成)          (採点)
```

| 手順 | スキル | 読むもの | 作るもの | 置き場所 |
|---|---|---|---|---|
| 1 | `theme-init` | ロゴ／ブランド素材・neutral default | ブランド配色・フォント・サイズ | **`theme.json`** |
| 2 | `deck-strategy` | `docs/` の原稿 | 検証済みの並び順つきパターン一覧 | **`deck_plan.json`** |
| 3 | `create-deck` | deck plan + `theme.json` | レンダリング済み deck（QAループを回す） | **`outputs/<name>.pptx`** |
| 4 | `deck-review` | 生成 deck + QA画像 | ハウス基準に対する採点レポート | （レビュー結果） |

## 置き場所のルール

- **`docs/` は中身だけ** — 原稿・メモ・文字起こし。色もレイアウトも書かない。
  （`deck-strategy` がこれを plan に変換する。plan の形＝`deck_plan.schema.json`）
- **`theme.json` は見た目だけ** — 配色・フォント・サイズ・キャンバス、多くても
  `brand.footerLabel` まで。章立てやスライド順は入れない。
- **`outputs/` は生成物** — `.pptx` と QA レンダー。`docs/` + plan + `theme.json`
  からいつでも作り直せる派生物として扱う。
- **deck plan（`deck_plan.json`）** は `deck-strategy` の出力かつ `create-deck` の入力。
  元にした原稿の隣に置き（例：`docs/<deck>/deck_plan.json`）、原稿と plan を一緒にしておく。
- `create-deck` では**必須のQAループ**（描画→目視→修正→再描画）が回る。レイアウト崩れが
  きれいに直せないときは、妥協したスライドを出さず**止めて報告**する。

## 1つの deck を作るときの最小構成

```
docs/
├── _manuscript-template.md   # コピー元の空原稿
└── <deck>/                   # deck ごとに1フォルダ
    ├── manuscript.md         #   人が書く原稿（deck-strategy の入力）
    └── deck_plan.json        #   deck-strategy の出力 → create-deck の入力
```

小さい deck なら `docs/<deck>/` を作らず、原稿を既存の設計ドキュメント
（例：`04_台本_Day1.md`）そのままにして plan だけ `outputs/` 隣に置く運用でもよい。
生成 pptx は必ず `outputs/<name>.pptx` に出す。

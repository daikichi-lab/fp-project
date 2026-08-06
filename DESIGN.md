---
version: 1.1
name: daikichi-juku-deck-design
description: 大吉会計株式会社（教育ブランド「大吉塾」）のデッキデザインシステム。純白の紙面に濃紺（#1B2A4A）のダーク面と鋼青（#1F4E79）のアクセント——金融・士業の「堅実」を正面から着る palette-navy 系。見出しも本文もゴシック（游ゴシック）のウェイト主導で、格や差別化は色ではなく〈具体数字のデカさ・1枚1メッセージ・正直さルール〉が作る。声は藤山泰成の「標準語の丁寧語×熱量」——難しい会計を身近なたとえと具体数字で噛み砕く"社長の相談役"のポジションを、端正な紺の紙面が信頼側から支える。
source: パレット＝プラグイン較正済みプリセット palette-navy（2026-07-08 theme-init Step 0 で人間が明示選択）。ロゴ実色から起こしたオリジナル案（大吉深紅×クリーム）は theme.json.crimson.example に退避
theme: ./theme.json（name "palette-navy"）

colors:
  # --- 紙・地 ---
  bg: "#FFFFFF"              # 純白。全本文スライドの床
  surface: "#F2F5F8"         # ニュートラルカード（青みの薄灰）
  surface-accent: "#E9EFF6"  # 強調カード（鋼青のティント）
  line: "#D8DEE6"            # 罫線・ヘアライン
  # --- インク（テキスト） ---
  ink: "#232E42"             # 見出し・本文（紺系の墨）
  muted: "#5D6A7E"           # 補足・サブテキスト
  faint: "#93A0B2"           # キャプション・フッター
  # --- 紺（ダーク面） ---
  dark: "#1B2A4A"            # 表紙・CTA・章扉・ダークmessageの床（濃紺）
  dark-alt: "#24365E"        # dark の持ち上げ。表紙/CTAの円弧モチーフ
  on-dark: "#FFFFFF"         # ダーク面上のテキスト
  on-dark-muted: "#AEB9CE"   # ダーク面上のサブテキスト
  # --- 鋼青（唯一のアクセント） ---
  accent: "#1F4E79"          # 鋼青。1面1箇所
  accent-deep: "#16395A"     # ティント面上のラベル・テキスト用の濃青
  accent-soft: "#7FA3C8"     # ダーク面上のキッカードット等、青のソフト版
  accent-on-dark: "#9CC3E8"  # ダーク面上で青を立たせる明青
  on-accent-muted: "#E8F0F8" # 鋼青ベタ面上のサブテキスト
  # --- 警告（用途限定の暖色） ---
  warn: "#C7431D"            # マイナス・注意・リスク**専用**。装飾に使わない
  warn-on-dark: "#E8603A"    # ダーク面上の同上
  # --- ブランド限定色（スライドの塗り・文字には使わない） ---
  brand-crimson: "#8B1E1E"   # ロゴ梅紋の朱。ロゴ資産内のみ
  brand-sumi: "#2A221D"      # ロゴワードマークの墨。ロゴ資産内のみ
  brand-gold: "#C2A15B"      # 公式サイト装飾の金。Web面のみ

typography:
  cover:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 44pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  cover-sub:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 17pt
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  section-title:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 36pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  section-index:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 150pt
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  title:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 30pt
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0
  message:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 32pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  stat-display:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 64pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  stat-card:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 40pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  compare-label:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 23pt
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  offer-head:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 21pt
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  takeaway-head:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 19pt
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  head:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 19pt
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  num:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 17pt
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 15pt
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  small:
    fontFamily: "Yu Gothic Medium, sans-serif"
    fontSize: 13.5pt
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  footer:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 12.5pt
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  kicker:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 12pt
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Yu Gothic, sans-serif"
    fontSize: 12pt
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

spacing:
  canvas: "13.333 × 7.5 in（16:9）"
  margin: "0.75 in"
  lead-title: 1.08
  lead-display: 1.18
  lead-body: 1.6
  lead-caption: 1.5
  lead-tight: 1.4

radius-elevation:
  card: "エンジン既定（プリセットに layout オーバーライドなし）"
  kicker: "dot（アクセント色のドット＋小ラベル）"
  cover-motif: "darkAlt の柔らかい円弧（オフキャンバスの楕円）が表紙/CTAの深度"
  section-style: "chapter（「CHAPTER N」キッカー＋中央タイトル。巨大透かし数字はセミナー系レジスターで AI-tell のため不使用 — house bar §3・2026-07-09）"
---

# DESIGN.md — 大吉塾（大吉会計株式会社）deck design system

## Overview

大吉塾のデッキは、**16:9（13.333×7.5in）・純白の紙面に、濃紺（`{colors.dark}` #1B2A4A）のダーク面と鋼青（`{colors.accent}` #1F4E79）のアクセントが規律を作る palette-navy 系**である。パレットは 2026-07-08 の theme-init Step 0 で**人間が5択から明示選択**した較正済みプリセット——以後の全ビルドがこの `theme.json` を読む（決定論）。

視覚の性格は**金融・士業の「堅実」を正面から着る**こと。保険営業・FP に「法人・経営者の世界の資料はこう見える」という格をそのまま体験させる。差別化・熱量は色ではなく、**具体数字のデカさ（stat 64pt）・1枚1メッセージ・正直さルール（§4）**、そしてライブの藤山ボイスが担う——紙面は信頼側、語りは熱量側、という分業。

タイポグラフィは**游ゴシックのウェイト主導**（見出し＝太字、本文＝Medium）。表紙と CTA には `{colors.dark-alt}` の柔らかい円弧モチーフが深度を作り、キッカーはアクセント色のドット。ペーシングは**紺のダーク面（表紙・章扉・決め台詞・CTA）と白地の本文の交代**で刻む。

## Colors

### Brand & Accent

- **鋼青 / Accent**（`{colors.accent}` — #1F4E79）：唯一のアクセント。使う場所＝キッカーのドット、強調したい数字1つ、強調カードの文脈、CTA・オファーパネル。**使わない場所**＝ストライプ・帯・背景の面塗り（アクセントはドット/キッカー/ティントのみ、house bar）、本文の文字色、2箇所目以降の強調。**1面に主役1箇所**。
- **Accent Deep**（`{colors.accent-deep}` — #16395A）：ティント面（`{colors.surface-accent}`）上のラベル・見出し用の濃青。
- **Accent Soft**（`{colors.accent-soft}` — #7FA3C8）／**Accent On Dark**（`{colors.accent-on-dark}` — #9CC3E8）：ダーク面上でアクセントを名乗るための明度版（キッカードット・強調語）。白地の上では薄すぎるので使わない。
- **On Accent Muted**（`{colors.on-accent-muted}` — #E8F0F8）：鋼青ベタ（CTAパネル）上のサブテキスト。
- **警告 / Warn**（`{colors.warn}` — #C7431D／ダーク面上は `{colors.warn-on-dark}` — #E8603A）：**マイナス・注意・リスク専用の暖色**（▲の数字、締切、「ここでつまずく」）。装飾・強調の2色目として使った瞬間に2アクセント違反になる——用途外使用禁止。
- **ロゴ限定色**：梅紋の朱 `{colors.brand-crimson}` #8B1E1E・ワードマークの墨 `{colors.brand-sumi}` #2A221D・サイトの金 `{colors.brand-gold}` #C2A15B は**ロゴ資産・Web 面の中にのみ存在を許す**。スライドの塗り・文字に持ち込むと紺×鋼青の二家族規律が壊れる。

### Surface

- **Canvas**（`{colors.bg}` — #FFFFFF）：本文スライドの床。純白——このテーマの「端正」の土台。クリームや灰に濁さない。
- **Surface**（`{colors.surface}` — #F2F5F8）：ニュートラルカード（card-grid・two-column の面、表のヘッダ行）。
- **Surface Accent**（`{colors.surface-accent}` — #E9EFF6）：**強調カード専用**の鋼青ティント。1面に1枚まで。ラベルは `{colors.accent-deep}` で置く。
- **Line**（`{colors.line}` — #D8DEE6）：罫線・ヘアライン。Zoom 圧縮で消えることがある前提で、罫線だけに構造を託さない。

### Text（インクの階調）

- **Ink**（`{colors.ink}` — #232E42）：見出し・本文。紺系の墨——純黒 #000000 は使わない。
- **Muted**（`{colors.muted}` — #5D6A7E）：サブテキスト・補足。
- **Faint**（`{colors.faint}` — #93A0B2）：キャプション・フッター・出典行。本文には使わない（コントラスト不足）。

### Dark（紺のダーク面）

- **Dark**（`{colors.dark}` — #1B2A4A）：**表紙（cover）・CTA・章扉（section）・ダーク message の床**（cover/CTA がダークなのはエンジンのトークン設計。プレビュー確認済 2026-07-08）。
- **Dark Alt**（`{colors.dark-alt}` — #24365E）：dark の持ち上げ。表紙/CTA の**柔らかいオフキャンバス円弧モチーフ**の色。帯・ストライプには使わない。
- **On Dark**（`{colors.on-dark}` — #FFFFFF）／**On Dark Muted**（`{colors.on-dark-muted}` — #AEB9CE）：ダーク面上の主・副テキスト。

## Typography

### フォントファミリー

**全デッキ游ゴシック一族**：見出し＝Yu Gothic（太字）／本文＝Yu Gothic Medium／キャプション＝Yu Gothic。serif は使わない——このテーマの格は**ウェイトとサイズの規律**で出す。

**実機にない場合の代替**：**Noto Sans JP** または **Meiryo**（いずれもビルド互換）。ビルドマシン（WSL2）には Yu Gothic 登録済み（`~/.local/share/fonts/`）。

### ヒエラルキー

| ロール | サイズ | ウェイト | 行間 | 用途 |
|---|---|---|---|---|
| `stat-display` | 64pt | 太字 | 1.18 | 巨大数字（message の statBig） |
| `cover` | 44pt | 太字 | 1.18 | 表紙タイトル（セミナー名） |
| `stat-card` | 40pt | 太字 | 1.18 | stat-grid のカード数字 |
| `section-title` | 36pt | 太字 | 1.18 | 章扉タイトル（＋150pt の章番号） |
| `message` | 32pt | 太字 | 1.18 | 1枚1メッセージの主文 |
| `title` | 30pt | 太字 | 1.08 | 本文ページの見出し |
| `compare-label` | 23pt | 太字 | 1.18 | 比較の左右ラベル |
| `offer-head` | 21pt | Medium | 1.4 | CTA のオファー見出し |
| `head`／`takeaway-head` | 19pt | Medium | 1.4 | カード・列の小見出し／まとめ |
| `cover-sub` | 17pt | Medium | 1.4 | 表紙サブタイトル |
| `num` | 17pt | Medium | 1.4 | 番号・小さめ数字 |
| `body` | 15pt | Medium | 1.6 | 本文。**これ未満に落とさない** |
| `small` | 13.5pt | Medium | 1.5 | 補足 |
| `footer` | 12.5pt | Regular | 1.4 | フッター（大吉塾） |
| `kicker`／`caption` | 12pt | Regular | 1.4–1.5 | キッカー・出典・注記 |

### 原則

- **ウェイト主導**：強調は 見出し太字 → サイズ → 強調カード の順で。色での強調はアクセント1箇所の枠内でだけ。
- **和文にレタースペーシングは入れない**（letterSpacing 0）。禁則（kinsoku）と行長はエンジンの floor（Phase A/B）が守る——手で改行位置を細工しない。
- 本文 15pt・行間 1.6 は Zoom 画面共有＋スマホ視聴を想定した下限。密度を上げたくなったら枚数を割る（1枚1メッセージ）。
- 数字は本文に埋めず `stat-display`／`stat-card` に引き上げる。「具体の金額に落とす」藤山メソッドの視覚版＝**数字がいちばん大きい紙面**。

## Layout

- **キャンバス**：13.333 × 7.5 in（16:9）、マージン **0.75in**（Zoom の画面端・録画のセーフエリア兼用）。
- **行間**：title 1.08 / display 1.18 / body 1.6 / caption 1.5 / tight 1.4（`theme.lead`）。
- **余白哲学**：余白は「省略」ではなく「相談役の間（ま）」。語りはライブの藤山ボイスが担うので、紙面は**1枚1メッセージ＋支える具体1つ**（数字・比較・たとえ）まで。詰め込んだ瞬間に"研修資料"へ退化する。
- 密度を上げてよいのは配布前提の特典 PDF と社内レビューのみ（§3 プリセット）。

## Elevation & Depth / Shapes

- **深度は面の色差**（bg → surface → surface-accent → dark）で作る。影は使わない/最小限（エンジン既定に従う）。
- **キッカーは dot**：アクセント色のドット＋小ラベル。ドットがアクセントの定位置。
- **表紙・CTA の深度モチーフ＝ `{colors.dark-alt}` の柔らかいオフキャンバス円弧**（エンジンが描く。プレビュー確認済）。帯・ストライプは何色でも禁止。
- **章扉は chapter スタイル**（`theme.layout.sectionStyle: "chapter"`＝「CHAPTER N」キッカー＋中央タイトル）。巨大透かし数字はセミナー・ストーリー系レジスターで AI-tell と判定されるため使わない（house bar §3・2026-07-09 反映）。
- **ロゴの扱い**：コーポレートロゴ「大𠮷」（墨のワードマーク＋朱の梅紋）は**濃紺の表紙に沈む**（墨×紺のコントラスト不足）。**白抜き版ロゴが入手できるまで、スライドにはロゴを置かずテキスト（フッター「大吉塾」・表紙 footer 行）で示す**（→ Known Gaps）。梅紋を単独装飾として散らさない。
- グラデーション・パターン柄・絵文字装飾は使わない（AI-tell。house bar §2 のブロックリスト準拠）。

## Components（deck surface）

- **cover（表紙）**：濃紺のダーク面＋dark-alt の円弧モチーフ。白の太字タイトル 44pt、キッカーにイベント名/日付（accent-soft のドット＋ラベル）、footer 行に「大吉塾｜大吉会計株式会社」。プレビュー確認済（2026-07-08）。
- **section（章扉）**：濃紺面・chapter スタイル（「CHAPTER N」キッカー＋中央タイトル 36pt、透かし数字なし）。Day 内の「ここから話が変わる」合図。1デッキ 2〜4 枚まで。
- **message（1枚1メッセージ）**：主文 32pt 太字＋巨大数字（64pt・鋼青）＋根拠キャプション。**dark: true 形＝感情を刻む決め台詞のページ**（例：「保険は、結果としてあとからついてくる」）。本文中の dark 形は 1 Day に 1〜2 枚——乱発すると締めの効力が消える。
- **two-column**：概念の対置（個人マーケット/法人マーケット等）。列見出しは `head` 19pt。
- **comparison**：Before/After・A/B の正式対決（compare-label 23pt）。価格プラン A/B の対比は Day3・個別相談のみ（§5）。
- **chart**：単位は常に明示（unit）。**強調は1本だけ**（emphasizeIndex）。時系列・連続量は line。目標・前年は targetLine の参照線。**マイナス・悪化は ▲＋`{colors.warn}`**。系列色は鋼青1本＋インク階調——虹色にしない。
- **table**：決算書・比較表は**教材用に簡略化**して載せ、見るべき1セルだけ強調（surface-accent ティント）。実物の決算書の網羅転載はしない（「読める気がする」体験が目的。Day2 教材の核心）。
- **stat-grid**：KPI・実績のカード列。強調カードは1枚（emphasizeIndex）。各カードに比較の文脈（前年比・業界平均）を `sub` で併記。
- **card-grid**：3案・3類型（ペルソナ A/B/C 等）の並置。3-up が基本形。
- **before-after**（education register）：受講前→受講後、2019年税制改正の前→後などの転換の型。
- **dialogue／testimonial**：社長との会話再現・受講者の声。**人物図版は当面使わずテキスト運用**（figures 資産未整備 → Known Gaps)。実在顧客名は載せない（§4）。
- **cta（クロージング）**：鋼青／濃紺のオファーパネル。価格・期限付き特典・申込導線。**Day3 と個別相談資料にのみ出現**（§5）。デッキ内でアクセントの面積が最大になる唯一の場所＝「ここが決めどころ」の視覚合図。
- **footer**：全本文ページ左下に「大吉塾」（`brand.footerLabel`）＋ページ番号。faint 色 12.5pt で控えめに。

## 1. 誰に・どんな声で

- **発信者**：大吉会計株式会社（daikichi-accg.co.jp）／教育ブランド「**大吉塾**」。登壇者＝**藤山泰成**。
- **主要オーディエンス**：
  1. **3日間チャレンジセミナー参加者**（Zoom・20:00〜21:00）＝法人開拓に悩む保険営業・FP（30〜50代・実務3年以上、`01_ターゲット設計` の A/B/C 類型）
  2. **特典（プレゼント）受領者**＝同上。公式LINE・FBグループで配布される PDF/pptx
  3. **バックエンド講座受講生**（大吉塾 マスターコース・伴走支援）
  4. **経営者**（個別相談・共同募集の同席場面。売上2〜20億の中小経営者）
  5. **社内・定例**（大吉会計内のレビュー・企画資料）
- **声・トーン**：`docs/style/fujiyama-voice-guide.md` に従う——**標準語の丁寧語をベースに、具体数字・身近なたとえ・前向きさで熱量を出す**。スライド上の文字は台本より一段締める（結論先出し・体言止め可）。**関西弁・自虐は生成物に載せない**（経営者方針）。「また聞きたいと思っていただけたら」等、**尊敬・評価を自分から宣言する文言は書かない**——それは聴衆の行動が示すもの。

## 2. デザイン言語とブランド

- **採用パレット**：**紺（palette-navy）** — 2026-07-08 theme-init Step 0 で**人間が5択から明示選択**（理由＝金融・士業の堅実路線。プリセットは CONTRAST lint〔4.5:1 契約〕較正済み＝決定論）。
  - 不採用案の記録：ロゴ・公式サイトから実抽出したオリジナル案（大吉深紅 #8B1E1E×クリーム #FAF7F0×游明朝、editorial 言語）は **`theme.json.crimson.example` に退避**。ブランド実色路線へ戻す場合はこのファイルを theme.json に戻し、本書 v1.0（git 履歴）を参照。
- **構図・型**：neutral-business 系（プリセットの既定ジオメトリ）。円弧モチーフ・dot キッカー・章番号数字。
- **ブランド色**：ロゴの墨 #2A221D・朱 #8B1E1E・金 #C2A15B は**ロゴ資産・Web 面限定**。スライドの塗り・文字には使わない（§Colors）。
- **フォント**：游ゴシック一族（見出し太字／本文 Medium）。
- **theme.json**：**`./theme.json`**（リポジトリ直下、name = "palette-navy"）。本ドキュメントの frontmatter と同値を機械可読で持つ。ズレたら §Iteration Guide の手順で同時更新。

## 3. オーディエンス別プリセット

> テーマは全デッキ共通で `./theme.json`（palette-navy・Step 0 で固定）。プリセットで変えるのは**トーン・密度・目標 band・語りの枠・intent**。

| オーディエンス | トーン（レジスター） | 目標band | 密度 | 既定frame | meta.intent | meta.personStyle |
|---|---|---|---|---|---|---|
| 3日間チャレンジ登壇（Zoom） | 熱量（藤山B・締めは一瞬A） | external(≥90) | 低（1枚1メッセージ） | Day1 WHY → Day2 HOW → Day3 GAP | セミナー（説得） | なし（テキスト運用） |
| 特典・プレゼント資料（配布PDF/pptx） | 実務・教育（藤山B寄り） | external(≥90)※手元に残る配布物 | 中 | PREP | education | なし |
| バックエンド講座教材 | 教育・伴走 | internal(80+)以上 | 中 | 手順型（たとえ→用語の順） | education | なし |
| 経営者向け（個別相談・共同募集同席） | 端正（藤山A） | external(≥90) | 低〜中 | PREP | financial | なし |
| 社内・定例レビュー | 実務 | internal(80+) | 高 | PREP | report | なし |

- 会計の教え方はプロジェクト共通ルール：**たとえ→用語の後出し**（例：「画用紙の仕入れ」→「売上原価」）。スライドでも用語を先に出さない。
- 人物図版（persona/dialogue/testimonial 用イラスト）は資産未整備のため全プリセット「なし」。導入する際は `assets/generated/figures/` を整備し（figures-index.md＋LICENSE.md 必須）、本表を更新する。

## 4. コンテンツ整合の house rules（常設の正直さ）

- **仮ラベルの維持**：KPI 目標・人数・伴走支援 300万の成果保証/分配率/役割分担は「**仮**」ラベル付きの数字。スライドに載せるときも（仮）を落とさない。確定済み＝セミナー名／プランA 30万。
- **税・法の数字は正確に**：出典＝`docs/research/知識ドメイン_リサーチ.md`（特例承継計画 2027/9/30・適用 2027/12/31、純資産価額方式の控除 38%〔2026/4〜〕、法人保険 2019年通達4区分、相続の基礎控除・非課税枠 等）。**施行日・年度を数字に併記**する。リサーチと引用側は同時更新。
- **コンプラ定型文**（税・保険に触れる配布物の末尾に必ず）：「※本資料は一般的な情報提供を目的としたものであり、個別の税務判断・保険提案を行うものではありません。具体的な税務は税理士等の専門家にご相談ください。」（税理士法・保険業法＝情報提供にとどめる）
- **出典のない数値の創作禁止**：実数 or **〔要確認〕**プレースホルダ。市場データは `docs/research/` の確度〔高/中〕表記に従い、断定は〔高〕のみ。
- **実在顧客名・第三者の固有名・個別案件は載せない**（事例は一般化する）。
- **社内集計値には「社内集計」「概算」ラベル**を付ける（受講生実績・成約率など）。
- **保険を「売り込む/決まる」と書かない**：3日間の一貫ポジション＝保険は"結果としてあとからついてくる"。
- 他社・競合への言及は公式ソースの裏取りが済んだものだけ。士業への問題提起は「中小を守りたいから」の文脈とセットで書く（悪口にしない）。

## 5. 制約・禁止

- **標準枚数（仮）**：セミナー1Day（60分）＝20〜30枚／特典資料＝8〜14枚／経営者向け＝8〜12枚。超過しそうなら枚数でなく内容を割る。
- **価格は Day1・Day2 の資料に載せない**。価格・オファーの提示は Day3 の cta と個別相談資料のみ。
- **割引・二重価格表現の禁止**（「今だけ◯円→◯円」等）。動機づけは**期限付き特典**で行う。分割は"回数相談"であり金額は下げない。
- **禁止表現**：断定的な成果保証の煽り（「必ず契約が取れる」「絶対儲かる」——保険業法・景表法リスク）／自虐／関西弁・方言／実在キャラ・他社IP／絵文字の装飾使用。
- **フッター brand**："大吉塾"（`theme.json` の `brand.footerLabel`。経営者向け・社内資料は plan の `meta.footerLabel` で「大吉会計株式会社」に差し替え可）。
- **出力先**：生成 pptx は `outputs/<name>.pptx`、QA レンダーは `outputs/qa/`（複数 deck が並ぶ場合は `outputs/<name>.qa/`）。deck_plan は原稿の隣（`docs/<deck>/deck_plan.json`）。

## 6. 検証バー（既定）

- **既定パイプライン**：bake → generate → design-lint → typo-lint → image-lint → **QAループ（描画→目視→修正→再描画）** → deck-review。
- **目標 band**：対外（セミナー登壇・特典配布・経営者向け）＝**external(≥90)**／社内＝**internal(80+)** 以上。
- レイアウト崩れがきれいに直せない場合は、**妥協したスライドを出さず止めて報告**（M-4）。
- 税・法数値を含むデッキは、deck-review と別に **§4 の出典照合**（知識ドメイン_リサーチとの突き合わせ）を1回行う。

## 7. 視覚・図解の方針（standing visual conventions）

- **チャート**：単位は常に明示（unit）。強調は1本だけ（emphasizeIndex）。連続量は line。前年・目標は targetLine。**マイナス・悪化は ▲＋warn 色**（warn はここと注意書きにしか使わない）。系列色は鋼青1本＋インク階調。
- **図解は保守的＝既定はテキスト**。構造が1語で言えるときだけ図にする。**この案件の概念→骨格の対応は `docs/canon/accounting-fp-insurance.md`（正準形カタログ）が単一ソース**——BS＝identity、STRAC＝identity+sub、利益→現金＝waterfall、循環モデル＝cycle、バリューラダー＝steps、期限＝timeline 等。カタログに無い概念は迷ったらテキスト。座標文法：**「残り（純資産・自由なお金・利益）が常に主役」**をデッキ横断で維持する。
- **アイコン・モチーフ**：アイコンは使わない基調（数字とタイポで語る）。深度モチーフはエンジンの円弧のみ。ロゴは白抜き版入手まで置かない（§Elevation）。
- **構図**：プリセット既定の `theme.layout`（円弧モチーフ・dot キッカー・章番号数字）に従う。

## Do's and Don'ts

### Do

- **純白の床と紺の規律を保つ。** このテーマの価値は「経営者・金融機関の世界の資料に見える」端正さ。色数を増やした瞬間に崩れる。
- **鋼青 #1F4E79 は1面に主役1箇所。** キッカーのドットか、数字1つか、強調カード1枚か——どれか。Day3 の cta で初めてアクセントの面積を最大化する＝クロージングの視覚設計。
- **強調はウェイト→サイズ→強調カードの順で。** 游ゴシックの太字が見出しの声。色に頼る前に太さと大きさで語る。
- **数字を紙面で一番大きくする（stat 64pt）。** 「具体の金額に落とす」が藤山メソッドの核。曖昧な図解より、大きな実数1つ＋出典。
- **1枚1メッセージ、本文15pt以上。** 聴衆は Zoom（しばしばスマホ）。詰めた分だけ届かない。熱量は語り（ライブ）が担う。
- **本文中のダーク面は「感情を刻むページ」だけに絞る。** 表紙・CTA・章扉の紺はエンジンが置く固定の句読点。それに加えて dark: true にしてよいのは決め台詞の message 1 Day 1〜2枚まで——乱発すると「締め」が効かなくなる。
- **マイナス・リスクは ▲＋warn で正直に見せる。** 警告専用の暖色があるのは「悪い数字を隠さない」ため。良い数字と同じ青で塗って紛らわせない。
- **決算書・表は簡略化して強調1セル。** Day2 の目的は「読める気がする」体験。網羅した瞬間に挫折体験に変わる。
- **税・保険に触れる配布物には §4 のコンプラ定型文と出典年を必ず入れる。** 配布物は手元に残る＝リスクも残る。
- **たとえ→用語の順で組む。** スライドでも「画用紙のたとえ」が先、「売上原価」は後。用語が先に出ると Day1 で脱落が出る。

### Don'ts

- **ロゴの朱・墨・金をスライドの塗り・文字に持ち込まない。** 紺×鋼青の二家族規律が壊れ、暖色は warn と衝突して「どれが警告か」が消える。ロゴ色はロゴ資産の中でだけ品位を持つ。
- **warn #C7431D を装飾・強調の2色目に使わない。** マイナス・注意・リスク専用。締切の演出に多用すると煽りに転じ、本当の警告が効かなくなる。
- **アクセントをストライプ・帯・背景に広げない。** アクセントはドット/キッカー/ティントのみ（house bar）。面積が増えるほど端正さが死ぬ。
- **割引・二重価格を載せない。** 割引は情報商材化の入口（プロジェクト方針）。動機づけは期限付き特典で。
- **Day1・Day2 の資料に価格を出さない。** 価格は Day3 クロージングの設計要素。先出しは3日間のアーク（WHY→HOW→GAP）を壊す。
- **自虐・関西弁を書かない。** 経営者方針（2026-06）。失敗談は「学び・使命」として前向きに書く。
- **「必ず」「絶対」等の成果断定をしない。** 保険業法・景表法リスクであり、「保険は結果としてついてくる」ポジションとも矛盾する。
- **尊敬・評価を自分から宣言する文言を書かない**（「また聞きたいと思っていただけたら」等）。口に出させてよい目標は聴衆側の変化だけ。
- **虹色チャート・グラデーション・絵文字装飾を使わない。** AI-tell ブロックリスト該当。系列は鋼青1本＋インク階調で足りる。
- **見出しを Medium のまま大きくだけしない。** ウェイト主導のテーマで太字を外すと、ただの薄い研修資料になる。

## 出力面の挙動

| 出力面 | 何が劣化するか | 何を守るか |
|---|---|---|
| **Zoom 画面共有**（主戦場） | JPEG 圧縮で 1px 罫線（`line`）と bg↔surface の薄い差が潰れる | 構造を罫線だけに託さない。カードは面色差＋余白で分ける。本文15pt下限・数字はディスプレイサイズ |
| **スマホ視聴**（Zoom アプリ） | 12pt 級の注記は読めない。画面端が切れる | 1枚1メッセージ。キッカー・出典は「読めなくても本文が成立する」情報に限る。マージン 0.75in がセーフエリア |
| **PDF 配布**（特典） | 発表の間（ま）がない＝1枚ごとに自己完結が必要。リンクはクリックできない環境もある | 密度プリセット「中」。URL はテキスト併記。コンプラ定型文・出典を必ず紙面内に |
| **モノクロ印刷** | 鋼青 #1F4E79 とインク #232E42 の区別がほぼ消える。warn の赤も灰に落ちる | 強調は色＋**太字・サイズ・ラベル**の複線で。▲は記号として色なしでも意味が立つ |
| **低輝度プロジェクタ**（会場開催時） | bg と surface の差が消え、カード境界が消失。濃紺面は黒に沈む | 余白でグルーピングが読める配置に。ダーク面上は onDark の白と accent-on-dark を使う（accent-soft は沈む） |

## Iteration Guide

1. **トークンを変えるときは DESIGN.md（frontmatter）と `./theme.json` を同時に更新**する。片方だけの変更は禁止——ズレた瞬間にこの文書は死ぬ。
2. 更新後は必ず：`node <plugin>/bin/validate.js --theme theme.json` → **1枚プレビュー再生成**（cover＋body 1枚）→ 目視 → 影響が広ければ run-gate。
3. パレットの乗り換え（例：crimson 案へ戻す）は theme-init Step 0 のやり直し＝**人間の明示選択**を経ること。`theme.json.crimson.example` を theme.json へ戻し、本書の色・タイポ節を v1.0（git 履歴）から復元する。
4. 色変更はコントラスト契約を再確認（on-dark×dark／accent-deep×surface-accent／on-accent-muted×accent、本文系は 4.5:1）。プリセットのまま使う限り較正済み。
5. **修正履歴はこの文書が吸収する**：藤山さん・塩尻さんの「ここは違う」は、該当セクションの Do/Don't（理由つき）・§3 プリセット・§7 の構造マップに追記する。反映なしのレビュー指摘を残さない。
6. 意思決定として残すもの（価格・名称・方針）は `docs/06_意思決定ログ.md` へ、デザイン規範はここへ——置き場所を混ぜない。

## Known Gaps

- **ロゴの白抜き（反転）版の有無が未確認**。現行ロゴ（墨＋朱）は濃紺の表紙に沈むため、入手まで**スライドにロゴを置かない**運用（テキスト「大吉塾」のみ）。入手できたら cover/cta への配置ルールを §Elevation に追記する。
- **公式ブランドガイド未入手**。ロゴ実色（墨 #2A221D・朱 #8B1E1E・金 #C2A15B）は daikichi-accg.co.jp からの抽出値（2026-07-08）。パレット自体はプリセット採用のため影響は小さいが、ロゴ運用規定（クリアスペース・最小サイズ）は未定義。
- **不採用のブランド実色案**（大吉深紅×クリーム×游明朝・editorial）は `theme.json.crimson.example` と本書 v1.0（git 履歴）に保存。将来「ブランド色に寄せたい」となったら Step 0 をやり直す。
- **「大吉塾」ブランド単体のロゴ有無は未確認**。フッターはテキスト運用中。
- **人物図版（dialogue/testimonial/persona 用 figures）は未整備**。`assets/generated/figures/` も未作成。導入時に figures-index.md＋LICENSE.md とセットで整備し、§3 の personStyle を更新する。
- **経営者向けプリセットは未実戦**。初回の個別相談・共同募集デッキで較正する。
- note・LP・公式LINE 等の**スライド以外の面はこの文書の対象外**（Web は金・朱を含む別トーンが既に走っている）。
- アニメーション・画面切替（Zoom でのスライド送り演出）はスコープ外。

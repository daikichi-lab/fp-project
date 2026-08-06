# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project** — it is a **business / marketing design repository** for the **FP法人マーケット攻略プロジェクト**（「FP育成プロジェクト」／運営＝大吉会計株式会社・daikichi-accg.co.jp。※教育ブランド「大吉塾」の名称は**2026/7/14決定で非表示**＝生成物・対外物では使用しない）.

It houses Japanese Markdown design documents for a high-ticket education funnel that trains FP・保険営業 (financial planner / insurance sales) professionals to break into the corporate (法人) market — teaching 決算書 reading, 財務分析, 相続, 事業承継. **There is no build, lint, test, or run step.** Deliverables are the Markdown documents in `docs/`.

## The big picture (two layers — hold both before editing)

Edits go wrong when only the inner layer is considered.

**Layer 1 — the 入口 funnel** (most of `docs/`): 集客 → 無料3日間チャレンジセミナー（2026/7/14火・16木・18土 20:00〜21:00）→ 個別相談 → バックエンド. Pattern adapted from a note.com "challenge seminar" funnel (free multi-day seminar → 1:1 consult → high-ticket backend).

**Layer 2 — the 循環エンジン** (上位の事業構造; `docs/mtg/2026_06_21_FP循環モデル_まとめ.md`): FP育成 is only the *入口* of a loop — 育ったFPが**共同募集**で経営者を連れてくる → 高収益の本業（管理会計・外部CFO・相続・事業承継・M&A・上場支援・不動産）が自動流入 → 成果と評判が次のFPを呼ぶ。最終顧客＝**売上2〜20億の経営者**（上場志向／M&A／実務成長の3類型）。FPは収益の終点ではなく起点。

### Backend = two support models (二つの支援モデル) ★2026/7/14 公開LPで確定
**本講座の正＝公開LP**（https://hokenlp-av8vhogh.manus.space/ ・サイト名「法人保険提案実践アカデミー」）。リポジトリ内リファレンス＝`08_本講座_内容まとめ.md`／講座のみプラン詳細＝`08_本講座_講座のみプラン_33万.md`。
- **プランA：経営者から選ばれるFP養成講座（3か月集中実践コース）・講座のみ** — **33万税込**・3ヶ月・全6回＋フォロー（"学ぶ"／基礎を固め初商談〜初契約まで自走。カリキュラム＝オリエン→MG体験→財務分析→相続→事業承継→ブランディング。第1期 2026/8/5〜10/28・定員10名）。
- **プランB：伴走コンサルティング付・成果保証あり** — **198万税込**・1年・限定5名（"成果まで伴走"／Aを内包、商談同行無制限、成果保証＝手数料累計180万まで無期限。共同募集・本業連携まで）。**Aは最上位の本命ではなくBへの一段**。
- 別導線：MG（マネジメントゲーム）体験会 2万 → 友の会 月1万。
- バックエンドの**概念軸**＝「会計を武器に、FPが法人で保険を売れるようになる」（`02`/`08`）。会計は目的でなく手法。

### Front seminar = the 相談役 spine
セミナー名（2026/6/22 確定）「**保険営業から、社長の"相談役"へ ― 会計を武器に法人を開く3日間チャレンジ**」。3日間は「相談役のポジションを取る」アーク＝**Day1 WHY（取れたら何が変わる）→ Day2 HOW（取り方＝見て・聞いて・提案）→ Day3 GAP（必要な力と独学の壁 → 講座へ）**。保険は終始「結果として後からついてくるもの」扱い（"売り込む／決まる"を前面に出さない）。

## Document structure (`docs/`)

Numbered to read as a sequence. **Design docs (00–08) are the spec**; several have **付属／production artifacts** derived from them — change a number in the spec and you must propagate it to the artifact.

> **現状（2026-06-26）**: セミナー導線 `03` / `04` / `05` / `07`（＋それらの旧 artifacts・`docs/slides/`・`docs/sample/`）は、3日間チャレンジを「チャレンジ／プロダクトローンチの型」で作り直すため**いったん全削除**した（git 復元点＝コミット `75723a9`）。**現在 `docs/` 直下に実在するのは `00`/`01`/`02`/`06`/`08`(大枠・6回プラン案) のみ。** 下表は**再構築のターゲット構造**として残す。型の土台＝`docs/research/チャレンジ・プロダクトローンチ_リサーチ.md`、決定経緯＝`docs/mtg/大吉会計定例_まとめ.md`。

| Spec | 付属・production artifacts derived from it |
|---|---|
| `00_全体設計`（value ladder・funnel・KPI） | — |
| `01_ターゲット設計`（persona・pains・messaging） | — |
| `02_商品設計`（front + backend A/B・pricing・offer） | — |
| `03_集客設計`（channels・6段階ティザー） | — |
| `04_チャレンジセミナー設計`（3日間 curriculum・運営ルール） | `04_3日間カリキュラム詳細案`, `04_セミナータイトル・特典カタログ案`, `04_台本_Day1〜3`, `04_サンプル決算書_Day2`, `04_運営マニュアル_当日進行` |
| `05_個別相談・クロージング設計`（closing・A/B提示導線・objection handling） | — |
| `06_意思決定ログ`（decisions of record） | — |
| `07_プレゼント（特典）設計`（bonus strategy・3カテゴリ） | `07_特典コンテンツ集`（そのまま配布できる実コンテンツ／A着席・B参加理由・C無条件・D完走・E相談役スタック・S分割） |
| `08_バックエンド大枠`（3×2日集中案） | `08_バックエンド_6回プラン案`（6回ハイブリッド案。形態は T2 で未決） |

Supporting: `docs/research/`（cited research — 2026 tax facts, competitor/market, 藤山ストーリー, 経営者の保険屋イメージ・断り文句, **チャレンジ／プロダクトローンチの型**）、`docs/mtg/`（meeting `.txt`/`.docx` ＋ それぞれの `*_まとめ.md`）、`docs/style/fujiyama-voice-guide.md`（登壇者＝藤山泰成の口調）.

Logical design order: **02 → 01 → 03 → 04 → 05**, bound by `00`.

## Conventions when editing

- Write in **Japanese**; match the existing tone (concrete, actionable, table/checklist-driven). Every doc ends with a "このドキュメントの使い方" cross-linking block — keep it.
- **Keep the funnel internally consistent.** Live dependencies: 01 pains → 03 messaging; 04 seminar previews 02's backend; 05 proposes 02's exact plans/prices; 07 gifts bridge 3日間→backend; 00 value ladder = 02's tiers. Changing one number/claim means updating its references in the others.
- **Decisions are recorded in `06_意思決定ログ.md` with a date.** When a new meeting file lands in `docs/mtg/`, summarize the transcript/`.docx` into a sibling `*_まとめ.md` (see `事業モデル説明_動画まとめ`, `2026_06_21_FP循環モデル_まとめ` for the format), then propagate into the affected docs and log the decision in `06`.
- **`仮` labelling**: KPI targets, prices, headcount, names are placeholders marked **仮** — preserve until the user confirms. (Currently: セミナー名＝確定／A=33万税込・B=198万税込・成果保証180万・定員10名/5名・第1期日程＝**確定（2026/7/14 LP）**／共同募集の分配率・役割分担＝仮。)
- **Tax/legal numbers are NOT 仮 — they must be accurate.** Source of truth = `docs/research/知識ドメイン_リサーチ.md`（特例承継計画 2027/9/30・適用 2027/12/31、純資産価額方式の控除 38%〔2026/4〜〕、法人保険 2019年通達4区分、相続 基礎控除・非課税枠 等）. Every gift/script citing tax must match it and carry the コンプラ注意書き（税理士法・保険業法＝情報提供にとどめる）. Update research and the citing doc together.
- **台本 follow `docs/style/fujiyama-voice-guide.md`**: 地は**標準語の丁寧語**、熱量は具体数字・身近なたとえ・前向きさ・オノマトペで出す（**関西弁・方言は生成テキストでは使わない**／2026-06-24 経営者方針。本人ライブの関西弁は別＝止めない）。**自虐は生成テキストに入れない**（失敗は「学び・使命」として前向きに）。価格は Day1-2 で出さず、Day3 クロージングで提示。
- **割引はしない**（情報商材化を避ける）。動機づけは**期限付き特典**で。分割は"回数相談"（金額は下げない）。

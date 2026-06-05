# LP制作プロジェクト（Phase 5）

FAST-UP逆転塾の新Google広告アカウント運用に向けた、14広告グループ別LPの制作。

## 制作方針（確定）

- **対象媒体**：Google広告（新アカウント運用）のみ
- **デザイン**：既存LP（`fast-up.jp/lp/`）を完全踏襲（カラー・フォント・CTAスタイル）
- **設計原則**：「自分ゴト感最大化」×「既存の強み」×「競合の良い部分」でCVR最強を狙う
- **実装**：静的HTML + バニラJS（Next.js等の動的言語は使わない）
- **ホスティング**：別ドメイン（候補：`fastup-lp.com` 再利用 / `lp.fast-up.jp` 新サブドメイン / 新規取得）

## ディレクトリ構成

```
lp/
├── README.md                     # このファイル
├── shared/
│   ├── styles.css                # 全LP共通CSS（正・唯一の土台）
│   ├── img/                      # 共通画像
│   └── liff-redirect.js          # CTAパラメータ動的切替JS
├── 04a-koachi/                   # ✅ 基準LP（共通の正）
│   ├── design.md                 # 設計書
│   ├── index.html                # LP本体
│   ├── style.css                 # 個別CSS（差分のみ。現状は差分ゼロ＝実質空）
│   └── img/                      # LP固有画像
├── 04b-online/ … 13-nittokomasen/  # 各LPフォルダ（index.html / style.css / img / design.md）
```

全LPの `index.html` は `../shared/styles.css` → `style.css` の順で読み込む。

## CSS設計（共通＋差分）★重要

- **`shared/styles.css` を全LP共通の「正」** とする。共通のデザイン変更はここに書く。
- **各LPの `style.css` には、そのLP固有の差分だけ** を書く（共通を後から部分的に上書き）。
- 内容の違い（コピー・画像）は各LPの `index.html` 側で対応する。

### 別LP着手時の手順
1. そのLPの `style.css` は現状「旧CSSのフルコピー」になっている（未修正LPが崩れないための暫定）。**着手時にフルコピーを削除**する。
2. **shared からの差分のみ** を `style.css` に記述する。

### 現状と注意
- `shared/styles.css` は現在 **「04a完成版」がそのまま共通** になっている（共通＋一部04a固有が混在）。
- 2つ目のLPを差分化する際に、「04a固有」と判明したルールを `shared` → `04a/style.css` へ移し、`shared` を“本当の共通”へ純化していく（2つ目着手時に対応）。
- 04a固有画像（`shared/img/` のコーチ画像・CEO写真等）は、他LPでは各LPの画像へ差し替えが必要。
- **04a 以外の13LP（04b含む）は旧フルコピーのまま凍結中**。各LP着手時に上記手順で最新共通へ乗せる。

## 制作対象（バッチ1：6LP）

| # | LPフォルダ | グループ名 | 状態 |
|---|---|---|---|
| 04a | `04a-koachi/` | 学習管理・自学自習 | ✅ 実装v1（修正待ち） |
| 04b | `04b-online/` | オンライン塾（NEW） | 未着手 |
| 05 | `05-soukei/` | 早慶志望群 | 未着手 |
| 06 | `06-waseda/` | 早稲田志望 | 未着手 |
| 07 | `07-keio/` | 慶應志望 | 未着手 |
| 11 | `11-takeda/` | 武田塾層（武田塾名は出さない） | 未着手 |

## ローカルプレビュー手順

### 1. ローカルサーバー起動

```bash
cd /c/nogifa/02_marketing/ads/lp && py -m http.server 8765
```

### 2. ブラウザで開く

| LP | dev URL |
|---|---|
| #04a 学習管理 | http://localhost:8765/04a-koachi/?from=g-04a |

### 3. パラメータ動的切替の動作確認

URLの `?from=g-{グループ番号}` を変えると、CTAボタンのLINE登録URLの `lp=` 値が動的に切り替わる（現状はプレースホルダー、LSTEPで実値を発行後に置換）。

## 山本さん側の並行作業

### 1. 新ドメイン取得
候補：
- `fastup-lp.com` 再利用（既存ドメインだが現在CV0で使われていない）
- `lp.fast-up.jp` 新サブドメイン
- 新規取得

### 2. LSTEP流入経路URL発行（最重要）

LSTEPで14個＋デフォルト1個 = **15個の友達追加URL**を発行 → 各 `lp=XXX` 値を取得 → claude codeに共有 → `lp/shared/liff-redirect.js` のLP_MAPに反映。

| キー | グループ | 発行状況 |
|---|---|---|
| `g-01` | 指名_FAST-UP | 未発行 |
| `g-02` | 逆転合格 | 未発行 |
| `g-03` | 浪人生 | 未発行 |
| `g-04a` | 学習管理_自学自習 | 未発行 |
| `g-04b` | オンライン塾 | 未発行 |
| `g-05` | 早慶志望群 | 未発行 |
| `g-06` | 早稲田志望 | 未発行 |
| `g-07` | 慶應志望 | 未発行 |
| `g-08` | GMARCH志望群 | 未発行 |
| `g-09` | MARCH各校 | 未発行 |
| `g-10a` | 塾比較・選び方 | 未発行 |
| `g-10b` | 料金コスパ検討 | 未発行 |
| `g-11` | 武田塾層 | 未発行 |
| `g-12` | 関関同立志望 | 未発行 |
| `g-13` | 日東駒専志望 | 未発行 |
| `default` | パラメータなし | 未発行 |

### 3. 新Google広告アカウント開設 + API申請（Phase 7出稿前）

## 次回再開時の最初のアクション

1. 上記コマンドでローカルサーバー起動
2. dev URL `http://localhost:8765/04a-koachi/?from=g-04a` を山本さんがブラウザで開く
3. 修正フィードバックをヒアリング
4. `lp/04a-koachi/index.html` `lp/shared/styles.css` を編集して反映
5. 再プレビュー → 確定
6. バッチ1残り5LP（#04b/#05/#06/#07/#11）に展開

## 関連ドキュメント

- 既存LP情報抽出：`../data/lp_existing_extraction.md`
- 競合9社分析：`../data/lp_competitor_analysis.md`
- 情報ランク分け：`../data/lp_info_ranking.md`
- KW振り分け表：`../data/kw_assignment_phase4.csv`

## LP設計の原則（feedback memory）

- `feedback_ad_group_design.md`：広告グループは「同じLPでCVR最大化するくくり」、自分ゴト感が鍵
- `feedback_lp_design.md`：既存の強み × 競合の良い部分 × 自分ゴト感でCVR最強を最優先、手段は択ばない

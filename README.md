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
│   ├── styles.css                # 全LP共通CSS（663行）
│   └── liff-redirect.js          # CTAパラメータ動的切替JS（56行）
├── 04a-koachi/                   # ✅ 実装v1完了
│   ├── design.md                 # 設計書（ペルソナ/14セクション/コピー案）
│   └── index.html                # LP本体
├── 04b-online/                   # 未着手
├── 05-soukei/                    # 未着手
├── 06-waseda/                    # 未着手
├── 07-keio/                      # 未着手
└── 11-takeda/                    # 未着手
```

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

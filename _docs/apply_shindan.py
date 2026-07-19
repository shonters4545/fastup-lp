# -*- coding: utf-8 -*-
import re, os, sys

BASE = r"C:\nogifa\02_marketing\ads\lp"
SRC  = os.path.join(BASE, "05-soukei", "index.html")

with open(SRC, encoding="utf-8") as f:
    s = f.read()

def slice_between(text, start_marker, end_marker):
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    return text[i:j]

# --- 05 から実ブロックを抽出（転記ミス防止） ---
DIAG  = slice_between(s, "<!-- ======= 埋め込み診断", "<!-- ======= LINE登録ブロック ======= -->")
MODAL = slice_between(s, "<!-- 診断誘導モーダル", "<!-- 診断フロート")
FLOAT = slice_between(s, "<!-- 診断フロート", "<!-- スマホ用 sticky CTA -->")
js_i = s.index("<script>/* 埋め込み診断")
js_j = s.index("</script>", js_i) + len("</script>")
JS = s[js_i:js_j] + "\n"

# 抽出健全性チェック
assert 'id="shindan"' in DIAG and 'shindanForm' in JS and 'id="shindanModal"' in MODAL and 'id="shindanFloat"' in FLOAT, "extract failed"

# --- LP別config: (SCHOOL, PRESENT_NAME, PRESENT_SHORT, PRESENT_SUB) ---
LPS = {
 "01-brand":              ("第一志望", "逆転合格 学習法ライブラリ", "逆転合格の学習法", "逆転合格に必要な学習法を1冊に凝縮して無料進呈"),
 "02-gyakuten":           ("逆転", "PLACEHOLDER", "PLACEHOLDER", "PLACEHOLDER"),  # overwritten below
 "03-ronin":              ("第一志望", "浪人1年 逆転計画テンプレ", "浪人の逆転計画", "浪人1年で逆転するための年間計画テンプレを無料進呈"),
 "04a-koachi":            ("第一志望", "逆転合格 学習法ライブラリ", "逆転合格の学習法", "逆転合格に必要な学習法を1冊に凝縮して無料進呈"),
 "04b-online":            ("第一志望", "自宅で伸びる 学習法ガイド", "自宅学習の攻略法", "自宅でも成績を伸ばす学習法ガイドを無料進呈"),
 "06-waseda":             ("早稲田", "早稲田英語 頻出テーマ攻略教材", "早稲田英語の攻略教材", "早稲田英語の頻出テーマを、最短で攻略する教材を無料進呈"),
 "07-keio":               ("慶應", "慶應英語 頻出テーマ攻略教材", "慶應英語の攻略教材", "慶應英語の頻出テーマを、最短で攻略する教材を無料進呈"),
 "08-gmarch":             ("GMARCH", "GMARCH英語 頻出テーマ攻略教材", "GMARCH英語の攻略教材", "GMARCH英語の頻出テーマを、最短で攻略する教材を無料進呈"),
 "09-march-each":         ("MARCH", "MARCH英語 頻出テーマ攻略教材", "MARCH英語の攻略教材", "MARCH英語の頻出テーマを、最短で攻略する教材を無料進呈"),
 "10a-juku-comparison":   ("第一志望", "失敗しない塾選び チェックリスト", "塾選びの判断材料", "塾選びで失敗しないためのチェックリストを無料進呈"),
 "10b-cost-perf":         ("第一志望", "塾費用まるわかり 比較資料", "塾費用の比較資料", "塾の総額・時給を比較できる資料を無料進呈"),
 "11-jigaku-fixed-online":("第一志望", "参考書ルート 設計シート", "参考書ルートの設計法", "志望校までの参考書ルート設計シートを無料進呈"),
 "12-kankandoritsu":      ("関関同立", "関関同立英語 頻出テーマ攻略教材", "関関同立英語の攻略教材", "関関同立英語の頻出テーマを、最短で攻略する教材を無料進呈"),
 "13-nittokomasen":       ("日東駒専", "日東駒専英語 頻出テーマ攻略教材", "日東駒専英語の攻略教材", "日東駒専英語の頻出テーマを、最短で攻略する教材を無料進呈"),
}
# 02 は日本語で明示上書き（可読性のため）
LPS["02-gyakuten"] = ("逆転", "偏差値30台からの逆転 学習法ガイド", "逆転合格の学習法", "偏差値30台から逆転するための学習法ガイドを無料進呈")

# --- 早慶依存テキストをLP別に置換する関数（順序重要） ---
SOU = "早慶"  # 早慶
def sub(text, school, pname, pshort, psub):
    text = text.replace(SOU + "英語 頻出テーマ攻略教材", pname)                # 早慶英語 頻出テーマ攻略教材
    text = text.replace(SOU + "英語の頻出テーマを、最短で攻略する教材を無料進呈", psub)  # sub
    text = text.replace(SOU + "英語の攻略教材", pshort)                                   # 早慶英語の攻略教材
    text = text.replace("英語（" + SOU + "は英語で差がつく）", "英語（配点が高く、合否を分ける）")  # 英語（早慶は英語で差がつく）→中立
    text = text.replace(SOU + "合格可能性", school + "合格可能性")             # 早慶合格可能性
    text = text.replace(SOU + "合格の可能性", school + "合格の可能性") # 早慶合格の可能性
    text = text.replace(SOU, school)                                                                                 # 残り早慶
    return text

changed = 0
for lp,(school,pname,pshort,psub) in LPS.items():
    path = os.path.join(BASE, lp, "index.html")
    with open(path, encoding="utf-8") as f:
        t = f.read()
    if 'id="shindan"' in t:
        print("SKIP already:", lp); continue

    d = sub(DIAG, school, pname, pshort, psub)
    m = sub(MODAL, school, pname, pshort, psub)
    fl = sub(FLOAT, school, pname, pshort, psub)
    j = sub(JS, school, pname, pshort, psub)

    # 1) CTA①: 診断ボタン挿入＋ボタン文言をカウンセリングへ
    inline = ('    <a href="#shindan" class="shindan-inline-cta">＼' + school +
              '合格の可能性が1分でわかる／<b>' + school +
              '合格可能性診断を受ける</b></a>\n    ')
    pat = re.compile(r'(<a href="[^"]*" class="counsel-cta reveal">.*?<span class="counsel-cta-text">)逆転ルート診断を受ける(</span>\s*</a>)', re.DOTALL)
    t2, n1 = pat.subn(inline + r'\1無料カウンセリングを予約\2', t)
    assert n1 == 1, lp + " CTA1 fail:" + str(n1)
    t = t2

    # 2) プレゼントブロック差し替え
    t, a = re.subn(re.escape("無料カウンセリング予約・学習相談、すべてLINEで完結。"),
                   "友だち追加で〈" + pname + "〉をプレゼント。無料カウンセリング予約・学習相談もLINEで完結。", t)
    t = t.replace('alt="学習法ライブラリ"', 'alt="' + pname + '"')
    t, b = re.subn(re.escape("「学習法ライブラリ」プレゼント<small>逆転合格に必要な学習法を1冊に凝縮</small>"),
                   "「" + pname + "」プレゼント<small>" + psub + "</small>", t)
    assert a == 1 and b == 1, lp + " gift fail"

    # 3) 診断本体をLINE登録ブロックの直前に注入
    t = t.replace("<!-- ======= LINE登録ブロック ======= -->", d + "<!-- ======= LINE登録ブロック ======= -->", 1)
    # 4) モーダル+フロートを sticky CTA の直前に注入
    t = t.replace("<!-- スマホ用 sticky CTA -->", m + fl + "<!-- スマホ用 sticky CTA -->", 1)
    # 5) JSを </body> 直前に注入
    t = t.replace("</body>", j + "</body>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(t)
    changed += 1
    print("OK:", lp, "| school=", school, "| present=", pname)

print("\nDONE changed:", changed)

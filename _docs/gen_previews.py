# -*- coding: utf-8 -*-
import io, os, json

OUT = r"C:\nogifa\02_marketing\ads\lp\_docs\preview"
os.makedirs(OUT, exist_ok=True)

CSS = """*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:"Noto Sans JP",sans-serif;background:#efe9e3;color:#222;line-height:1.7;-webkit-text-size-adjust:100%;}
.review-bar{background:#222;color:#fff;padding:14px 18px;font-size:12px;line-height:1.8;}
.review-bar b{color:#e8b4bc;}
.review-bar a{color:#9ad0ff;}
.review-bar .rv-title{font-size:13px;font-weight:900;display:block;margin-bottom:4px;}
.stage{padding:40px 20px 80px;}
.card-wrap{max-width:640px;margin:0 auto;}
#shindan{--sd-acc:#722F37;}
.shindan-head{text-align:center;margin-bottom:26px;}
.shindan-eyebrow{display:inline-block;font-size:12px;letter-spacing:.14em;font-weight:700;color:#fff;background:var(--sd-acc);padding:5px 14px;border-radius:999px;}
.shindan-title{font-size:28px;font-weight:900;margin:14px 0 10px;line-height:1.3;}
.shindan-title em{font-style:normal;color:var(--sd-acc);}
.shindan-lead{font-size:14px;line-height:1.8;color:#555;}
.shindan-lead b{color:var(--sd-acc);}
.shindan-form,.shindan-result{background:#fff;border-radius:18px;padding:26px 22px;box-shadow:0 12px 40px rgba(0,0,0,.08);}
.shindan-progress{font-size:11px;color:#999;text-align:right;margin-bottom:14px;letter-spacing:.05em;}
.shindan-q{margin-bottom:22px;}
.shindan-q-label{font-size:15px;font-weight:800;margin-bottom:12px;}
.shindan-q-label span{color:var(--sd-acc);margin-right:6px;}
.shindan-opts{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.shindan-opt{font-size:13.5px;font-weight:700;color:#333;background:#f4f4f6;border:2px solid #f4f4f6;border-radius:12px;padding:13px 8px;cursor:pointer;transition:.15s;font-family:inherit;line-height:1.4;}
.shindan-opt:hover{border-color:var(--sd-acc);}
.shindan-opt.is-on{background:var(--sd-acc);border-color:var(--sd-acc);color:#fff;}
.shindan-submit{width:100%;margin-top:6px;font-size:16px;font-weight:800;color:#fff;background:var(--sd-acc);border:none;border-radius:12px;padding:16px;cursor:pointer;font-family:inherit;transition:.2s;}
.shindan-submit:disabled{background:#c9c2c3;cursor:not-allowed;}
.shindan-note{font-size:11px;color:#999;text-align:center;margin-top:12px;}
.shindan-result{text-align:left;}
.rb{padding:22px 0;border-bottom:1px solid #eee;}
.rb:first-child{padding-top:0;}
.rb:last-child{border-bottom:none;padding-bottom:0;}
.res-eyebrow{display:block;font-size:13px;font-weight:700;color:#777;text-align:center;}
.res-gauge{text-align:center;color:var(--sd-acc);font-weight:900;line-height:1;margin:6px 0 4px;}
.res-num{font-size:64px;}
.res-unit{font-size:26px;margin-left:2px;}
.res-bar{height:10px;background:#eee;border-radius:999px;overflow:hidden;margin:8px auto 16px;max-width:320px;}
.res-bar-fill{display:block;height:100%;width:0;background:linear-gradient(90deg,#b9535f,var(--sd-acc));border-radius:999px;transition:width 1.1s ease;}
.res-type{text-align:center;font-size:34px;font-weight:900;color:var(--sd-acc);line-height:1.3;margin:8px 0 12px;}
.res-verdict{font-size:18px;font-weight:900;text-align:center;line-height:1.55;}
.rb h4{font-size:14px;font-weight:900;color:var(--sd-acc);margin-bottom:8px;}
.rb p.body{font-size:14px;line-height:1.9;color:#444;}
.offer{background:#f6f1ec;border-radius:14px;padding:20px 18px;margin-top:6px;}
.offer-title{font-size:18px;font-weight:900;text-align:center;line-height:1.5;margin-bottom:8px;}
.offer-title em{font-style:normal;color:var(--sd-acc);}
.offer-subtitle{text-align:center;font-size:14px;font-weight:900;color:#fff;background:var(--sd-acc);border-radius:999px;padding:7px 16px;display:block;width:fit-content;margin:0 auto 10px;letter-spacing:.02em;}
.offer-note{text-align:center;font-size:12px;color:#666;line-height:1.7;margin-bottom:14px;}
.offer-note b{color:var(--sd-acc);font-weight:900;}
.offer-body{display:flex;gap:14px;align-items:center;margin-bottom:16px;}
.offer-img{flex:0 0 38%;aspect-ratio:3/4;background:#fff;border:2px dashed #cfc4c5;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:11px;font-weight:800;color:#a99a9c;line-height:1.6;}
.offer-img span{font-size:9.5px;font-weight:700;color:#c3b6b7;}
.offer-checks{flex:1;list-style:none;}
.offer-checks li{position:relative;padding-left:26px;font-size:13px;line-height:1.65;color:#333;margin-bottom:12px;font-weight:700;}
.offer-checks li:last-child{margin-bottom:0;}
.offer-checks li::before{content:"\\2713";position:absolute;left:0;top:2px;width:18px;height:18px;background:var(--sd-acc);color:#fff;border-radius:4px;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;}
.offer-checks b{color:var(--sd-acc);font-weight:900;}
.line-btn{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;font-size:16px;font-weight:800;color:#fff;background:#06c755;border-radius:12px;padding:16px;text-decoration:none;box-shadow:0 8px 22px rgba(6,199,85,.3);}
.retry{display:block;margin:14px auto 0;background:none;border:none;color:#999;font-size:13px;text-decoration:underline;cursor:pointer;font-family:inherit;}
@media(max-width:420px){.shindan-title{font-size:23px;}.res-num{font-size:54px;}.res-type{font-size:28px;}.offer-body{flex-direction:column;}.offer-img{flex:none;width:60%;aspect-ratio:4/3;}}"""

SUBJ_Q = """    <div class="shindan-q" data-q="%(n)s">
      <p class="shindan-q-label"><span>Q%(n)s.</span>一番の苦手科目は？</p>
      <div class="shindan-opts">
        <button type="button" class="shindan-opt" data-v="eng">英語</button>
        <button type="button" class="shindan-opt" data-v="jpn">国語</button>
        <button type="button" class="shindan-opt" data-v="soc">社会</button>
        <button type="button" class="shindan-opt" data-v="mat">数学</button>
      </div>
    </div>"""

BASE_Q = """    <div class="shindan-q" data-q="1">
      <p class="shindan-q-label"><span>Q1.</span>いまの偏差値は？</p>
      <div class="shindan-opts">
        <button type="button" class="shindan-opt" data-v="0">%(H0)s</button>
        <button type="button" class="shindan-opt" data-v="1">%(H1)s</button>
        <button type="button" class="shindan-opt" data-v="2">%(H2)s</button>
        <button type="button" class="shindan-opt" data-v="3">%(H3)s</button>
      </div>
    </div>
    <div class="shindan-q" data-q="2">
      <p class="shindan-q-label"><span>Q2.</span>本番まで残りは？</p>
      <div class="shindan-opts">
        <button type="button" class="shindan-opt" data-v="0">3ヶ月以内</button>
        <button type="button" class="shindan-opt" data-v="1">4〜6ヶ月</button>
        <button type="button" class="shindan-opt" data-v="2">7〜12ヶ月</button>
        <button type="button" class="shindan-opt" data-v="3">13ヶ月以上</button>
      </div>
    </div>
    <div class="shindan-q" data-q="3">
      <p class="shindan-q-label"><span>Q3.</span>勉強はひとりで続けられる？</p>
      <div class="shindan-opts">
        <button type="button" class="shindan-opt" data-v="0">ほぼ続かない</button>
        <button type="button" class="shindan-opt" data-v="1">波がある</button>
        <button type="button" class="shindan-opt" data-v="2">だいたい続く</button>
        <button type="button" class="shindan-opt" data-v="3">問題なく続く</button>
      </div>
    </div>"""

OFFER = """      <div class="offer">
        <p class="offer-title">%(TOKKA)sの独自教材を、<em>体感してみませんか？</em></p>
        <p class="offer-subtitle" id="offerSubtitle"></p>
        <p class="offer-note" id="offerNote"></p>
        <div class="offer-body">
          <div class="offer-img">教材モックアップ<span>（画像を後ではめ込み）</span></div>
          <ul class="offer-checks">
            <li>%(CHECK1)s</li>
            <li>%(CHECK2)s</li>
            <li>%(CHECK3)s</li>
          </ul>
        </div>
        <a href="#" class="line-btn" onclick="return false;">LINE登録で教材を受け取る <span aria-hidden="true">›</span></a>
      </div>
      <button type="button" class="retry" id="retry">もう一度診断する</button>"""

PAGE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>【プレビュー】%(LP)s %(DNAME)s</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
<style>
%(CSS)s
</style>
</head>
<body>
<div class="review-bar">
  <span class="rv-title">【レビュー用プレビュー】%(LP)s「%(DNAME)s」</span>
  グループ%(GRP)s（%(GRPNAME)s）／設問%(QN)s問。回答を変えると結果・あなたの現状・これからやるべきこと・プレゼント科目がすべて変わります。<br>
  ※本番LPには未反映。 <a href="./index.html">← 全LP一覧へ</a>
</div>
<div class="stage">
<div class="card-wrap" id="shindan">
  <div class="shindan-head">
    <span class="shindan-eyebrow">1分でわかる</span>
    <h2 class="shindan-title">%(TITLE_HTML)s</h2>
    <p class="shindan-lead">%(LEAD)s</p>
  </div>
  <form class="shindan-form" id="form">
    <p class="shindan-progress" id="prog">0 / %(QN)s 問</p>
%(QUESTIONS)s
    <button type="button" class="shindan-submit" id="submit" disabled>診断結果を見る</button>
    <p class="shindan-note">※あくまで目安です。正確な合格戦略は無料カウンセリングで。</p>
  </form>
  <div class="shindan-result" id="result" hidden>
    <div class="rb">
%(RESULT_TOP)s
    </div>
    <div class="rb">
      <h4>あなたの現状</h4>
      <p class="body" id="detail"></p>
    </div>
    <div class="rb">
      <h4>これからやるべきこと</h4>
      <p class="body" id="advice"></p>
    </div>
    <div class="rb">
%(OFFER)s
    </div>
  </div>
</div>
</div>
<script>
(function(){
  var QN=%(QN)s;
  var ans={}; for(var i=1;i<=QN;i++) ans[i]=null;
  var form=document.getElementById('form'), submit=document.getElementById('submit'), prog=document.getElementById('prog');
  var HENSA=%(HENSA_JS)s;
  var MONTH=['残り3ヶ月以内','残り4〜6ヶ月','残り7〜12ヶ月','残り13ヶ月以上'];
  var SUBJ={eng:'英語',jpn:'国語',soc:'社会',mat:'数学'};
  form.querySelectorAll('.shindan-q').forEach(function(q){
    var qi=q.getAttribute('data-q'), opts=q.querySelectorAll('.shindan-opt');
    opts.forEach(function(b){
      b.addEventListener('click',function(){
        opts.forEach(function(o){o.classList.remove('is-on');});
        b.classList.add('is-on'); ans[qi]=b.getAttribute('data-v');
        var n=0; for(var k=1;k<=QN;k++){ if(ans[k]!==null) n++; }
        prog.textContent=n+' / '+QN+' 問';
        submit.disabled=(n<QN);
      });
    });
  });
  submit.addEventListener('click',function(){
%(LOGIC)s
    document.getElementById('offerSubtitle').textContent='%(BOOK)s'+sj+'%(BOOK_SUFFIX)s　無料プレゼント';
    document.getElementById('offerNote').innerHTML='このシリーズの全科目の中から、あなたが選んだ<b>'+sj+'</b>をお渡しします。';
    document.getElementById('detail').textContent=detail;
    document.getElementById('advice').textContent=advice;
    form.hidden=true; document.getElementById('result').hidden=false;
%(REVEAL)s
    document.getElementById('result').scrollIntoView({behavior:'smooth',block:'start'});
  });
  document.getElementById('retry').addEventListener('click',function(){
    document.getElementById('result').hidden=true; form.hidden=false;
    form.querySelectorAll('.shindan-opt').forEach(function(o){o.classList.remove('is-on');});
    for(var k=1;k<=QN;k++) ans[k]=null;
    submit.disabled=true; prog.textContent='0 / '+QN+' 問';
    form.scrollIntoView({behavior:'smooth',block:'start'});
  });
})();
</script>
</body>
</html>"""

# ============ グループA ============
A_RESULT_TOP = """      <span class="res-eyebrow">あなたの%(EYE)s 可能性</span>
      <div class="res-gauge"><span class="res-num" id="pct">0</span><span class="res-unit">%%</span></div>
      <div class="res-bar"><span class="res-bar-fill" id="bar"></span></div>
      <p class="res-verdict" id="verdict"></p>"""

A_LOGIC = """    var h=+ans[1], m=+ans[2], k=+ans[3], w=ans[4];
    var pH=%(PH)s[h], pM=[-8,0,8,14][m], pK=[-10,-4,4,10][k], pW=(w==='eng'?-6:w==='jpn'?-3:w==='mat'?-2:-1);
    var poss=50+pH+pM+pK+pW;
    if(poss<35)poss=35; if(poss>92)poss=92;
    var sj=SUBJ[w], hs=HENSA[h], mo=MONTH[m];
    var LONG=(m>=2);
    var verdict, detail, advice;
    if(poss>=75){
      verdict='%(V_HI)s';
      if(LONG){
        detail='いまは'+hs+'・'+mo+'です。基礎の力はもう十分にあり、時間にも余裕があります。ここで差がつくのは、%(TG)sに必要なところを早めに仕上げておけるかどうかです。';
        advice='%(TG)sに必要なところから、先に仕上げてください。%(TG)s入試で出るところは決まっています。時間があるうちに'+sj+'をそこまで引き上げておけば、合格率は大きく上がります。';
      } else {
        detail='いまは'+hs+'・'+mo+'です。基礎の力はもう十分にあります。ここから合否を分けるのは、%(TG)sが実際に出す問題にどれだけ慣れているかです。学力よりも、%(TG)sに向けた準備があるかで決まります。';
        advice='%(TG)sが出す問題に合わせて勉強してください。基礎ができている人の差は、出る形式とテーマに慣れているかで決まります。'+sj+'もそこに絞って勉強すれば、合格点を確実に超えられます。';
      }
    } else if(poss>=55){
      verdict='%(V_MID)s';
      if(LONG){
        detail='いまは'+hs+'・'+mo+'です。%(TG)s合格は十分にねらえて、時間にも余裕があります。ここで差がつくのは、なんとなく勉強を続けるか、%(TG)sに必要なところから勉強するかです。';
        advice='%(TG)sに必要なところから勉強してください。%(TG)s入試で出るところは決まっています。早いうちから'+sj+'をそこに向けて仕上げていけば、合格率は大きく上がります。';
      } else {
        detail='いまは'+hs+'・'+mo+'です。%(TG)s合格は十分にねらえます。ここから差がつくのは、勉強する量ではなく、どこを勉強するかです。出るところに絞れているかで決まります。';
        advice='勉強する範囲を、これ以上広げないでください。%(TG)s入試で合否を分けるのは、範囲の広さではなく、出るところをどこまで仕上げたかです。'+sj+'のよく出るテーマから先に仕上げれば、合格点は安定します。';
      }
    } else {
      verdict='%(V_LOW)s';
      if(LONG){
        detail='いまは'+hs+'・'+mo+'です。%(D_LOW_LONG)s';
        advice='いまから%(TG)sに必要な勉強を始めてください。%(TG)s入試で出るところは決まっています。早いうちから'+sj+'をそこに向けて勉強すれば、合格率は大きく上がります。';
      } else {
        detail='いまは'+hs+'・'+mo+'です。%(D_LOW)s';
        advice='勉強する範囲を絞ってください。%(TG)s入試で出るところは決まっています。苦手な'+sj+'も、出るところだけを勉強すれば、最短で合格点に届きます。';
      }
    }
    document.getElementById('verdict').textContent=verdict;
    document.getElementById('bar').style.width=poss+'%%';"""

A_REVEAL = """    var el=document.getElementById('pct'), cur=0;
    var t=setInterval(function(){cur+=Math.max(1,Math.round((poss-cur)/6)); if(cur>=poss){cur=poss;clearInterval(t);} el.textContent=cur;},40);"""

# ============ グループB ============
B_RESULT_TOP = """      <span class="res-eyebrow">あなたに合うのは</span>
      <div class="res-type" id="typeName"></div>
      <p class="res-verdict" id="verdict"></p>"""

B_LOGIC = """    var h=+ans[1], m=+ans[2], k=+ans[3], t4=ans[4], w=ans[5];
    var sj=SUBJ[w], hs=HENSA[h], mo=MONTH[m];
    var LONG=(m>=2);
    var TYPE={plan:'毎日管理型',lib:'教材特化型',test:'テスト反復型',log:'データ分析型'};
    var ty=t4;
    var verdict, detail, advice;
    if(ty==='plan'){
      verdict='毎日やることが決まれば、動けるタイプ。';
      detail='いまは'+hs+'・'+mo+'です。足りていないのは学力よりも、毎日やることが決まっている状態です。何をやるか迷う時間が増えると、勉強できる時間そのものが減ります。やることが決まれば、ここから伸びます。';
      advice=(LONG?'いまから、毎日':'毎日')+'やることが決まっている状態にしてください。%(TGB)s入試で出るところは決まっています。それが順番に並んでいれば、迷う時間がなくなり、'+(LONG?'早く始めるほど合格率は大きく上がります。':'最短で合格点に届きます。');
    } else if(ty==='lib'){
      verdict='使う教材が決まれば、伸びるタイプ。';
      detail='いまは'+hs+'・'+mo+'です。課題は、何をどの順で勉強するかが決まっていないことです。教材がばらばらだと、勉強した量のわりに点が伸びません。出る順に並んだ教材を1つに決めれば、変わります。';
      advice=(LONG?'いまから、使う':'使う')+'教材を1つに絞ってください。%(TGB)s入試で出るところは決まっています。出る順に並んだ教材だけを使えば、量に頼らず'+(LONG?'、早く始めるほど合格率は大きく上がります。':'最短で合格点に届きます。');
    } else if(ty==='test'){
      verdict='理解を確認できれば、点になるタイプ。';
      detail='いまは'+hs+'・'+mo+'です。勉強しているのに伸びないときは、覚えきれていないことがほとんどです。読んで分かった状態と、テストで答えられる状態は別です。確認する回数が足りていないだけです。';
      advice=(LONG?'いまから、理解':'理解')+'できたかを、その場で確認できるようにしてください。入試で点になるのは、読んだ内容ではなく、自分で答えられる内容です。単元ごとに確認すれば、'+(LONG?'早く始めるほど合格率は大きく上がります。':'抜けを残さず合格点に届きます。');
    } else {
      verdict='弱点が見えれば、最短で伸びるタイプ。';
      detail='いまは'+hs+'・'+mo+'です。勉強する時間は足りていても、どこが弱いか分からないままだと伸びは止まります。感覚で振り返ると、得意なところばかり繰り返しがちです。数値で見えれば、順番が変わります。';
      advice=(LONG?'いまから、弱点':'弱点')+'を数値で把握してください。伸びが止まる原因は、どこが弱いか分からないことです。理解度が数値で見えれば、何から手をつけるかが決まり、'+(LONG?'早く始めるほど合格率は大きく上がります。':'最短で合格点に届きます。');
    }
    document.getElementById('typeName').textContent=TYPE[ty];
    document.getElementById('verdict').textContent=verdict;"""

B_REVEAL = ""

# ============ LP設定 ============
A_LPS = [
 # lp, 診断名, タイトルHTML, EYE(結果見出し), TG(コピー内の対象語), 特化ラベル, check1
 ("01-brand","私大逆転合格 可能性診断","私大逆転合格 可能性<em>診断</em>","私大逆転合格","私大","私大特化","私大専門で<b>7年</b>、出題傾向を分析し続けて作成"),
 ("02-gyakuten","逆転合格可能性診断","逆転合格可能性<em>診断</em>","逆転合格","私大","逆転合格特化","私大専門で<b>7年</b>、<b>逆転合格者の伸び方</b>を分析して作成"),
 ("03-ronin","浪人逆転合格 可能性診断","浪人逆転合格 可能性<em>診断</em>","浪人逆転合格","私大","私大特化","私大専門で<b>7年</b>、出題傾向を分析し続けて作成"),
 ("05-soukei","早慶合格可能性診断","早慶合格可能性<em>診断</em>","早慶合格","早慶","早慶特化","私大専門で<b>7年</b>、<b>早慶</b>の出題傾向を分析し続けて作成"),
 ("06-waseda","早稲田合格可能性診断","早稲田合格可能性<em>診断</em>","早稲田合格","早稲田","早稲田特化","私大専門で<b>7年</b>、<b>早稲田</b>の出題傾向を分析し続けて作成"),
 ("07-keio","慶應合格可能性診断","慶應合格可能性<em>診断</em>","慶應合格","慶應","慶應特化","私大専門で<b>7年</b>、<b>慶應</b>の出題傾向を分析し続けて作成"),
 ("08-gmarch","GMARCH合格可能性診断","GMARCH合格可能性<em>診断</em>","GMARCH合格","GMARCH","GMARCH特化","私大専門で<b>7年</b>、<b>GMARCH</b>の出題傾向を分析し続けて作成"),
 ("09-march-each","MARCH合格可能性診断","MARCH合格可能性<em>診断</em>","MARCH合格","MARCH","MARCH特化","私大専門で<b>7年</b>、<b>MARCH各校</b>の出題傾向を分析し続けて作成"),
 ("12-kankandoritsu","関関同立合格可能性診断","関関同立合格可能性<em>診断</em>","関関同立合格","関関同立","関関同立特化","私大専門で<b>7年</b>、<b>関関同立</b>の出題傾向を分析し続けて作成"),
 ("13-nittokomasen","日東駒専合格可能性診断","日東駒専合格可能性<em>診断</em>","日東駒専合格","日東駒専","日東駒専特化","私大専門で<b>7年</b>、<b>日東駒専</b>の出題傾向を分析し続けて作成"),
]

B_LPS = [
 # lp, 診断名, タイトルHTML, Q4ラベル, Q4選択肢[(label,type)]
 ("04a-koachi","あなたに合うコーチング塾 タイプ診断","あなたに合うコーチング塾<br><em>タイプ診断</em>","塾に一番求めるものは？",
   [("毎日の管理","plan"),("進め方と教材","lib"),("定着の確認","test"),("弱点の可視化","log")]),
 ("04b-online","あなたに合うオンライン塾 タイプ診断","あなたに合うオンライン塾<br><em>タイプ診断</em>","自宅学習で崩れる原因は？",
   [("今日やることが決まらない","plan"),("何で勉強すればいいか分からない","lib"),("やったつもりで終わる","test"),("伸びているか分からない","log")]),
 ("10a-juku-comparison","あなたに合う塾 タイプ診断","あなたに合う塾<em>タイプ診断</em>","塾選びで一番不安なのは？",
   [("続けられるか","plan"),("教材が自分に合うか","lib"),("本当に力がつくか","test"),("成果が見えるか","log")]),
 ("10b-cost-perf","費用から選ぶ 塾タイプ診断","費用から選ぶ<br><em>塾タイプ診断</em>","お金を払うなら何に一番払いたい？",
   [("毎日の管理","plan"),("教材とカリキュラム","lib"),("定着の確認テスト","test"),("学習データの分析","log")]),
 ("11-jigaku-fixed-online","あなたに合う自学サポート塾 タイプ診断","あなたに合う自学サポート塾<br><em>タイプ診断</em>","自学で足りないものは？",
   [("毎日の計画","plan"),("使う教材とルート","lib"),("定着の確認","test"),("進捗と弱点の把握","log")]),
]


DEF = {
 "H":["〜45","46〜55","56〜65","66〜"],
 "HENSA_JS":"['偏差値45以下','偏差値46〜55','偏差値56〜65','偏差値66以上']",
 "PH":"[-10,2,14,22]",
 "V_HI":"合格できる位置です。あとは%(TG)sの問題に慣れるだけ。",
 "V_MID":"十分にねらえます。差がつくのは、どこを勉強するかです。",
 "V_LOW":"合格できます。あとは勉強する範囲を絞れるかです。",
 "D_LOW":"合格ラインとはまだ差がありますが、%(TG)sに合格することは十分にできます。ただ、全部の範囲を勉強する時間はありません。出るところだけを勉強する必要があります。",
 "D_LOW_LONG":"合格ラインとはまだ差がありますが、時間はたっぷり残っています。差がつくのは、%(TG)sに必要な勉強をいつから始めるかです。早く始めた人ほど、合格に近づきます。",
 "LEAD":"4つの質問に答えるだけで、いまの合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。",
 "BOOK":"FAST-UP 私大逆転 ",
 "BOOK_SUFFIX":"",
 "LEAD_B":"5つの質問に答えるだけで、あなたに合う塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。",
 "CHECK2":"<b>感動する！</b>圧倒的な分かりやすさ",
 "CHECK3":"<b>セクションごとの確認テスト</b>で、定着まで",
}
OVERRIDE = {
 "02-gyakuten": {
   "H":["〜35","36〜45","46〜55","56〜"],
   "HENSA_JS":"['偏差値35以下','偏差値36〜45','偏差値46〜55','偏差値56以上']",
   "PH":"[-6,2,12,20]",
   "V_HI":"逆転どころか、もう合格できる位置です。",
   "V_LOW":"E判定からでも、逆転は可能です。",
   "D_LOW":"E判定や偏差値30台からの逆転は、毎年実際に起きています。ただ、全部の範囲を勉強する時間はありません。出るところだけを勉強する必要があります。",
   "D_LOW_LONG":"E判定や偏差値30台からの逆転は、毎年実際に起きています。時間もたっぷり残っています。差がつくのは、%(TG)sに必要な勉強をいつから始めるかです。早く始めた人ほど、合格に近づきます。",
   "LEAD":"4つの質問に答えるだけで、<b>いまE判定でも逆転できるのか</b>と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。",
   "CHECK2":"<b>感動する！</b>基礎から分かる圧倒的な分かりやすさ",
   "CHECK3":"<b>セクションごとの確認テスト</b>で、抜けを残さない",
 },
}


OVERRIDE["03-ronin"] = {
 "LEAD": "4つの質問に答えるだけで、この1年で合格できるかと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。",
 "V_LOW":"この1年で、合格できます。",
 "D_LOW":"合格ラインとはまだ差がありますが、この1年で%(TG)sに合格することは十分にできます。ただ、全部の範囲を勉強する時間はありません。出るところだけを勉強する必要があります。",
 "CHECK1_A":"私大専門で<b>7年</b>、<b>浪人生の伸び方</b>を分析して作成",
}
OVERRIDE["05-soukei"] = {"H":['〜50', '51〜60', '61〜70', '71〜'],"HENSA_JS":"['偏差値50以下','偏差値51〜60','偏差値61〜70','偏差値71以上']","LEAD":"4つの質問に答えるだけで、いまの早慶合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["06-waseda"] = {"H":['〜50', '51〜60', '61〜70', '71〜'],"HENSA_JS":"['偏差値50以下','偏差値51〜60','偏差値61〜70','偏差値71以上']","LEAD":"4つの質問に答えるだけで、いまの早稲田合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["07-keio"]   = {"H":['〜50', '51〜60', '61〜70', '71〜'],"HENSA_JS":"['偏差値50以下','偏差値51〜60','偏差値61〜70','偏差値71以上']","LEAD":"4つの質問に答えるだけで、いまの慶應合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["08-gmarch"] = {"LEAD":"4つの質問に答えるだけで、いまのGMARCH合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["09-march-each"] = {"LEAD":"4つの質問に答えるだけで、いまのMARCH合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["12-kankandoritsu"] = {"LEAD":"4つの質問に答えるだけで、いまの関関同立合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["13-nittokomasen"] = {"H":['〜40', '41〜50', '51〜60', '61〜'],"HENSA_JS":"['偏差値40以下','偏差値41〜50','偏差値51〜60','偏差値61以上']","LEAD":"4つの質問に答えるだけで、いまの日東駒専合格可能性と、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["04a-koachi"] = {"LEAD_B":"5つの質問に答えるだけで、あなたに合うコーチング塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["04b-online"] = {"LEAD_B":"5つの質問に答えるだけで、あなたに合うオンライン塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["10a-juku-comparison"] = {"LEAD_B":"5つの質問に答えるだけで、あなたに合う塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。"}
OVERRIDE["10b-cost-perf"] = {"LEAD_B":"5つの質問に答えるだけで、費用に見合う塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。","CHECK1_B":"私大専門で<b>7年</b>、出題傾向を分析し続けて作成（<b>追加費用ゼロ</b>）"}
OVERRIDE["11-jigaku-fixed-online"] = {"LEAD_B":"5つの質問に答えるだけで、自学に足りないものと、合う塾のタイプと、次に何をやればいいかがわかります。<br>結果に合わせて<b>あなたの苦手科目の独自教材</b>を無料プレゼント。","CHECK1_B":"私大専門で<b>7年</b>、<b>出る順の参考書ルート</b>として作成"}

OVERRIDE.setdefault("05-soukei",{}); OVERRIDE["05-soukei"]["BOOK"]="FAST-UP 早慶必出 "; OVERRIDE["05-soukei"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("06-waseda",{}); OVERRIDE["06-waseda"]["BOOK"]="FAST-UP 早稲田必出 "; OVERRIDE["06-waseda"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("07-keio",{}); OVERRIDE["07-keio"]["BOOK"]="FAST-UP 慶應必出 "; OVERRIDE["07-keio"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("08-gmarch",{}); OVERRIDE["08-gmarch"]["BOOK"]="FAST-UP GMARCH必出 "; OVERRIDE["08-gmarch"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("09-march-each",{}); OVERRIDE["09-march-each"]["BOOK"]="FAST-UP MARCH必出 "; OVERRIDE["09-march-each"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("12-kankandoritsu",{}); OVERRIDE["12-kankandoritsu"]["BOOK"]="FAST-UP 関関同立必出 "; OVERRIDE["12-kankandoritsu"]["BOOK_SUFFIX"]=""
OVERRIDE.setdefault("13-nittokomasen",{}); OVERRIDE["13-nittokomasen"]["BOOK"]="FAST-UP 日東駒専必出 "; OVERRIDE["13-nittokomasen"]["BOOK_SUFFIX"]=""

files=[]

for lp,dname,title_html,eye,tg,tokka,check1 in A_LPS:
    cfg=dict(DEF); cfg.update(OVERRIDE.get(lp,{}))
    vhi=cfg["V_HI"] % {"TG":tg} if "%(TG)s" in cfg["V_HI"] else cfg["V_HI"]
    dlow=cfg["D_LOW"] % {"TG":tg} if "%(TG)s" in cfg["D_LOW"] else cfg["D_LOW"]
    q = (BASE_Q % {"H0":cfg["H"][0],"H1":cfg["H"][1],"H2":cfg["H"][2],"H3":cfg["H"][3]}) + chr(10) + (SUBJ_Q % {"n":4})
    dlong=cfg["D_LOW_LONG"] % {"TG":tg} if "%(TG)s" in cfg["D_LOW_LONG"] else cfg["D_LOW_LONG"]
    logic = A_LOGIC % {"TG":tg,"HENSA_JS":cfg["HENSA_JS"],"PH":cfg["PH"],"V_HI":vhi,"V_MID":cfg["V_MID"],"V_LOW":cfg["V_LOW"],"D_LOW":dlow,"D_LOW_LONG":dlong}
    html = PAGE % {
      "LP":lp,"DNAME":dname,"CSS":CSS,"GRP":"A","GRPNAME":"合格可能性診断","QN":4,"HENSA_JS":cfg["HENSA_JS"],"BOOK":cfg["BOOK"],"BOOK_SUFFIX":cfg["BOOK_SUFFIX"],
      "TITLE_HTML":title_html,"LEAD":cfg["LEAD"],"QUESTIONS":q,
      "RESULT_TOP":A_RESULT_TOP % {"EYE":eye},
      "OFFER":OFFER % {"TOKKA":tokka,"CHECK1":cfg.get("CHECK1_A",check1),"CHECK2":cfg["CHECK2"],"CHECK3":cfg["CHECK3"]},
      "LOGIC":logic,"REVEAL":A_REVEAL,
    }
    io.open(os.path.join(OUT,lp+"-shindan.html"),"w",encoding="utf-8").write(html)
    files.append((lp,dname,"A"))

for lp,dname,title_html,q4label,q4opts in B_LPS:
    opts="\n".join(['        <button type="button" class="shindan-opt" data-v="%s">%s</button>'%(t,l) for l,t in q4opts])
    q4 = """    <div class="shindan-q" data-q="4">
      <p class="shindan-q-label"><span>Q4.</span>%s</p>
      <div class="shindan-opts">
%s
      </div>
    </div>""" % (q4label,opts)
    cfg=dict(DEF); cfg.update(OVERRIDE.get(lp,{}))
    q = (BASE_Q % {"H0":cfg["H"][0],"H1":cfg["H"][1],"H2":cfg["H"][2],"H3":cfg["H"][3]}) + chr(10) + q4 + chr(10) + (SUBJ_Q % {"n":5})
    html = PAGE % {
      "LP":lp,"DNAME":dname,"CSS":CSS,"GRP":"B","GRPNAME":"塾タイプ診断","QN":5,"HENSA_JS":cfg["HENSA_JS"],"BOOK":cfg["BOOK"],"BOOK_SUFFIX":cfg["BOOK_SUFFIX"],
      "TITLE_HTML":title_html,
      "LEAD":cfg["LEAD_B"],
      "QUESTIONS":q,
      "RESULT_TOP":B_RESULT_TOP,
      "OFFER":OFFER % {"TOKKA":cfg.get("TOKKA_B","私大特化"),"CHECK1":cfg.get("CHECK1_B","私大専門で<b>7年</b>、出題傾向を分析し続けて作成"),"CHECK2":cfg["CHECK2"],"CHECK3":cfg["CHECK3"]},
      "LOGIC":B_LOGIC % {"TGB":"私大"},
      "REVEAL":B_REVEAL,
    }
    fn=os.path.join(OUT,lp+"-shindan.html")
    io.open(fn,"w",encoding="utf-8").write(html)
    files.append((lp,dname,"B"))

# index
rows=""
for lp,dname,grp in files:
    rows+='<li><span class="g g%s">%s</span><a href="./%s-shindan.html">%s</a><small>%s</small></li>\n'%(grp,grp,lp,lp,dname)
idx="""<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0"><title>診断プレビュー 全LP一覧</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
<style>
body{font-family:"Noto Sans JP",sans-serif;background:#efe9e3;padding:40px 20px;line-height:1.7;}
.w{max-width:720px;margin:0 auto;}
h1{font-size:22px;font-weight:900;margin-bottom:6px;}
p.lead{font-size:13px;color:#666;margin-bottom:24px;}
ul{list-style:none;background:#fff;border-radius:14px;padding:8px;box-shadow:0 10px 30px rgba(0,0,0,.07);}
li{display:flex;align-items:center;gap:12px;padding:13px 14px;border-bottom:1px solid #f0f0f0;}
li:last-child{border-bottom:none;}
a{font-weight:900;color:#722F37;text-decoration:none;font-size:15px;min-width:210px;}
a:hover{text-decoration:underline;}
small{color:#777;font-size:12.5px;}
.g{font-size:10px;font-weight:900;color:#fff;border-radius:4px;padding:3px 7px;}
.gA{background:#722F37;} .gB{background:#4a6b8a;}
</style></head><body><div class="w">
<h1>診断プレビュー 全LP一覧</h1>
<p class="lead">本番LPには未反映のプレビューです。<span style="color:#722F37;font-weight:900;">A＝合格可能性診断（4問）</span> / <span style="color:#4a6b8a;font-weight:900;">B＝塾タイプ診断（5問）</span></p>
<ul>
%s</ul></div></body></html>""" % rows
io.open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write(idx)

print("generated:",len(files),"files + index")
for f in files: print(" -",f[0],"(group",f[2]+")")

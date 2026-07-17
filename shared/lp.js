/* ============================================================
   FAST-UP LP 共通スクリプト（shared/lp.js）
   ------------------------------------------------------------
   デザインレイヤー（shared/design.css）とセットで読み込む。
   各LPは </body> 直前に <script src="../shared/lp.js"></script> を1行足すだけ。
   対象要素が無いLPでは各ブロックが何もせず終わる（querySelectorAll が空）。

   前提：<head> 内に次のインライン1行が必要（初回描画前に付けてちらつき防止）。
     if ('IntersectionObserver' in window) {
       document.documentElement.classList.add('js-reveal');
       document.documentElement.classList.add('js-bglazy');
     }
   ============================================================ */

/* アニメクラスの自動付与（<html data-anim="auto"> のLPのみ）：
   HTMLに .reveal 等を手打ちしなくても、共通語彙の要素へ自動で付ける。
   04a のように手動で付けたLPは data-anim を付けない＝この処理は動かない。
   手動クラスが既に付いた要素・FV内・アニメ管理する親の中はスキップする。 */
(function () {
  if (document.documentElement.getAttribute('data-anim') !== 'auto') return;
  /* 04a の手動配置と同じ型：グリッド/カード列はコンテナに stagger、
     単体要素は reveal。二重付与を避けるため stagger を先に付け、
     stagger の中の要素には reveal を付けない。 */
  var STAGGER = ['.empathy-grid', '.feature-sub-cards', '.calendar-compare'];
  var REVEAL = [
    '.section-title', '.quick-feature-card', '.case-card', '.trust-card',
    '.stat-item', '.add-service-card', '.faq-item',
    '.aha-lead', '.aha-lead-card', '.cta-wrap', '.cta-wrap-multi',
    '.ceo-message-compact', '.empathy-conclusion', '.check-table-conclusion',
    '.gift-banner', '.pay-support', '.pricing-detail', '.pricing-included-clean'
  ];
  var ANIM = ['reveal', 'reveal--stagger', 'slide-x', 'slide-x--stagger', 'wipe-in', 'focus-in', 'fv-anim'];
  function tag(selectors, cls) {
    document.querySelectorAll(selectors.join(', ')).forEach(function (el) {
      if (el.closest('.fv')) return;
      for (var i = 0; i < ANIM.length; i++) if (el.classList.contains(ANIM[i])) return;
      if (cls === 'reveal' && el.parentElement && el.parentElement.closest('.reveal--stagger, .slide-x--stagger')) return;
      el.classList.add(cls);
    });
  }
  tag(STAGGER, 'reveal--stagger');
  tag(REVEAL, 'reveal');
})();

/* 共通スクロールインアニメ：ビューポート進入時に .is-in を付与（1回のみ） */
(function () {
  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -22% 0px', threshold: 0.15 });
  document.querySelectorAll('.reveal, .reveal--stagger, .slide-x--stagger, .focus-in').forEach(function (el) { io.observe(el); });
  /* #extra（3つの仕組み）はTailwind由来のclassのため、構造セレクタで個別に監視 */
  document.querySelectorAll('#extra .text-olive-700, #extra .space-y-3, #extra .about3-ipad-pair, #extra .md\\:order-1').forEach(function (el) { io.observe(el); });
  /* ワイプ/横入り要素：FV内は読み込み時発火・stagger内は親の発火に任せるため、それ以外のみ個別監視 */
  document.querySelectorAll('.wipe-in, .slide-x').forEach(function (el) {
    if (!el.closest('.fv') && !el.closest('.reveal--stagger') && !el.closest('.slide-x--stagger')) io.observe(el);
  });
})();

/* FV内のアニメは常に最上部にあるため、IOに依存せず読み込み時に確実に再生（万一の非表示化を防止） */
(function () {
  var fv = document.querySelectorAll('.fv-anim, .fv .wipe-in, .fv-anim-sub, .fv-anim-stats, .fv-anim-cta, .fv-anim-notes');
  if (!fv.length) return;
  setTimeout(function () { fv.forEach(function (el) { el.classList.add('is-in'); }); }, 120);
})();

/* 数値カウントアップ（採用01：イーズアウト1.4s・ため付き・1回のみ）
   JS無効やreduced-motion時は静的な最終値のまま */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
  function fmt(n, el) {
    var s = n.toFixed(+(el.dataset.dec || 0));
    if (el.dataset.comma) { var p = s.split('.'); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ','); s = p.join('.'); }
    return (el.dataset.pre || '') + s;
  }
  window.__runCount = function (el) {
    if (el.__counted) return;
    el.__counted = true;
    var end = parseFloat(el.dataset.end), delay = +(el.dataset.delay || 0), dur = 1400, t0 = null;
    el.textContent = fmt(0, el);
    function tick(ts) {
      if (!t0) t0 = ts;
      var t = (ts - t0 - delay) / dur;
      if (t < 0) { requestAnimationFrame(tick); return; }
      if (t > 1) t = 1;
      el.textContent = fmt(end * ease(t), el);
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  };
  var cio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { window.__runCount(e.target); cio.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -22% 0px', threshold: 0.15 });
  document.querySelectorAll('.count-num').forEach(function (el) { cio.observe(el); });
})();

/* 背景写真の遅延読み込み：画面に近づいた .bg-lazy に .is-bg を付けて初めて写真を読む。
   400px 手前から読み始めるので、スクロールしても写真が遅れて現れることはない。 */
(function () {
  var els = document.querySelectorAll('.bg-lazy');
  if (!els.length) return;
  function show(el) { el.classList.add('is-bg'); }
  if (!('IntersectionObserver' in window)) { els.forEach(show); return; }
  var bio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { show(e.target); bio.unobserve(e.target); }
    });
  }, { rootMargin: '400px 0px', threshold: 0 });
  els.forEach(function (el) { bio.observe(el); });

  /* フェイルセーフ：IOが取りこぼしても、近づいた背景は必ず読み込む */
  var ticking = false;
  function sweep() {
    var vh = window.innerHeight;
    document.querySelectorAll('.bg-lazy:not(.is-bg)').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh + 400 && r.bottom > -400) show(el);
    });
    ticking = false;
  }
  function onScroll() { if (!ticking) { ticking = true; setTimeout(sweep, 200); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('load', function () { setTimeout(sweep, 800); });
})();

/* フェイルセーフ：IOが取りこぼしても、画面内に入った要素は必ず表示する（表示されないバグの根絶） */
(function () {
  var SEL = '.reveal:not(.is-in), .reveal--stagger:not(.is-in), .slide-x--stagger:not(.is-in), .focus-in:not(.is-in), .wipe-in:not(.is-in), .slide-x:not(.is-in),' +
    '#extra .text-olive-700:not(.is-in), #extra .space-y-3:not(.is-in), #extra .about3-ipad-pair:not(.is-in), #extra .md\\:order-1:not(.is-in)';
  var ticking = false;
  function sweep() {
    var vh = window.innerHeight;
    document.querySelectorAll(SEL).forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh * 0.92 && r.bottom > 0) el.classList.add('is-in');
    });
    if (window.__runCount) {
      document.querySelectorAll('.count-num').forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < vh * 0.92 && r.bottom > 0) window.__runCount(el);
      });
    }
    ticking = false;
  }
  function onScroll() { if (!ticking) { ticking = true; setTimeout(sweep, 200); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('load', function () { setTimeout(sweep, 800); });
})();

/* 下部スティッキーCTA：FVを過ぎたら表示、上部では非表示（スクロール連動） */
(function () {
  var el = document.querySelector('.sticky-cta');
  var fv = document.querySelector('.fv');
  if (!el || !fv) return;
  el.classList.add('sticky-cta--dynamic');
  var ticking = false;
  function update() {
    var trigger = fv.offsetTop + fv.offsetHeight - 80;
    el.classList.toggle('is-visible', window.pageYOffset > trigger);
    ticking = false;
  }
  function onScroll() {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', update);
  update();
})();

/**
 * FAST-UP LP共通：CTAパラメータ動的切替
 *
 * URLの ?from=g-{グループ番号} を読み取り、
 * 全CTAボタン（liff.line.me）の lp= 値を動的に切り替える。
 *
 * これにより1つのLPで14広告グループ別の流入経路識別が可能。
 *
 * lp値の発行はLSTEP管理画面で行い、下記マッピング表に反映する。
 * 山本さん作業：LSTEPで14個＋デフォルト1個 = 15個のlp値を発行 → このマップを更新
 */

(function () {
  // 14広告グループ → LSTEP流入経路ID（lp値）のマッピング
  // ※ 'XXXXXX' の部分はLSTEPで発行された実際のlp値に置き換える
  const LP_MAP = {
    'g-01':  'XXXXXX', // 指名_FAST-UP
    'g-02':  'XXXXXX', // 逆転合格
    'g-03':  'XXXXXX', // 浪人生
    'g-04a': 'XXXXXX', // 学習管理_自学自習
    'g-04b': 'XXXXXX', // オンライン塾
    'g-05':  'XXXXXX', // 早慶志望群
    'g-06':  'XXXXXX', // 早稲田志望
    'g-07':  'XXXXXX', // 慶應志望
    'g-08':  'XXXXXX', // GMARCH志望群
    'g-09':  'XXXXXX', // MARCH各校
    'g-10a': 'XXXXXX', // 塾比較・選び方
    'g-10b': 'XXXXXX', // 料金コスパ検討
    'g-11':  'XXXXXX', // 武田塾層
    'g-12':  'XXXXXX', // 関関同立志望
    'g-13':  'XXXXXX'  // 日東駒専志望
  };

  // パラメータ無し / 不正値時のフォールバック（既存LPの kanto と同じ値を仮置き）
  const DEFAULT_LP = '0Qzdig';

  function applyLpParam() {
    const params = new URLSearchParams(window.location.search);
    const fromKey = params.get('from');
    const lpValue = (fromKey && LP_MAP[fromKey]) || DEFAULT_LP;

    document.querySelectorAll('a[href*="liff.line.me"]').forEach(function (a) {
      a.href = a.href.replace(/lp=[^&]+/, 'lp=' + lpValue);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyLpParam);
  } else {
    applyLpParam();
  }

  // FAQ accordion
  document.addEventListener('click', function (e) {
    const q = e.target.closest('.faq-question');
    if (q) {
      q.parentElement.classList.toggle('open');
    }
  });

  // ハンバーガー・ドロワー開閉
  document.addEventListener('click', function (e) {
    const burger = e.target.closest('.header-burger');
    if (burger) {
      const open = document.body.classList.toggle('nav-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      return;
    }
    // オーバーレイ or ドロワー内リンクをタップしたら閉じる
    if (e.target.closest('.nav-overlay') || e.target.closest('.nav-drawer a')) {
      document.body.classList.remove('nav-open');
      const b = document.querySelector('.header-burger');
      if (b) b.setAttribute('aria-expanded', 'false');
    }
  });

  // Escでドロワーを閉じる
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('nav-open')) {
      document.body.classList.remove('nav-open');
      const b = document.querySelector('.header-burger');
      if (b) b.setAttribute('aria-expanded', 'false');
    }
  });
})();

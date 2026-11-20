/* Urantia America — 모든 하위 페이지 공용 「홈」 단추. 페이지 언어(html lang)에 맞춰 그 언어 첫 화면으로 간다.
   페이지 <head>에:  <script src="/home-button.js" defer></script>
   위치 바꾸기:      data-pos="left"(기본 right)   data-top="60"(위에서 px, 기본 10)
   머리 띠 안에 넣기: data-into="header" */
(function () {
  if (window.__urHomeBtn) return; window.__urHomeBtn = 1;
  var s = document.currentScript || document.querySelector('script[src*="home-button.js"]');
  var pos = (s && s.dataset.pos) === 'left' ? 'left' : 'right';
  var top = (s && s.dataset.top) || '10';
  var into = s && s.dataset.into;
  var LABEL = { en: 'Home', es: 'Inicio', fr: 'Accueil', pt: 'Início' };
  function add() {
    if (document.querySelector('.ur-home-btn')) return;
    var st = document.createElement('style');
    st.textContent =
      '.ur-home-btn{position:fixed;top:calc(env(safe-area-inset-top,0px) + ' + top + 'px);' + pos + ':10px;z-index:2147483000;' +
      'display:inline-flex;align-items:center;gap:4px;padding:6px 11px;border-radius:999px;' +
      'background:#ff5a1f;color:#fff!important;border:2px solid #fff;box-shadow:0 3px 10px rgba(0,0,0,.28);' +
      'font:700 12.5px/1.1 "Segoe UI",Roboto,system-ui,sans-serif;text-decoration:none!important;letter-spacing:0}' +
      '.ur-home-btn.inline{position:static;flex:0 0 auto;margin-right:6px;box-shadow:0 2px 6px rgba(0,0,0,.25)}' +
      '.ur-home-btn:hover{background:#e64a10}' +
      '.ur-home-btn:focus-visible{outline:3px solid #ffd23f;outline-offset:2px}' +
      '@media print{.ur-home-btn{display:none}}';
    document.head.appendChild(st);
    var lang = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
    if (!LABEL[lang]) lang = 'en';
    var a = document.createElement('a');
    a.href = '/' + lang + '/'; a.className = 'ur-home-btn'; a.title = LABEL[lang];
    a.setAttribute('aria-label', LABEL[lang]);
    a.textContent = '🏠 ' + LABEL[lang];
    var host = into && document.querySelector(into);
    if (host) { a.className += ' inline'; host.insertBefore(a, host.firstChild); }
    else document.body.appendChild(a);
  }
  if (document.body) add(); else document.addEventListener('DOMContentLoaded', add);
})();

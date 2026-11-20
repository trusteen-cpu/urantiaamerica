/* 바탕화면·홈 화면 앱용 서비스 워커 (Urantia America).
   첫 화면과 세 언어 본문 리더만 기기에 저장해 인터넷 없이도 연다.
   인터넷이 되면 늘 새 파일을 받아 저장본을 바꾸고, 안 될 때만 저장본을 쓴다. */
var CACHE = "uam-offline-v1";
var OFFLINE = [
  "/", "/en/", "/es/", "/fr/", "/pt/",
  "/es/book/", "/fr/book/", "/pt/book/", "/es/book/book.js", "/fr/book/book.js", "/pt/book/book.js",
  "/home.css", "/i18n.js", "/home-button.js", "/app.webmanifest",
  "/favicon.ico", "/apple-touch-icon.png", "/app-icon-192.png", "/app-icon-512.png"
];
var MSG = {
  en: "This page needs an internet connection.", es: "Esta página necesita conexión a internet.",
  fr: "Cette page nécessite une connexion internet.", pt: "Esta página precisa de conexão à internet."
};

self.addEventListener("install", function (e) {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function (c) {
    return Promise.all(OFFLINE.map(function (u) {
      return fetch(u, { cache: "reload" }).then(function (r) { if (r.ok) return c.put(u, r); }).catch(function () {});
    }));
  }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function offlinePage(path) {
  var m = /^\/(es|fr|pt)(\/|$)/.exec(path), l = m ? m[1] : "en";
  var body = "<h2>" + MSG[l] + "</h2><p><a href='/" + (l === "en" ? "en/" : l + "/book/") + "'>📖</a> · <a href='/" + l + "/'>🏠</a></p>";
  return new Response("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><body style='font:16px sans-serif;padding:24px;line-height:1.7'>" + body,
    { headers: { "Content-Type": "text/html; charset=utf-8" } });
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.origin !== location.origin) return;
  var saved = OFFLINE.indexOf(url.pathname) >= 0;
  if (req.mode !== "navigate" && !saved) return;
  e.respondWith(fetch(req).then(function (r) {
    if (saved && r.ok) {
      var copy = r.clone();
      e.waitUntil(caches.open(CACHE).then(function (c) { return c.put(url.pathname, copy); }));
    }
    return r;
  }).catch(function () {
    return caches.match(url.pathname).then(function (r) {
      return r || (req.mode === "navigate" ? offlinePage(url.pathname) : Response.error());
    });
  }));
});

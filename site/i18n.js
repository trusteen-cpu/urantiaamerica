/* Urantia America — 네 언어(영어·스페인어·프랑스어·포르투갈어) 글자 모음.
   메뉴 이름을 고치거나 늘릴 때는 이 파일만 고치면 됩니다.
   내용이 준비된 메뉴는 아래 links 에 언어별 주소를 적고, 없으면 '준비 중' 페이지로 갑니다. */
window.SITE = {
  langs: [
    { code: "en", label: "English" },
    { code: "es", label: "Español" },
    { code: "fr", label: "Français" },
    { code: "pt", label: "Português" }
  ],

  ui: {
    en: { brand: "Urantia Book Study Resources", tagline: "Urantia America",
          menu: "Menu", soon: "Coming soon", soonTitle: "This page is being prepared",
          soonBody: "The content will be added here soon. Thank you for your patience.",
          back: "Back to the menu", langLabel: "Language",
          byline: "Written & Edited by Jay Han",
          share: "🔗 Share link", copied: "Link copied — paste it into a message or chat.",
          install: "📲 Save to desktop", installed: "Already saved on this device.",
          iosHelp: "In Safari, tap the Share button (□↑) at the bottom, then choose “Add to Home Screen”.",
          otherHelp: "Open the browser menu (⋮ or …) and choose “Install app”, “Add to Home screen”, or “Create shortcut”." },
    es: { brand: "Recursos de Estudio de El libro de Urantia", tagline: "Urantia America",
          menu: "Menú", soon: "Próximamente", soonTitle: "Esta página está en preparación",
          soonBody: "Pronto añadiremos el contenido. Gracias por su paciencia.",
          back: "Volver al menú", langLabel: "Idioma",
          byline: "Redacción y edición: Jay Han",
          share: "🔗 Compartir enlace", copied: "Enlace copiado: péguelo en un mensaje o chat.",
          install: "📲 Guardar en el escritorio", installed: "Ya está guardado en este dispositivo.",
          iosHelp: "En Safari, toque el botón Compartir (□↑) abajo y elija «Añadir a pantalla de inicio».",
          otherHelp: "Abra el menú del navegador (⋮ o …) y elija «Instalar aplicación», «Añadir a pantalla de inicio» o «Crear acceso directo»." },
    fr: { brand: "Ressources d’étude du Livre d’Urantia", tagline: "Urantia America",
          menu: "Menu", soon: "Bientôt", soonTitle: "Cette page est en préparation",
          soonBody: "Le contenu sera bientôt ajouté. Merci de votre patience.",
          back: "Retour au menu", langLabel: "Langue",
          byline: "Rédaction et édition : Jay Han",
          share: "🔗 Partager le lien", copied: "Lien copié — collez-le dans un message.",
          install: "📲 Enregistrer sur le bureau", installed: "Déjà enregistré sur cet appareil.",
          iosHelp: "Dans Safari, touchez le bouton Partager (□↑) en bas, puis « Sur l’écran d’accueil ».",
          otherHelp: "Ouvrez le menu du navigateur (⋮ ou …) et choisissez « Installer l’application », « Ajouter à l’écran d’accueil » ou « Créer un raccourci »." },
    pt: { brand: "Recursos de Estudo de O Livro de Urântia", tagline: "Urantia America",
          menu: "Menu", soon: "Em breve", soonTitle: "Esta página está em preparação",
          soonBody: "O conteúdo será adicionado em breve. Obrigado pela paciência.",
          back: "Voltar ao menu", langLabel: "Idioma",
          byline: "Texto e edição: Jay Han",
          share: "🔗 Compartilhar link", copied: "Link copiado — cole-o numa mensagem ou conversa.",
          install: "📲 Salvar na área de trabalho", installed: "Já está salvo neste dispositivo.",
          iosHelp: "No Safari, toque no botão Compartilhar (□↑) embaixo e escolha “Adicionar à Tela de Início”.",
          otherHelp: "Abra o menu do navegador (⋮ ou …) e escolha “Instalar app”, “Adicionar à tela inicial” ou “Criar atalho”." }
  },

  menu: [
    { id: "text",       en: "The Urantia Book — Full Text",              es: "El libro de Urantia — Texto completo",            fr: "Le Livre d’Urantia — Texte intégral",             pt: "O Livro de Urântia — Texto integral" },
    { id: "bilingual",  en: "",                                           es: "Español / English — Texto paralelo",             fr: "Français / English — Texte parallèle",            pt: "Português / English — Texto paralelo", only: ["es", "fr", "pt"] },
    { id: "core",       en: "The Urantia Book Core — Digital Reader",    es: "Lo esencial de El libro de Urantia — Lector digital", fr: "L’essentiel du Livre d’Urantia — Liseuse numérique", pt: "O essencial de O Livro de Urântia — Leitor digital" },
    { id: "intro",      en: "Introduction to The Urantia Book",          es: "Introducción a El libro de Urantia",             fr: "Introduction au Livre d’Urantia",                 pt: "Introdução a O Livro de Urântia" },
    { id: "easy",       en: "Easy-Reading Commentary Edition",           es: "Edición comentada de lectura fácil",              fr: "Édition commentée facile à lire",                 pt: "Edição comentada de leitura fácil" },
    { id: "overview",   en: "A Conceptual Overview of The Urantia Book", es: "Panorama conceptual de El libro de Urantia",      fr: "Vue d’ensemble conceptuelle du Livre d’Urantia",  pt: "Panorama conceitual de O Livro de Urântia" },
    { id: "cosmology",  en: "Cosmology of The Urantia Book",             es: "Cosmología de El libro de Urantia",              fr: "Cosmologie du Livre d’Urantia",                   pt: "Cosmologia de O Livro de Urântia" },
    { id: "theology",   en: "Theology of The Urantia Book",              es: "Teología de El libro de Urantia",                fr: "Théologie du Livre d’Urantia",                    pt: "Teologia de O Livro de Urântia" },
    { id: "doctrine",   en: "Core Doctrines of The Urantia Book",        es: "Doctrinas centrales de El libro de Urantia",     fr: "Doctrines essentielles du Livre d’Urantia",       pt: "Doutrinas centrais de O Livro de Urântia" },
    { id: "jesus",      en: "Jesus Study",                               es: "Estudio sobre Jesús (Jesus Study)",              fr: "Étude sur Jésus (Jesus Study)",                   pt: "Estudo sobre Jesus (Jesus Study)" },
    { id: "personalities", en: "The Personalities of The Urantia Book",  es: "Las personalidades de El libro de Urantia",      fr: "Les personnalités du Livre d’Urantia",            pt: "As personalidades de O Livro de Urântia" },
    { id: "lists",      en: "376 Key Lists in The Urantia Book",         es: "376 listas clave de El libro de Urantia",        fr: "376 listes clés du Livre d’Urantia",              pt: "376 listas-chave de O Livro de Urântia" },
    { id: "chronology", en: "Urantia Book Chronology",                   es: "Cronología de El libro de Urantia",              fr: "Chronologie du Livre d’Urantia",                  pt: "Cronologia de O Livro de Urântia" },
    { id: "maps",       en: "Urantia Book Maps",                         es: "Mapas de El libro de Urantia",                   fr: "Cartes du Livre d’Urantia",                       pt: "Mapas de O Livro de Urântia" },
    { id: "youth",      en: "The Urantia Book for Young Readers",        es: "El libro de Urantia para jóvenes lectores",      fr: "Le Livre d’Urantia pour les jeunes lecteurs",     pt: "O Livro de Urântia para jovens leitores" },
    { id: "abridged",   en: "The Urantia Book, Abridged",                es: "El libro de Urantia abreviado",                  fr: "Le Livre d’Urantia abrégé",                       pt: "O Livro de Urântia resumido" },
    { id: "newcomer",   en: "12-Week Course for New Readers",            es: "Curso de 12 semanas para nuevos lectores",       fr: "Cours de 12 semaines pour nouveaux lecteurs",     pt: "Curso de 12 semanas para novos leitores" },
    { id: "commentary", en: "Paper-by-Paper Commentary",                 es: "Comentario documento por documento",             fr: "Commentaire fascicule par fascicule",             pt: "Comentário documento por documento" },
    { id: "qna",        en: "A Thousand Questions and Answers",          es: "Mil preguntas y respuestas",                     fr: "Mille questions et réponses",                     pt: "Mil perguntas e respostas" },
    { id: "topics",     en: "Topical Studies",                           es: "Estudios temáticos",                             fr: "Études thématiques",                              pt: "Estudos temáticos" },
    { id: "glossary",   en: "Urantia Book Glossary",                     es: "Glosario de El libro de Urantia",                fr: "Glossaire du Livre d’Urantia",                    pt: "Glossário de O Livro de Urântia" },
    { id: "reading",    en: "One-Year Reading of The Urantia Book",      es: "El libro de Urantia en un año",                  fr: "Le Livre d’Urantia en un an",                     pt: "O Livro de Urântia em um ano" },
    { id: "days365",    en: "365 Days with The Urantia Book",            es: "365 días con El libro de Urantia",               fr: "365 jours avec le Livre d’Urantia",               pt: "365 dias com O Livro de Urântia" },
    { id: "edu",        en: "English Study Resources",                   es: "English Study Resources (recursos en inglés)",   fr: "English Study Resources (ressources en anglais)", pt: "English Study Resources (recursos em inglês)" }
  ],

  /* 언어별 실제 주소. 여기에 없는 메뉴는 '준비 중'으로 갑니다.
     영어 메뉴는 극동판(fareast.urantiareaders.com)의 영어 페이지를 그대로 엽니다. */
  links: {
    en: {
      text: "https://fareast.urantiareaders.com/reader-en/", core: "https://fareast.urantiareaders.com/core-en/",
      intro: "https://fareast.urantiareaders.com/en/intro/", overview: "https://fareast.urantiareaders.com/en/overview/",
      newcomer: "https://fareast.urantiareaders.com/en/newcomer/", lists: "https://fareast.urantiareaders.com/en/lists/",
      chronology: "https://fareast.urantiareaders.com/en/chronology/", topics: "https://fareast.urantiareaders.com/en/topics/",
      qna: "https://fareast.urantiareaders.com/en/qna/", maps: "https://fareast.urantiareaders.com/en/maps/",
      youth: "https://fareast.urantiareaders.com/en/youth/", abridged: "https://fareast.urantiareaders.com/en/abridged/",
      commentary: "https://fareast.urantiareaders.com/en/commentary/", glossary: "https://fareast.urantiareaders.com/en/glossary/",
      theology: "https://fareast.urantiareaders.com/en/theology/", doctrine: "https://fareast.urantiareaders.com/en/doctrine/",
      personalities: "https://fareast.urantiareaders.com/en/personalities/", cosmology: "https://fareast.urantiareaders.com/en/cosmology/",
      easy: "https://fareast.urantiareaders.com/en/easy/", reading: "https://fareast.urantiareaders.com/reading/?lang=en",
      jesus: "https://fareast.urantiareaders.com/en/jesus/", days365: "https://fareast.urantiareaders.com/en/365days/",
      edu: "https://cozy-dragon-4626f0.netlify.app/"
    },
    es: { text: "es/book/", qna: "es/qna/", lists: "es/lists/", glossary: "es/glossary/", personalities: "es/personalities/", chronology: "es/chronology/", overview: "es/overview/", bilingual: "es/bilingual/", intro: "es/intro/", edu: "https://cozy-dragon-4626f0.netlify.app/" },
    fr: { text: "fr/book/", qna: "fr/qna/", lists: "fr/lists/", glossary: "fr/glossary/", personalities: "fr/personalities/", chronology: "fr/chronology/", overview: "fr/overview/", bilingual: "fr/bilingual/", intro: "fr/intro/", edu: "https://cozy-dragon-4626f0.netlify.app/" },
    pt: { text: "pt/book/", qna: "pt/qna/", lists: "pt/lists/", glossary: "pt/glossary/", personalities: "pt/personalities/", chronology: "pt/chronology/", overview: "pt/overview/", bilingual: "pt/bilingual/", intro: "pt/intro/", edu: "https://cozy-dragon-4626f0.netlify.app/" }
  }
};

/* 언어 고르기: 언어별 주소 → 주소의 ?lang= → 전에 고른 언어 → 브라우저 언어 → 영어 */
window.pickLang = function () {
  var codes = SITE.langs.map(function (l) { return l.code; });
  if (window.FORCE_LANG) return window.FORCE_LANG;
  var q = new URLSearchParams(location.search).get("lang");
  if (codes.indexOf(q) >= 0) return q;
  try { var s = localStorage.getItem("lang"); if (codes.indexOf(s) >= 0) return s; } catch (e) {}
  var n = (navigator.language || "en").slice(0, 2).toLowerCase();
  return codes.indexOf(n) >= 0 ? n : "en";
};
window.saveLang = function (code) {
  try { localStorage.setItem("lang", code); } catch (e) {}
  var u = new URL(location.href);
  u.searchParams.set("lang", code);
  history.replaceState(null, "", u);
};
window.HTML_LANG = { en: "en", es: "es", fr: "fr", pt: "pt" };

import "./App.css";

const SKILLSWAP_FEAT = [
  "Authentification complète (inscription, connexion, session).",
  "Profil utilisateur enrichi (avatar, bio, niveau, localisation, badge).",
  "Messagerie et notifications.",
  "Échanges de compétences (demandes, suivi, statuts).",
  "Feed communautaire avec priorisation visuelle Expert / Intermédiaire / Débutant.",
  "Recherche dynamique : compétence, domaine, utilisateur ; filtres et suggestions.",
  "Profils de démonstration auto-générés au démarrage du backend.",
];

const STACK_FRONT = ["React 19", "React Router", "Vite", "Tailwind CSS 4"];
const STACK_BACK = [
  "Node.js",
  "Express",
  "SQLite (better-sqlite3)",
  "JWT + bcryptjs",
  "Multer",
];

const VENTES_FEAT = [
  "Base relationnelle SQLite et données simulées cohérentes.",
  "Extraction et préparation avec Pandas.",
  "Indicateurs métier, visualisations Matplotlib et Seaborn.",
  "Exports CSV dans outputs/ et graphiques PNG dans outputs/figures/.",
  "Dashboard web principal (index.html) à servir en local.",
  "Interface Flask optionnelle : clients, achats, confirmations, listes mises à jour.",
  "Notebook Jupyter optionnel (dashboard.ipynb).",
  "Exports automatiques des KPI, plage de dates en CLI, contrôles qualité (assertions).",
];

const VENTES_STACK = [
  "Python",
  "SQLite",
  "Pandas",
  "Matplotlib",
  "Seaborn",
  "Flask (optionnel)",
  "Jupyter (optionnel)",
];

const ALPHA_SCOPE = [
  "Saisie dossier patient : identité, âge, sexe, date de prélèvement.",
  "Modules biochimie et hématologie (NFS) avec valeurs saisies, unités et observations.",
  "Compte rendu structuré : résultats, normes biologiques, interprétation, dates prélèvement / résultat.",
  "Mise en page alignée sur une fiche laboratoire (en-tête laboratoire, examens, techniques, signatures biologiste / responsable).",
];

const ALPHA_BIO_PARAMS: { param: string; unite: string }[] = [
  { param: "Glycémie (à jeun)", unite: "g/L" },
  { param: "Urémie", unite: "mg/dL" },
  { param: "Créatininémie", unite: "mg/dL" },
  { param: "ASAT (TGO)", unite: "UI/L" },
  { param: "ALAT (TGP)", unite: "UI/L" },
  { param: "Bilirubine totale", unite: "µmol/L" },
  { param: "Cholestérol total", unite: "g/L" },
  { param: "HDL-cholestérol", unite: "g/L" },
  { param: "LDL-cholestérol", unite: "g/L" },
  { param: "Triglycérides", unite: "g/L" },
];

const LARAVEL_LOGO =
  "https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg";

const LARAVEL_BADGES: { href: string; src: string; alt: string }[] = [
  {
    href: "https://github.com/laravel/framework/actions",
    src: "https://github.com/laravel/framework/workflows/tests/badge.svg",
    alt: "Build Status",
  },
  {
    href: "https://packagist.org/packages/laravel/framework",
    src: "https://img.shields.io/packagist/dt/laravel/framework",
    alt: "Total Downloads",
  },
  {
    href: "https://packagist.org/packages/laravel/framework",
    src: "https://img.shields.io/packagist/v/laravel/framework",
    alt: "Latest Stable Version",
  },
  {
    href: "https://packagist.org/packages/laravel/framework",
    src: "https://img.shields.io/packagist/l/laravel/framework",
    alt: "License",
  },
];

const LARAVEL_FEAT_LINKS: { label: string; href: string }[] = [
  { label: "Moteur de routage simple et rapide", href: "https://laravel.com/docs/routing" },
  { label: "Conteneur d’injection de dépendances", href: "https://laravel.com/docs/container" },
  { label: "Sessions (plusieurs pilotes de stockage)", href: "https://laravel.com/docs/session" },
  { label: "Cache (plusieurs pilotes de stockage)", href: "https://laravel.com/docs/cache" },
  { label: "ORM Eloquent", href: "https://laravel.com/docs/eloquent" },
  { label: "Migrations de schéma agnostiques du SGBD", href: "https://laravel.com/docs/migrations" },
  { label: "Traitement des tâches en arrière-plan (files d’attente)", href: "https://laravel.com/docs/queues" },
  { label: "Diffusion d’événements en temps réel (broadcasting)", href: "https://laravel.com/docs/broadcasting" },
];

const LARAVEL_LINKS: { href: string; label: string; hint: string }[] = [
  { href: "https://laravel.com/docs", label: "Documentation", hint: "guides détaillés" },
  { href: "https://laravel.com/learn", label: "Laravel Learn", hint: "parcours guidé" },
  { href: "https://laracasts.com", label: "Laracasts", hint: "vidéos Laravel, PHP, tests, JS" },
];

const LARAVEL_SPONSORS: { name: string; href: string }[] = [
  { name: "Vehikl", href: "https://vehikl.com" },
  { name: "Tighten Co.", href: "https://tighten.co" },
  { name: "Kirschbaum Development Group", href: "https://kirschbaumdevelopment.com" },
  { name: "64 Robots", href: "https://64robots.com" },
  { name: "Curotec", href: "https://www.curotec.com/services/technologies/laravel" },
  { name: "DevSquad", href: "https://devsquad.com/hire-laravel-developers" },
  { name: "Redberry", href: "https://redberry.international/laravel-development" },
  { name: "Active Logic", href: "https://activelogic.com" },
];

/** Affiché en tête de page — à ajuster si besoin. */
const AUTHOR_DISPLAY_NAME = "KETEMEPI Fidella Maeva";

export default function App() {
  return (
    <div className="page">
      <header className="header">
        <div className="header__inner">
          <a className="logo" href="#">
            <span className="logo__brand">{AUTHOR_DISPLAY_NAME}</span>
            <span className="logo__suffix">Portfolio</span>
          </a>
          <nav className="nav">
            <a href="#skillswap">SkillSwap</a>
            <a href="#analyse-ventes">Analyse des ventes</a>
            <a href="#alpha-lab">ALPHA_LAB</a>
            <a href="#laravel">Laravel</a>
          </nav>
        </div>
      </header>

      <main>
        <section className="hero">
          <p className="hero__eyebrow">Projets</p>
          <h1 className="hero__name">{AUTHOR_DISPLAY_NAME}</h1>
          <p className="hero__strapline">
            Web, <em>données</em> et <em>santé</em>
          </p>
          <p className="hero__lead">
            SkillSwap (full-stack), TP analyse des ventes (Python / SQLite),
            cadrage ALPHA_LAB (santé), et <strong>Laravel</strong> côté PHP pour des
            applications web robustes — selon la documentation officielle du
            framework.
          </p>
          <div className="hero__actions hero__actions--row">
            <a className="btn btn--primary" href="#skillswap">
              SkillSwap
            </a>
            <a className="btn btn--ghost" href="#analyse-ventes">
              Analyse des ventes
            </a>
            <a className="btn btn--ghost" href="#alpha-lab">
              ALPHA_LAB
            </a>
            <a className="btn btn--ghost" href="#laravel">
              Laravel
            </a>
          </div>
          <p className="hero__hint mono">
            React · Express · Python · Pandas · SQLite · PHP · Laravel
          </p>
        </section>

        <section id="skillswap" className="section project">
          <div className="section__head">
            <p className="project__label">Application web</p>
            <h2 className="section__title">SkillSwap</h2>
            <p className="section__subtitle">
              Plateforme d&apos;échange de compétences entre particuliers et
              professionnels — profils complémentaires pour apprendre et
              collaborer.
            </p>
          </div>

          <div className="project__grid">
            <article className="card card--main">
              <h3 className="card__title">Fonctionnalités principales</h3>
              <ul className="feat-list">
                {SKILLSWAP_FEAT.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </article>

            <aside className="card card--aside">
              <h3 className="card__title">Structure</h3>
              <pre className="tree mono">
                {`SkillSwap/
  backend/    # API Express + SQLite
  frontend/   # React / Vite`}
              </pre>
              <p className="card__note">
                Prérequis : Node.js 20+ (recommandé), npm 10+.
              </p>
            </aside>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Stack technique</h3>
            <div className="stack__cols">
              <div className="card stack__card">
                <h4 className="card__title">Frontend</h4>
                <ul className="tags">
                  {STACK_FRONT.map((t) => (
                    <li key={t}>{t}</li>
                  ))}
                </ul>
              </div>
              <div className="card stack__card">
                <h4 className="card__title">Backend</h4>
                <ul className="tags">
                  {STACK_BACK.map((t) => (
                    <li key={t}>{t}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Installation &amp; développement</h3>
            <div className="card dev__card">
              <p className="dev__intro">
                Copier <span className="mono">backend/.env.example</span> vers{" "}
                <span className="mono">backend/.env</span> (JWT, PORT, etc.).
                Optionnel : <span className="mono">frontend/.env</span> pour le
                proxy de dev.
              </p>
              <div className="blocks">
                <div>
                  <p className="blocks__label mono">Installation</p>
                  <pre className="blocks__code mono">
                    {`npm install --prefix backend
npm install --prefix frontend`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Deux terminaux</p>
                  <pre className="blocks__code mono">
                    {`npm run dev:backend
npm run dev:frontend`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Build production</p>
                  <pre className="blocks__code mono">
                    {`npm run build:frontend
npm run start:backend`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Qualité</p>
                  <pre className="blocks__code mono">{`npm run lint:frontend`}</pre>
                </div>
              </div>
            </div>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Déploiement</h3>
            <ul className="deploy__list">
              <li>Frontend : build statique dans <span className="mono">frontend/dist</span>.</li>
              <li>Backend : API configurable par variables d&apos;environnement.</li>
              <li>
                SQLite locale, chemin via <span className="mono">SQLITE_PATH</span>.
              </li>
              <li>
                <span className="mono">VITE_DEV_PROXY_TARGET</span>,{" "}
                <span className="mono">VITE_API_URL</span> (prod).
              </li>
            </ul>
            <p className="roadmap">
              <strong>Roadmap :</strong> captures et GIF dans le README, pipeline CI,
              déploiement cloud documenté.
            </p>
          </div>
        </section>

        <section id="analyse-ventes" className="section project section--sep">
          <div className="section__head">
            <p className="project__label">Data &amp; Python</p>
            <h2 className="section__title">TP Analyse des ventes</h2>
            <p className="section__subtitle">
              TP complet : base SQLite, données simulées, Pandas, indicateurs,
              graphiques, exports CSV, dashboard web et saisie Flask optionnelle.
            </p>
          </div>

          <div className="project__grid">
            <article className="card card--main">
              <h3 className="card__title">Contenu du pipeline</h3>
              <ul className="feat-list">
                {VENTES_FEAT.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </article>

            <aside className="card card--aside">
              <h3 className="card__title">Structure</h3>
              <pre className="tree mono">
                {`src/main.py           # point d'entrée
src/db_setup.py       # schéma SQLite + données
src/analyse_ventes.py # KPI, figures, exports
src/web_app.py        # Flask (optionnel)
data/ventes_magasin.db
outputs/              # CSV
outputs/figures/      # PNG
dashboard.ipynb       # notebook (optionnel)`}
              </pre>
            </aside>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Stack &amp; outils</h3>
            <div className="card stack__card stack__card--wide">
              <ul className="tags">
                {VENTES_STACK.map((t) => (
                  <li key={t}>{t}</li>
                ))}
              </ul>
            </div>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Commandes</h3>
            <div className="card dev__card">
              <div className="blocks">
                <div>
                  <p className="blocks__label mono">Installation</p>
                  <pre className="blocks__code mono">{`pip install -r requirements.txt`}</pre>
                </div>
                <div>
                  <p className="blocks__label mono">Pipeline données</p>
                  <pre className="blocks__code mono">{`python src/main.py`}</pre>
                </div>
                <div>
                  <p className="blocks__label mono">Dashboard web (serveur local)</p>
                  <pre className="blocks__code mono">
                    {`python -m http.server 8000
# puis http://127.0.0.1:8000/index.html`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Flask (saisie optionnelle)</p>
                  <pre className="blocks__code mono">
                    {`python src/web_app.py
# http://127.0.0.1:5000`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Notebook (optionnel)</p>
                  <pre className="blocks__code mono">
                    {`jupyter notebook
# ouvrir dashboard.ipynb`}
                  </pre>
                </div>
                <div>
                  <p className="blocks__label mono">Plage de dates</p>
                  <pre className="blocks__code mono">
                    {`python src/main.py --date-debut 2025-03-01 --date-fin 2025-06-30`}
                  </pre>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section id="alpha-lab" className="section project section--sep">
          <div className="section__head">
            <span className="badge badge--planned">Projet à venir</span>
            <p className="project__label">Santé · Laboratoire</p>
            <h2 className="section__title">ALPHA_LAB — gestion des analyses médicales</h2>
            <p className="section__subtitle">
              Application envisagée pour le laboratoire d&apos;analyses médicales et
              biologiques <strong>ALPHA_LAB</strong> : saisie patient, résultats
              biochimie / hématologie et compte rendu professionnel. Le développement
              n&apos;a pas encore démarré ; cette section fixe le cadrage métier.
            </p>
          </div>

          <div className="project__grid">
            <article className="card card--main">
              <h3 className="card__title">Périmètre fonctionnel (cadrage)</h3>
              <ul className="feat-list">
                {ALPHA_SCOPE.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
              <p className="card__note">
                Hématologie : numération et formule sanguine (tableau résultats /
                normes / interprétation, comme la biochimie). Détails des lignes NFS
                à préciser au même titre que les automates du laboratoire.
              </p>
            </article>

            <aside className="card card--aside">
              <h3 className="card__title">Laboratoire (référence métier)</h3>
              <p className="lab-card">
                <strong>ALPHA_LAB</strong>
                <br />
                Lomé, Togo — près de la Caisse Nationale de Sécurité Sociale.
                <br />
                <a href="tel:+22899889929">+228 99 88 99 29</a>
                <br />
                <br />
                Examens ciblés : <strong>biochimie médicale</strong> et{" "}
                <strong>hématologie</strong>.
                <br />
                Techniques : spectrophotométrie sur automate{" "}
                <strong>BIOBASE</strong>, automate <strong>hématologique</strong>.
              </p>
            </aside>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">
              Paramètres biochimiques prévus (saisie valeur + unité)
            </h3>
            <div className="param-table-wrap">
              <table className="param-table">
                <thead>
                  <tr>
                    <th scope="col">Paramètre</th>
                    <th scope="col">Unité</th>
                  </tr>
                </thead>
                <tbody>
                  {ALPHA_BIO_PARAMS.map((row) => (
                    <tr key={row.param}>
                      <td>{row.param}</td>
                      <td>{row.unite}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Prochaines étapes (suggestion)</h3>
            <p className="roadmap">
              <strong>Quand le projet démarrera :</strong> choisir la stack (ex. app
              web + API + base de données), modèle de données patients / prélèvements /
              résultats, génération PDF ou fiche imprimable, règles de validation et
              traçabilité conformes aux usages du laboratoire. Aucun dépôt ni code
              pour l&apos;instant — remplacer ce bloc par liens et captures une fois
              l&apos;implémentation entamée.
            </p>
          </div>
        </section>

        <section id="laravel" className="section project section--sep">
          <div className="laravel-brand card">
            <a
              className="laravel-brand__logo-link"
              href="https://laravel.com"
              target="_blank"
              rel="noreferrer"
            >
              <img
                className="laravel-brand__logo"
                src={LARAVEL_LOGO}
                width={400}
                alt="Laravel"
              />
            </a>
            <ul className="laravel-badges">
              {LARAVEL_BADGES.map((b) => (
                <li key={b.src} className="laravel-badges__item">
                  <a
                    className="laravel-badges__link"
                    href={b.href}
                    target="_blank"
                    rel="noreferrer"
                  >
                    <img src={b.src} alt={b.alt} loading="lazy" />
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div className="section__head section__head--tight">
            <p className="project__label">PHP · Framework</p>
            <h2 className="section__title">Laravel</h2>
            <p className="section__subtitle">
              Framework web PHP à syntaxe expressive. Laravel vise à rendre le
              développement agréable en facilitant les tâches courantes (routage,
              persistance, files d’attente, etc.), pour des applications accessibles
              et solides — d’après la présentation du{" "}
              <a href="https://github.com/laravel/laravel" target="_blank" rel="noreferrer">
                README officiel
              </a>
              . Complétez cette section par votre propre projet quand il sera prêt.
            </p>
          </div>

          <div className="project__grid">
            <article className="card card--main">
              <h3 className="card__title">Fonctionnalités (liens documentation)</h3>
              <ul className="feat-list feat-list--links">
                {LARAVEL_FEAT_LINKS.map((item) => (
                  <li key={item.href}>
                    <a href={item.href} target="_blank" rel="noreferrer">
                      {item.label}
                    </a>
                  </li>
                ))}
              </ul>
              <p className="card__note">
                Licence :{" "}
                <a
                  href="https://opensource.org/licenses/MIT"
                  target="_blank"
                  rel="noreferrer"
                >
                  MIT
                </a>
                .
              </p>
            </article>

            <aside className="card card--aside">
              <h3 className="card__title">Apprentissage</h3>
              <p className="card__blurb">
                La documentation officielle est très fournie ;{" "}
                <strong>Laravel Learn</strong> propose un parcours guidé pour
                construire une application moderne. <strong>Laracasts</strong> offre
                des milliers de tutoriels vidéo (Laravel, PHP moderne, tests,
                JavaScript).
              </p>
              <ul className="resource-list">
                {LARAVEL_LINKS.map((link) => (
                  <li key={link.href}>
                    <a href={link.href} target="_blank" rel="noreferrer">
                      {link.label}
                    </a>
                    <span className="resource-list__hint"> — {link.hint}</span>
                  </li>
                ))}
              </ul>
            </aside>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Sponsors — partenaires premium</h3>
            <p className="subsection__lead">
              Le README remercie les sponsors du framework. Devenir sponsor :{" "}
              <a href="https://partners.laravel.com" target="_blank" rel="noreferrer">
                Laravel Partners
              </a>
              .
            </p>
            <ul className="tags tags--sponsors">
              {LARAVEL_SPONSORS.map((s) => (
                <li key={s.href}>
                  <a href={s.href} target="_blank" rel="noreferrer">
                    {s.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div className="subsection">
            <h3 className="subsection__title">Communauté, sécurité, licence</h3>
            <div className="card dev__card laravel-meta">
              <ul className="feat-list">
                <li>
                  <strong>Contribution :</strong>{" "}
                  <a
                    href="https://laravel.com/docs/contributions"
                    target="_blank"
                    rel="noreferrer"
                  >
                    guide dans la documentation
                  </a>
                  .
                </li>
                <li>
                  <strong>Code de conduite :</strong>{" "}
                  <a
                    href="https://laravel.com/docs/contributions#code-of-conduct"
                    target="_blank"
                    rel="noreferrer"
                  >
                    voir la doc Laravel
                  </a>
                  .
                </li>
                <li>
                  <strong>Vulnérabilités :</strong> les signaler par e-mail à Taylor
                  Otwell :{" "}
                  <a href="mailto:taylor@laravel.com">taylor@laravel.com</a> (selon le
                  README officiel du framework).
                </li>
              </ul>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>
          <strong className="footer__author">{AUTHOR_DISPLAY_NAME}</strong> — Portfolio
          (SkillSwap, analyse des ventes, ALPHA_LAB, Laravel). Liens GitHub et
          captures au fil de l&apos;avancement.
        </p>
      </footer>
    </div>
  );
}

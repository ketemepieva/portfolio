# Portfolio

Site statique (React + Vite + TypeScript) présentant les projets SkillSwap, analyse des ventes, ALPHA_LAB et Laravel.

## Développement local

Avec `base: "/portfolio/"`, ouvrez l’URL affichée par Vite, en général :

**http://localhost:5173/portfolio/**

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

Les fichiers générés sont dans `dist/`.

## GitHub Pages

Le dépôt est configuré avec `base: /portfolio/` et un workflow GitHub Actions qui publie le dossier **`dist/`** (build Vite), pas les sources.

### Mise en place (obligatoire)

1. Sur GitHub : **Settings → Pages**.
2. **Build and deployment → Source** : choisir **GitHub Actions**.
3. Si **« Deploy from a branch »** est encore actif (branche `main`, dossier `/`), **désactivez-le** ou basculez sur Actions : sinon Pages sert le `index.html` **source** qui pointe vers `/src/main.tsx` → erreur MIME / page blanche dans la console.

4. Onglet **Actions** : vérifiez que le workflow **Deploy GitHub Pages** est vert. Sinon, ouvrez le run en échec et lisez les logs.

5. URL du site (dépôt nommé `portfolio`) :  
   **https://ketemepieva.github.io/portfolio/**  

   Ce n’est **pas** `https://ketemepieva.github.io/` seul (cela correspond au dépôt spécial `username.github.io`, autre projet).

### Dépannage : erreur « main.tsx » / type MIME `text/html`

Cela signifie que le navigateur charge encore les **sources** au lieu du build. Corrigez la source Pages (**GitHub Actions**) comme ci-dessus, puis relancez le workflow (**Actions → Deploy GitHub Pages → Re-run all jobs**).

## CV PDF (mise à jour)

Prérequis Python : `pip install reportlab pillow`, puis :

```bash
npm run cv:pdf
```

Le fichier `public/CV_Fidella_Maeva_Ketemepi_professionnel.pdf` est régénéré (photo `public/cv-photo.png`). Le script tente aussi de copier le PDF vers le dossier Cursor d’origine si accessible.

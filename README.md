# Portfolio

Site statique (React + Vite + TypeScript) présentant les projets SkillSwap, analyse des ventes, ALPHA_LAB et Laravel.

## Développement local

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

Le dépôt est configuré avec `base: /portfolio/` et un workflow GitHub Actions qui publie le build sur Pages après chaque push sur `main`.

1. Sur GitHub : **Settings → Pages** : source **GitHub Actions** (pas « Deploy from a branch »).
2. Après le premier workflow réussi, le site est disponible à  
   `https://ketemepieva.github.io/portfolio/`

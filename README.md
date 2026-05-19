# CozyCanvas AI Landing Page

A whimsical animated landing page for a cozy AI creative studio that makes storybook posters, cute science art, and animated explainers.

## Stack

- [Vite](https://vite.dev/) for the frontend build tool
- [React](https://react.dev/) for UI components
- [Tailwind CSS](https://tailwindcss.com/) for styling
- [Motion](https://motion.dev/) for lightweight animation

## Setup instructions

Install dependencies:

```bash
npm install
```

Start the local development server:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Project structure

```text
src/main.jsx     Main React landing page components and Motion animations
src/styles.css   Tailwind entrypoint plus custom blob, sparkle, and accessibility styles
```

## Notes

- The page is mobile-first and sized for small screens including iPhone widths.
- Animations are intentionally gentle and use `prefers-reduced-motion` fallbacks.
- No backend is required.

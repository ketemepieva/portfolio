import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  // Dépôt GitHub : ketemepieva/portfolio → https://ketemepieva.github.io/portfolio/
  base: "/portfolio/",
});

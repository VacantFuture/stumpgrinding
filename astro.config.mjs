// @ts-check
import { defineConfig } from 'astro/config';

import svelte from '@astrojs/svelte';
import iconset from 'astro-iconset';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  integrations: [
    svelte(),
    iconset({
      include: {
        'mdi': ['*'],
        'material-symbols': ['*'],
      },
    }),
  ],

  vite: {
    plugins: [tailwindcss()]
  }
});

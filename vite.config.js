import { sveltekit } from '@sveltejs/kit/vite';
import viteCompression from 'vite-plugin-compression';

export default {
  plugins: [
    sveltekit(),
    viteCompression({
      algorithm: 'gzip',
      ext: '.gz',
      threshold: 10240,
      deleteOriginFile: false,
      filter: /\.(js|css|html|json|svg|xml|wasm)$/i
    })
  ],
  build: {
    sourcemap: true
  },
  server: {
    sourcemap: true
  }
};

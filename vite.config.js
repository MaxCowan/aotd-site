import { sveltekit } from '@sveltejs/kit/vite';
import viteCompression from 'vite-plugin-compression';

export default {
  plugins: [
    sveltekit(),
    viteCompression({
      algorithm: 'gzip',
      ext: '.gz', // Use .gz extension
      threshold: 10240, // Compress files larger than 10KB
      deleteOriginFile: false, // Keep original files
      filter: /\.(js|css|html|json|svg|xml|wasm)$/i // Apply compression to JSON and other file types
    })
  ]
};

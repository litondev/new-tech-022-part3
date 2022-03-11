import { fileURLToPath, URL } from 'url'

import { defineConfig,loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import EnvironmentPlugin from 'vite-plugin-environment'

// https://vitejs.dev/config/
export default  ({ mode }) => {
  process.env = {...process.env, ...loadEnv(mode, process.cwd())};

  return defineConfig({
    plugins: [
      EnvironmentPlugin('all',{prefix: 'VUE_APP_'}),
      vue()
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  })
}
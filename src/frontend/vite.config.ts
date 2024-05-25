import { defineConfig } from 'vite'

const pages = {
  main: './index.html',
  auth: './auth.html',
  login: './auth/login.html',
  signup: './auth/signup.html',
  signup_code: './auth/signup/code.html',
  signup_profile: './auth/signup/profile.html'
}

export default defineConfig({
  build: {
    target: 'es2017',
    outDir: 'build',
    rollupOptions: {
      input: pages
    }
  }
})
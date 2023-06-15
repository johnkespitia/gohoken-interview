import { defineConfig } from 'cypress'

export default defineConfig({
    e2e: {
        baseUrl: 'http://gohoken-interview-front-app-1:3000',
        supportFile: false,
        specPattern: "**/e2e/integration/*.spec.ts",
    },
})
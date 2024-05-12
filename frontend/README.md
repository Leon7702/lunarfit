# Lunarfit (Working Title?) Webapp

This is what you get when following
https://vuejs.org/guide/quick-start.html using node, with the options
ESLint and Prettier. Feel free to replace it with the frontend setup you
actually use.

## Communicating with the backend

See the top-level readme, on how to start the backend server and database (`docker compose up backend`).

Currently there is just a small fetch request in the `src/App.vue` that fetches the API root and logs the response to the console.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

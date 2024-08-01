#!/usr/bin/env sh

# check for new dependencies
npm install

# bundle static files into ./dist/spa
npm run build

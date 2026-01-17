# Coding Algo Notes

This is a Hugo website with the Hextra theme containing my personal algorithm notes.

## Setup

1. Install Hugo (if not already installed):
   ```bash
   # On Ubuntu/Debian
   sudo apt update && sudo apt install hugo

   # Or download from https://gohugo.io/getting-started/installing/
   ```

2. Add the Hextra theme:
   ```bash
   git submodule add https://github.com/imfing/hextra.git themes/hextra
   ```

3. Build the site:
   ```bash
   hugo
   ```

4. Serve locally:
   ```bash
   hugo server
   ```

The site will be available at `http://localhost:1313`

## Content

- Home page: Introduction
- Dijkstra Algorithm: Complete notes on Dijkstra's algorithm

## Deployment

You can deploy this to Vercel, Netlify, or any static site host.

For Vercel:
- Connect your GitHub repo
- Set build command: `hugo`
- Set output directory: `public`
# Love Collection flipbook

- Add/replace images in `pages/` (named 01-..., 02-... in order), edit story text in `captions.json`.
- Run `python3 build.py` (Cloudflare Pages does this for you).

## Cloudflare Pages setup (once)
1. Push this folder to a GitHub repo.
2. Cloudflare > Workers & Pages > Create > Pages > Connect to Git > pick the repo.
3. Build command: `python3 build.py`   Build output directory: `/` (leave root)
After that, every push to GitHub republishes the flipbook.

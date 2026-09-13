# Tesla Firmware Jail Watch

A cartoon GitHub Pages dashboard for TeslaFi firmware `2026.20.300`.

## Deploy
1. Put these files in a GitHub repository, preserving `.github/workflows/update.yml`.
2. In **Settings → Pages**, set **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. In **Settings → Actions → General → Workflow permissions**, allow **Read and write permissions** if your repository does not already allow the workflow to commit `data.json`.
4. Run **Actions → Refresh TeslaFi data → Run workflow** once.

The GitHub Action runs every 30 minutes, fetches the public TeslaFi detail page, parses current installs and next-version counts, writes `data.json`, and commits changes. The browser animation reads `data.json`; it does not scrape TeslaFi directly, avoiding browser CORS issues.

This is an unofficial fan project and is not affiliated with Tesla or TeslaFi. Be considerate of TeslaFi's service and terms; the schedule performs only one request every 30 minutes.

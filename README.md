# Carwebsite-

Apex Motors — a static car dealership site (no build step, no dependencies).

## Structure

```
public/
  index.html   markup
  styles.css   styles
  script.js    inventory filtering + lead form
vercel.json    Vercel config (static, cleanUrls)
```

## Local preview

```bash
python3 -m http.server 8000 --directory public
# http://localhost:8000
```

## Deploy

Deployed on Vercel as a static site. `public/` is the output directory; there is
no build command.

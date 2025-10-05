
# Makralkaza IT Templates — Blog Site

A GitHub Pages + Jekyll site with scheduled automation to publish posts and generate new ones from `data/post_ideas.csv`.

## How to Use
1. Create a **new GitHub repository** (public) named `makralkaza-tools` (or any name).
2. Upload the contents of this folder to the repo root.
3. Go to **Settings → Pages → Build and deployment** and set **Source = GitHub Actions**.
4. Go to **Actions** tab and run **Build and Deploy (Jekyll)** once.
5. Edit `data/post_ideas.csv` to queue more articles; the workflow will generate posts on weekdays at 13:00 UTC.


import csv, os, datetime, pathlib

date_today = datetime.date.today().isoformat()
ideas_csv = "data/post_ideas.csv"  # columns: title, slug, keywords, outline, cta_url
posts_dir = pathlib.Path("_posts")
posts_dir.mkdir(parents=True, exist_ok=True)

def md(title, date, tags, body):
    fm = f"---
layout: post
title: "{title}"
date: {date}
tags: [{', '.join(tags)}]
---

"
    return fm + body

with open(ideas_csv, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        slug = row['slug']
        date = date_today
        fname = posts_dir / f"{date}-{slug}.md"
        if fname.exists():
            continue
        body = f"## What this solves

{row['outline']}

"
        body += "## Download the free template
"
        body += f"[Get it here]({row['cta_url']})

"
        body += "## How to customize

- Add your assets in the Sheet
- Use conditional formatting to spot risks
- Set reminder emails via Power Automate
"
        tags = [t.strip() for t in row['keywords'].split(',') if t.strip()]
        with open(fname, "w", encoding="utf-8") as out:
            out.write(md(row['title'], date, tags, body))

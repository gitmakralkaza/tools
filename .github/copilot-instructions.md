<!-- Copilot instructions for the repository: concise, actionable, and specific to this Jekyll blog + small Python helper script -->
# Copilot instructions — Makralkaza IT Templates

This repository is a small Jekyll-based blog (GitHub Pages) that publishes template-driven posts. Use these notes to quickly become productive when suggesting edits, generating content, or automating changes.

- Project type: Jekyll site using the `minima` theme (see `_config.yml`). Files are plain HTML/layouts plus Markdown posts in `_posts/`.
- Build/preview: site is intended for GitHub Pages. No Node/npm build. Local preview can be done with `jekyll serve` if the developer has Jekyll installed; otherwise target changes to be GitHub Pages compatible (Liquid templates, relative_url filters).

Key files and patterns to reference when editing or generating content

- `_config.yml` — site metadata and plugins (jekyll-feed, jekyll-sitemap). Use site variables like `{{ site.title }}` and `{{ site.description }}`.
- `_layouts/default.html` — global HTML shell (Bootstrap 5 CSS + Google Font). Put page content inside the layout's `{{ content }}` slot.
- `_posts/YYYY-MM-DD-slug.md` — blog posts. Posts use YAML front matter like:

  ---
  layout: post
  title: "My Title"
  date: 2025-10-09
  tags: [tag1, tag2]
  ---

- `index.html` — homepage that lists recent posts via `site.posts` and uses `post.excerpt`.

Automated content generator

- `scripts/generate_posts.py` reads `data/post_ideas.csv` (columns: title, slug, keywords, outline, cta_url) and emits new files into `_posts/` named `YYYY-MM-DD-{slug}.md`.
- When creating or editing posts programmatically, follow the same front matter and use `slug` values that are filesystem-safe (lowercase, hyphens, no spaces). The script splits `keywords` into `tags`.

Conventions and code patterns Copilot should follow

- HTML templates use Liquid tags (e.g., `{{ post.title }}`, `{% for post in site.posts %}`). Avoid replacing Liquid logic with static content unless the change is deliberate.
- Assets: images live under `assets/images/`. Use `{{ '/assets/images/filename.png' | relative_url }}` in layouts.
- Keep all Bootstrap and external assets referenced via CDN as the code does now; do not inline or alter to local copies without coordinating with the maintainer.
- Posts: prefer small, structured sections (see generator output) — headings: "What this solves", "Download the free template", "How to customize".

Developer workflows and commands

- To preview locally (developer must have Ruby + Jekyll):
  - Install Jekyll: `gem install bundler jekyll`
  - Run: `jekyll serve --livereload`
  If Jekyll is not available, changes can be validated by inspecting the generated HTML in `_site/` on a machine that builds it.
- To add posts in bulk, edit `data/post_ideas.csv` and run `python scripts/generate_posts.py` (uses default Python on system). The script will skip existing filenames.

What to avoid

- Don't change the `_config.yml` theme/plugin choices unless required — changes affect GitHub Pages rendering.
- Don't remove Liquid filters like `relative_url` or calls to `site.*` variables — these keep the site portable across `baseurl`/`url` configurations.

Searchable anchors for Copilot suggestions

- Look at `_layouts/default.html` for layout conventions and navbar entries.
- Look at `scripts/generate_posts.py` and `data/post_ideas.csv` for content generation patterns.
- Look at `_posts/` for real examples of filenames and front matter.

If you need more context

- Ask to inspect a specific file or the current `_posts/` front matter examples. When suggesting changes that affect build/hosting (e.g., plugin changes or baseurl), include a concise rationale and a step-by-step migration plan.

End of file.
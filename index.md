---
layout: default
title: Makralkaza IT Templates
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ site.title }}</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    header { background: linear-gradient(135deg, #0d6efd, #0a58ca); }
    .card:hover { transform: translateY(-5px); transition: 0.3s; }
  </style>
</head>
<body>

  <!-- Hero Section -->
  <header class="text-white text-center py-5">
    <div class="container">
      <h1 class="display-4 fw-bold">{{ site.title }}</h1>
      <p class="lead">{{ site.description }}</p>
      <a href="#posts" class="btn btn-light btn-lg mt-3">Explore Templates</a>
    </div>
  </header>

  <!-- Posts Section -->
  <section id="posts" class="py-5">
    <div class="container">
      <div class="row g-4">

        {% for post in site.posts limit:6 %}
        <div class="col-md-4">
          <div class="card shadow-sm h-100">
            <div class="card-body">
              <h5 class="card-title">{{ post.title }}</h5>
              <p class="card-text">{{ post.excerpt | strip_html | truncate: 120 }}</p>
              <a href="{{ post.url | relative_url }}" class="btn btn-primary">Read More</a>
            </div>
          </div>
        </div>
        {% endfor %}

      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-light text-center py-3">
    <p class="mb-0">© {{ site.time | date: "%Y" }} {{ site.title }} · Built with GitHub Pages</p>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

#!/usr/bin/env python3
"""
Iskalla Nyheter - Simpel Webbplats-generator
"""

import os
import json
import random
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path("/home/fg/clawd/projects/iskalla-nyheter")
TEMPLATE_PATH = PROJECT_DIR / "template.html"
OUTPUT_PATH = PROJECT_DIR / "index.html"
ARTICLES_DIR = PROJECT_DIR / "articles"
ARTICLE_PAGES_DIR = PROJECT_DIR / "article-pages"

ORDSPROK = [
    "Isen väntar på ingen människa, men alla människor väntar på isen.",
    "Den som sopar sist, sopar bäst — eller sämst, beroende på vind.",
    "Stenen är rund, men ödet är fyrkantigt.",
    "Vintern kommer alltid, oavsett hur man kastar.",
]

def hamta_artiklar():
    artiklar = []
    for filepath in sorted(ARTICLES_DIR.glob("*.json"), reverse=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                artikel = json.load(f)
                artikel['_filename'] = filepath.stem
                artiklar.append(artikel)
        except Exception as e:
            print(f"Fel: {e}")
    return artiklar

def skapa_artikel_sida(artikel):
    slug = artikel['_filename']
    page_path = ARTICLE_PAGES_DIR / f"{slug}.html"
    
    ordsprak = artikel.get('ordsprak', random.choice(ORDSPROK))
    
    bild_html = ""
    if artikel.get('image'):
        img_path = Path(artikel['image'])
        if img_path.exists():
            rel_path = os.path.relpath(img_path, ARTICLE_PAGES_DIR)
            bild_html = f'<img src="{rel_path}" alt="" class="article-img">'
    
    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{artikel['title']} — Iskalla Nyheter</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600&family=Inter:wght@300;400&display=swap');
        :root {{ --bg: #0d1117; --text: #c9d1d9; --muted: #8b949e; --accent: #58a6ff; --border: #30363d; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; max-width: 700px; margin: 0 auto; padding: 3rem 1.5rem; }}
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .back {{ display: inline-block; margin-bottom: 2rem; }}
        .date {{ color: var(--muted); font-size: 0.85rem; text-transform: uppercase; }}
        h1 {{ font-family: 'Crimson Text', serif; font-size: 2rem; font-weight: 600; margin: 0.5rem 0 1.5rem; color: #f0f6fc; line-height: 1.2; }}
        .article-img {{ width: 100%; height: 300px; object-fit: cover; border-radius: 4px; margin-bottom: 1.5rem; }}
        p {{ margin-bottom: 1rem; }}
        .ordsprak {{ font-family: 'Crimson Text', serif; font-style: italic; color: var(--accent); border-left: 2px solid var(--accent); padding-left: 1rem; margin-top: 2rem; }}
        footer {{ text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.85rem; }}
    </style>
</head>
<body>
    <a href="../index.html" class="back">← Tillbaka</a>
    
    <article>
        <div class="date">{artikel.get('date', '')}</div>
        <h1>{artikel['title']}</h1>
        {bild_html}
        <p>{artikel.get('content', artikel.get('summary', ''))}</p>
        <p class="ordsprak">"{ordsprak}"</p>
    </article>
    
    <footer>
        <p>Iskalla Nyheter — "Isen väntar på ingen människa"</p>
    </footer>
</body>
</html>'''
    
    page_path.write_text(html, encoding='utf-8')
    return page_path

def bygg_artikel_html(artikel):
    slug = artikel['_filename']
    
    bild_html = ""
    if artikel.get('image'):
        img_path = Path(artikel['image'])
        if img_path.exists():
            bild_html = f'<img src="{artikel["image"]}" alt="" class="article-img">'
    
    ordsprak = artikel.get('ordsprak', '')
    ordsprak_html = f'<p class="ordsprak">"{ordsprak}"</p>' if ordsprak else ''
    
    return f'''
        <article>
            <div class="date">{artikel.get('date', '')}</div>
            <h2><a href="article-pages/{slug}.html">{artikel['title']}</a></h2>
            {bild_html}
            <p>{artikel.get('summary', artikel.get('content', '')[:200])}</p>
            {ordsprak_html}
        </article>
    '''

def generera():
    print("❄️  Bygger simpel sida...")
    
    ARTICLE_PAGES_DIR.mkdir(exist_ok=True)
    
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    artiklar = hamta_artiklar()
    
    # Skapa artikelsidor
    for artikel in artiklar:
        skapa_artikel_sida(artikel)
    
    # Bygg startsida
    artiklar_html = '\n'.join(bygg_artikel_html(a) for a in artiklar)
    
    html = template.replace("{{INNEHALL}}", artiklar_html)
    OUTPUT_PATH.write_text(html, encoding='utf-8')
    
    print(f"✅ Klar! {len(artiklar)} artiklar.")

if __name__ == "__main__":
    generera()

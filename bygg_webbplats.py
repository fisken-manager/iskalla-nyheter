#!/usr/bin/env python3
"""
Iskalla Nyheter - Generator
Post-exotic waifu meets Dalarna
"""

import os
import json
import random
from pathlib import Path

PROJECT_DIR = Path("/home/fg/clawd/projects/iskalla-nyheter")
TEMPLATE_PATH = PROJECT_DIR / "template.html"
OUTPUT_PATH = PROJECT_DIR / "index.html"
ARTICLES_DIR = PROJECT_DIR / "articles"
ARTICLE_PAGES_DIR = PROJECT_DIR / "article-pages"

ORDSPROK = [
    "Isen väntar på ingen människa.",
    "Den som sopar sist, sopar bäst.",
    "Stenen är rund, men ödet är fyrkantigt.",
    "Man ska inte gråta över spilld curlingsten.",
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
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;600&family=Noto+Sans+JP:wght@300;400&display=swap" rel="stylesheet">
    <style>
        :root {{ --tra: #c9b18a; --sot: #2a2520; --blod: #8b2635; --aska: #4a3f35; --mork: #1a1714; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Noto Sans JP', sans-serif; background: var(--mork); color: var(--tra); line-height: 1.8; max-width: 650px; margin: 0 auto; padding: 4rem 1.5rem; }}
        a {{ color: var(--aska); text-decoration: none; }}
        a:hover {{ color: var(--blod); }}
        .back {{ display: inline-block; margin-bottom: 3rem; font-size: 0.85rem; }}
        .date {{ color: var(--aska); font-size: 0.8rem; letter-spacing: 0.1em; }}
        h1 {{ font-family: 'Noto Serif JP', serif; font-size: 1.6rem; font-weight: 400; margin: 1rem 0 1.5rem; color: var(--tra); line-height: 1.3; }}
        .article-img {{ width: 100%; height: 280px; object-fit: cover; margin: 1.5rem 0; filter: sepia(30%) contrast(0.9); border: 1px solid var(--aska); }}
        p {{ margin-bottom: 1rem; opacity: 0.9; }}
        .ordsprak {{ font-family: 'Noto Serif JP', serif; font-style: italic; color: var(--blod); margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--aska); }}
        footer {{ text-align: center; margin-top: 4rem; padding-top: 3rem; border-top: 1px solid var(--aska); color: var(--aska); font-size: 0.8rem; }}
    </style>
</head>
<body>
    <a href="../index.html" class="back">← Tillbaka</a>
    
    <article>
        <div class="date">{artikel.get('date', '')}</div>
        <h1>{artikel['title']}</h1>
        {bild_html}
        <p>{artikel.get('content', artikel.get('summary', ''))}</p>
        <p class="ordsprak">{ordsprak}</p>
    </article>
    
    <footer>
        <p>囚 — Iskalla Nyheter</p>
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
    ordsprak_html = f'<p class="ordsprak">{ordsprak}</p>' if ordsprak else ''
    
    return f'''
        <article>
            <div class="date">{artikel.get('date', '')}</div>
            <h2><a href="article-pages/{slug}.html">{artikel['title']}</a></h2>
            {bild_html}
            <p>{artikel.get('summary', artikel.get('content', '')[:180])}</p>
            {ordsprak_html}
        </article>
    '''

def generera():
    print("囚 Bygger Iskalla Nyheter...")
    
    ARTICLE_PAGES_DIR.mkdir(exist_ok=True)
    
    template = TEMPLATE_PATH.read_text(encoding='utf-8')
    artiklar = hamta_artiklar()
    
    for artikel in artiklar:
        skapa_artikel_sida(artikel)
    
    artiklar_html = '\n'.join(bygg_artikel_html(a) for a in artiklar)
    html = template.replace("{{INNEHALL}}", artiklar_html)
    OUTPUT_PATH.write_text(html, encoding='utf-8')
    
    print(f"✅ {len(artiklar)} artiklar. Färdig.")

if __name__ == "__main__":
    generera()

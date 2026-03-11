#!/usr/bin/env python3
"""
Iskalla Nyheter - Förbättrad Webbplats-generator
Med artikelsidor, bilder och fungerande länkar
"""

import os
import sys
import json
import subprocess
import random
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path("/home/fg/clawd/projects/iskalla-nyheter")
TEMPLATE_PATH = PROJECT_DIR / "template.html"
OUTPUT_PATH = PROJECT_DIR / "index.html"
ARTICLES_DIR = PROJECT_DIR / "articles"
ARTICLE_PAGES_DIR = PROJECT_DIR / "article-pages"
IMAGES_DIR = PROJECT_DIR / "images"

ORDSPROK = [
    "Isen väntar på ingen människa, men alla människor väntar på isen.",
    "Den som sopar sist, sopar bäst — eller sämst, beroende på vind.",
    "Stenen är rund, men ödet är fyrkantigt.",
    "Man ska inte gråta över spilld curlingsten.",
    "Vintern kommer alltid, oavsett hur man kastar.",
    "Borsten är kort, men minnet är långt.",
    "En blind höna kan också hitta en sten, men inte alltid i huset.",
]

def hamta_artiklar():
    """Hämtar alla artiklar sorterade efter datum (nyast först)"""
    artiklar = []
    
    for filepath in sorted(ARTICLES_DIR.glob("*.json"), reverse=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                artikel = json.load(f)
                artikel['_filename'] = filepath.stem
                artiklar.append(artikel)
        except Exception as e:
            print(f"Kunde inte läsa {filepath}: {e}")
    
    return artiklar

def skapa_artikel_sida(artikel):
    """Skapar en enskild artikelsida"""
    slug = artikel['_filename']
    page_path = ARTICLE_PAGES_DIR / f"{slug}.html"
    
    # Hämta relaterade artiklar (samma kategori, annan än denna)
    relaterade = []
    
    ordsprak = artikel.get('ordsprak', random.choice(ORDSPROK))
    
    # Bild-HTML
    bild_html = ""
    if artikel.get('image'):
        img_path = Path(artikel['image'])
        if img_path.exists():
            rel_path = os.path.relpath(img_path, ARTICLE_PAGES_DIR)
            bild_html = f'<img src="{rel_path}" alt="{artikel["title"]}" class="article-hero-image">'
        else:
            # Fallback till placeholder
            bild_html = f'<div class="article-hero-image placeholder-image"><span>❄️ Ingen bild tillgänglig</span></div>'
    
    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{artikel['title']} — Iskalla Nyheter</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');
        
        :root {{
            --isbla: #1a2332;
            --morkis: #0d1117;
            --frost: #c9d1d9;
            --dalablatt: #2d4a6f;
            --snovit: #f0f6fc;
            --askgra: #8b949e;
            --bloodfrost: #58a6ff;
            --isglans: rgba(88, 166, 255, 0.1);
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: var(--morkis);
            color: var(--frost);
            line-height: 1.8;
            min-height: 100vh;
        }}
        
        header {{
            background: linear-gradient(180deg, var(--isbla) 0%, var(--morkis) 100%);
            border-bottom: 1px solid var(--dalablatt);
            padding: 1.5rem 0;
        }}
        
        .header-content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem;
            text-align: center;
        }}
        
        .masthead {{
            font-family: 'Crimson Text', serif;
            font-size: 2rem;
            font-weight: 600;
            background: linear-gradient(135deg, var(--snovit) 0%, var(--askgra) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .masthead a {{
            text-decoration: none;
            color: inherit;
        }}
        
        nav {{
            background: var(--isbla);
            border-bottom: 1px solid rgba(45, 74, 111, 0.5);
            padding: 0.8rem 0;
        }}
        
        .nav-content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: center;
            gap: 1.5rem;
        }}
        
        nav a {{
            color: var(--frost);
            text-decoration: none;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.4rem 0.8rem;
            border-radius: 4px;
            transition: all 0.2s;
        }}
        
        nav a:hover {{
            background: var(--isglans);
            color: var(--bloodfrost);
        }}
        
        main {{
            max-width: 800px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }}
        
        .category-tag {{
            display: inline-block;
            background: var(--isglans);
            color: var(--bloodfrost);
            padding: 0.4rem 1rem;
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            border-radius: 4px;
            margin-bottom: 1.5rem;
        }}
        
        h1 {{
            font-family: 'Crimson Text', serif;
            font-size: 2.5rem;
            font-weight: 600;
            line-height: 1.2;
            margin-bottom: 1rem;
            color: var(--snovit);
        }}
        
        .meta {{
            color: var(--askgra);
            font-size: 0.9rem;
            margin-bottom: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--dalablatt);
        }}
        
        .article-hero-image {{
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 2rem;
            border: 1px solid var(--dalablatt);
        }}
        
        .placeholder-image {{
            background: linear-gradient(145deg, var(--isbla), var(--dalablatt));
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--askgra);
            font-size: 1.2rem;
        }}
        
        .article-content {{
            font-size: 1.1rem;
            line-height: 1.9;
            color: var(--frost);
        }}
        
        .article-content p {{
            margin-bottom: 1.5rem;
        }}
        
        .ordsprak-box {{
            background: linear-gradient(145deg, var(--dalablatt), var(--isbla));
            border-left: 4px solid var(--bloodfrost);
            padding: 1.5rem 2rem;
            margin: 2.5rem 0;
            border-radius: 0 8px 8px 0;
        }}
        
        .ordsprak-box blockquote {{
            font-family: 'Crimson Text', serif;
            font-style: italic;
            font-size: 1.3rem;
            color: var(--snovit);
            margin: 0;
        }}
        
        .ordsprak-box cite {{
            display: block;
            margin-top: 1rem;
            font-size: 0.9rem;
            color: var(--askgra);
            font-style: normal;
        }}
        
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--bloodfrost);
            text-decoration: none;
            margin-top: 3rem;
            padding: 0.8rem 1.5rem;
            border: 1px solid var(--dalablatt);
            border-radius: 6px;
            transition: all 0.2s;
        }}
        
        .back-link:hover {{
            background: var(--isglans);
            border-color: var(--bloodfrost);
        }}
        
        footer {{
            background: var(--isbla);
            border-top: 1px solid var(--dalablatt);
            padding: 2rem;
            text-align: center;
            margin-top: 4rem;
        }}
        
        .footer-logo {{
            font-family: 'Crimson Text', serif;
            font-size: 1.3rem;
            color: var(--askgra);
        }}
        
        .footer-tagline {{
            font-style: italic;
            color: var(--askgra);
            opacity: 0.7;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <div class="masthead"><a href="../index.html">Iskalla Nyheter</a></div>
        </div>
    </header>
    
    <nav>
        <div class="nav-content">
            <a href="../index.html">← Startsida</a>
            <a href="../index.html#senaste">Senaste</a>
            <a href="../index.html#mysterier">Mysterier</a>
            <a href="../index.html#sm2026">SM 2026</a>
        </div>
    </nav>
    
    <main>
        <article>
            <span class="category-tag">{artikel.get('category', 'Nyhet')}</span>
            <h1>{artikel['title']}</h1>
            <div class="meta">Publicerad {artikel.get('date', '')} | Iskalla Nyheter</div>
            
            {bild_html}
            
            <div class="article-content">
                <p>{artikel.get('content', artikel.get('summary', ''))}</p>
            </div>
            
            <div class="ordsprak-box">
                <blockquote>"{ordsprak}"</blockquote>
                <cite>— Mörkrets Dal</cite>
            </div>
            
            <a href="../index.html" class="back-link">← Tillbaka till startsidan</a>
        </article>
    </main>
    
    <footer>
        <div class="footer-logo">Iskalla Nyheter</div>
        <p class="footer-tagline">"Den som sopar sist, sopar bäst — eller sämst, beroende på vind."</p>
    </footer>
</body>
</html>'''
    
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return page_path

def bygg_featured_artikel(artikel):
    """Bygger HTML för featured artikel med länk"""
    slug = artikel['_filename']
    
    bild_html = ""
    if artikel.get('image'):
        img_path = Path(artikel['image'])
        if img_path.exists():
            bild_html = f'<img src="{artikel["image"]}" alt="{artikel["title"]}" loading="lazy">'
        else:
            bild_html = f'<div class="featured-image placeholder-image"><span>❄️</span></div>'
    else:
        bild_html = f'<div class="featured-image placeholder-image"><span>❄️</span></div>'
    
    ordsprak_html = ""
    if artikel.get('ordsprak'):
        ordsprak_html = f'<p class="ordsprak">"{artikel["ordsprak"]}"</p>'
    
    return f'''
        <article class="featured">
            <div class="featured-image">
                <a href="article-pages/{slug}.html">{bild_html}</a>
            </div>
            <div class="featured-content">
                <span class="category-tag">{artikel.get('category', 'Nyhet')}</span>
                <h2><a href="article-pages/{slug}.html">{artikel['title']}</a></h2>
                <p>{artikel.get('summary', artikel.get('content', '')[:200])}</p>
                {ordsprak_html}
                <a href="article-pages/{slug}.html" class="read-more">Läs hela artikeln →</a>
            </div>
        </article>
    '''

def bygg_artikel_kort(artikel):
    """Bygger HTML för artikel-kort med länk"""
    slug = artikel['_filename']
    
    bild_html = ""
    if artikel.get('image'):
        img_path = Path(artikel['image'])
        if img_path.exists():
            bild_html = f'<img src="{artikel["image"]}" alt="{artikel["title"]}" loading="lazy">'
        else:
            bild_html = f'<div class="card-image placeholder-image"><span>❄️</span></div>'
    else:
        bild_html = f'<div class="card-image placeholder-image"><span>❄️</span></div>'
    
    return f'''
        <article class="article-card">
            <a href="article-pages/{slug}.html" class="card-link">
                {bild_html}
                <div class="article-card-content">
                    <span class="category-tag">{artikel.get('category', 'Nyhet')}</span>
                    <h3>{artikel['title']}</h3>
                    <p>{artikel.get('summary', artikel.get('content', '')[:120])}...</p>
                    <span class="read-more-link">Läs mer →</span>
                </div>
            </a>
        </article>
    '''

def bygg_innehall(artiklar):
    """Bygger huvudinnehållet"""
    if not artiklar:
        return '<p style="text-align:center; padding: 4rem; color: #8b949e;">Inga nyheter än. Isen är tyst.</p>'
    
    # Skapa individuella artikelsidor
    print("📝 Skapar artikelsidor...")
    for artikel in artiklar:
        skapa_artikel_sida(artikel)
    
    # Första artikeln är featured
    featured = bygg_featured_artikel(artiklar[0])
    
    # Resten är i grid
    grid_items = ''.join(bygg_artikel_kort(a) for a in artiklar[1:6])
    grid = f'<div class="article-grid">{grid_items}</div>'
    
    # Sidebar med ordspråk
    dagens_ordspak = random.choice(ORDSPROK)
    sidebar = f'''
        <div class="ordsprak-widget">
            <blockquote>"{dagens_ordspak}"</blockquote>
            <cite>— Mörkrets Dal, idag</cite>
        </div>
        
        <div class="sidebar-widget">
            <h4>Kategorier</h4>
            <ul class="widget-list">
                <li><a href="#">Mysterier</a></li>
                <li><a href="#">Tävling</a></li>
                <li><a href="#">Profiler</a></li>
                <li><a href="#">SM 2026</a></li>
                <li><a href="#">Vetenskap</a></li>
            </ul>
        </div>
    '''
    
    return featured + grid + sidebar

def uppdatera_template():
    """Uppdaterar template med nya styles för länkar"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Lägg till CSS för länkar och placeholders
    extra_css = '''
        /* Länkar */
        a {
            color: inherit;
            text-decoration: none;
        }
        
        .featured h2 a {
            color: var(--snovit);
            transition: color 0.2s;
        }
        
        .featured h2 a:hover {
            color: var(--bloodfrost);
        }
        
        .read-more {
            display: inline-block;
            color: var(--bloodfrost);
            margin-top: 1.5rem;
            font-weight: 500;
            transition: transform 0.2s;
        }
        
        .read-more:hover {
            transform: translateX(4px);
        }
        
        .card-link {
            display: block;
            height: 100%;
        }
        
        .card-link:hover h3 {
            color: var(--bloodfrost);
        }
        
        .read-more-link {
            color: var(--bloodfrost);
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        /* Placeholder bilder */
        .placeholder-image {
            background: linear-gradient(145deg, var(--isbla) 0%, var(--dalablatt) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--askgra);
            font-size: 3rem;
        }
        
        .featured .placeholder-image {
            height: 100%;
            min-height: 400px;
        }
        
        .article-card .placeholder-image {
            height: 200px;
        }
        
        .card-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            opacity: 0.85;
            border-bottom: 1px solid var(--dalablatt);
        }
    '''
    
    # Lägg till innan </style>
    template = template.replace('</style>', extra_css + '\n    </style>')
    
    with open(TEMPLATE_PATH, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print("✅ Template uppdaterad med nya styles")

def generera_webbplats():
    """Genererar den färdiga webbplatsen"""
    print("❄️  Bygger Iskalla Nyheter (Förbättrad)...")
    
    # Skapa artikelsidor-mapp
    ARTICLE_PAGES_DIR.mkdir(exist_ok=True)
    
    # Uppdatera template
    uppdatera_template()
    
    # Läs mall
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Hämta artiklar
    artiklar = hamta_artiklar()
    print(f"📰 Hittade {len(artiklar)} artiklar")
    
    # Bygg innehåll
    innehall = bygg_innehall(artiklar)
    
    # Ersätt placeholders
    nu = datetime.now()
    datum_str = nu.strftime("%d %B %Y").replace("January", "Januari").replace("February", "Februari").replace("March", "Mars").replace("April", "April").replace("May", "Maj").replace("June", "Juni").replace("July", "Juli").replace("August", "Augusti").replace("September", "September").replace("October", "Oktober").replace("November", "November").replace("December", "December")
    
    nummer = (nu - datetime(2026, 1, 1)).days
    
    html = template.replace("{{DATUM}}", datum_str.upper())
    html = html.replace("{{NUMMER}}", str(nummer))
    html = html.replace("{{INNEHALL}}", innehall)
    
    # Spara
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Webbplats sparad: {OUTPUT_PATH}")
    print(f"✅ {len(artiklar)} artikelsidor skapade i article-pages/")
    return OUTPUT_PATH

if __name__ == "__main__":
    generera_webbplats()

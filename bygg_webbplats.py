#!/usr/bin/env python3
"""
Iskalla Nyheter - Webbplats-generator
Bygger HTML från mall och artiklar
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

ORDSPROK = [
    "Isen väntar på ingen människa, men alla människor väntar på isen.",
    "Den som sopar sist, sopar bäst — eller sämst, beroende på vind.",
    "Stenen är rund, men ödet är fyrkantigt.",
    "Man ska inte gråta över spilld curlingsten.",
    "Vintern kommer alltid, oavsett hur man kastar.",
    "Borsten är kort, men minnet är långt.",
]

def hamta_artiklar():
    """Hämtar alla artiklar sorterade efter datum (nyast först)"""
    artiklar = []
    
    for filepath in sorted(ARTICLES_DIR.glob("*.json"), reverse=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                artiklar.append(json.load(f))
        except Exception as e:
            print(f"Kunde inte läsa {filepath}: {e}")
    
    return artiklar

def bygg_featured_artikel(artikel):
    """Bygger HTML för featured artikel"""
    bild_html = ""
    if artikel.get('image'):
        bild_path = artikel['image']
        bild_html = f'<img src="{bild_path}" alt="{artikel["title"]}" loading="lazy">'
    
    ordsprak_html = ""
    if artikel.get('ordsprak'):
        ordsprak_html = f'<p class="ordsprak">"{artikel["ordsprak"]}"</p>'
    
    return f'''
        <article class="featured">
            <div class="featured-image">
                {bild_html}
            </div>
            <div class="featured-content">
                <span class="category-tag">{artikel.get('category', 'Nyhet')}</span>
                <h2>{artikel['title']}</h2>
                <p>{artikel.get('summary', artikel.get('content', '')[:200])}</p>
                {ordsprak_html}
            </div>
        </article>
    '''

def bygg_artikel_kort(artikel):
    """Bygger HTML för artikel-kort"""
    bild_html = ""
    if artikel.get('image'):
        bild_path = artikel['image']
        bild_html = f'<img src="{bild_path}" alt="{artikel["title"]}" loading="lazy">'
    
    return f'''
        <article class="article-card">
            {bild_html}
            <div class="article-card-content">
                <span class="category-tag">{artikel.get('category', 'Nyhet')}</span>
                <h3>{artikel['title']}</h3>
                <p>{artikel.get('summary', artikel.get('content', '')[:150])}...</p>
                <span class="date">{artikel.get('date', '')}</span>
            </div>
        </article>
    '''

def bygg_innehall(artiklar):
    """Bygger huvudinnehållet"""
    if not artiklar:
        return '<p style="text-align:center; padding: 4rem; color: #8b949e;">Inga nyheter än. Isen är tyst.</p>'
    
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
    '''
    
    return featured + grid + sidebar

def generera_webbplats():
    """Genererar den färdiga webbplatsen"""
    print("❄️  Bygger Iskalla Nyheter...")
    
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
    return OUTPUT_PATH

if __name__ == "__main__":
    generera_webbplats()

#!/usr/bin/env python3
"""
Iskalla Nyheter - Curling News Generator
En Dala-Noir tidning från Mörkrets Dal
"""

import os
import sys
import json
import random
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Konfiguration
PROJECT_DIR = Path("/home/fg/clawd/projects/iskalla-nyheter")
ARTICLES_DIR = PROJECT_DIR / "articles"
IMAGES_DIR = PROJECT_DIR / "images"
AUDIO_DIR = PROJECT_DIR / "audio"
VIDEO_DIR = PROJECT_DIR / "video"
ASSETS_DIR = PROJECT_DIR / "assets"

# Dala-Noir ordspråk för artiklar
ORDSPROK = [
    "Isen väntar på ingen människa, men alla människor väntar på isen.",
    "Den som sopar sist, sopar bäst — eller sämst, beroende på vind.",
    "Stenen är rund, men ödet är fyrkantigt.",
    "Man ska inte gråta över spilld curlingsten.",
    "Vintern kommer alltid, oavsett hur man kastar.",
    "Borsten är kort, men minnet är långt.",
    "En blind höna kan också hitta en sten, men inte alltid i huset.",
    "Man kan inte ha både glid och grepp — livet är ett val.",
    "Stenen tänker inte, den bara är. Som vi alla.",
    "Hammaren är tung, men tystnaden är tyngre.",
    "Den som spelar mot Mörkret förlorar alltid på övertid.",
    "Isen bryr sig inte om dina ambitioner, den väntar bara på att tina bort.",
]

# Fiktiva nyheter som KUNDE vara sanna
FIKTIVA_NYHETER = [
    {
        "title": "Mysterium i Mjölby: Spöksten dyker upp på banan vid midnatt",
        "summary": "Vaktmästaren rapporterar en ensam curlingsten som rör sig av sig själv när ingen ser. 'Den glider som om den letar efter något,' viskar han.",
        "category": "Mysterier"
    },
    {
        "title": "Ny studie: Curling-spelare lever i snitt 4 år längre — men känner sig 10 år äldre",
        "summary": "Forskare vid Umeå Universitet har upptäckt att curling förlänger livet, men den eviga vintern i själen gör att spelarna känner sig mer förbrukade.",
        "category": "Vetenskap"
    },
    {
        "title": "Lag från Orsa vinner SM genom att inte dyka upp — 'Tystnaden var vår strategi'",
        "summary": "Lag 'De Tysta Fåren' vann guld efter att motståndarna övergav matchen av ren rädsla för det okända.",
        "category": "Tävling"
    },
    {
        "title": "Sundbybergs curlinghall rapporterar: 'Vi har hittat en femte dimension i hacken'",
        "summary": "Tekniker upptäckte att isen i sektion C har egenskaper som inte följer fysikens lagar. 'Stenarna försvinner ibland,' säger hallchefen.",
        "category": "Teknik"
    },
    {
        "title": "Legendaren 'Gråa Vargen' från Siljan gör comeback vid 87 års ålder",
        "summary": "Ingen har sett honom på 30 år, men nu står han åter på isen med sin träborste från 1956. 'Döden kan vänta,' muttrar han.",
        "category": "Profiler"
    },
    {
        "title": "Ny regel på prov: 'Sorg-förlängning' — lag som förlorar får en extra end att sörja i",
        "summary": "Förbundet testar en ny human regel där förlorande lag får möjlighet att 'sörja klart' innan de lämnar isen.",
        "category": "Regler"
    },
    {
        "title": "Rykten: Nya curlingstenar tillverkade av meteoritjärn ska testas i elitserien",
        "summary": "En hemlig källa hävdar att stenar från en meteorit som föll i Norrland 1847 ska användas. 'De sjunger när man kastar dem,' viskar källan.",
        "category": "Rykten"
    },
    {
        "title": "Umeå förbereder sig för SM: 'Vi har köpt in 40% mer snö än vanligt — bara för säkerhets skull'",
        "summary": "Arrangörerna tar inga risker inför SM 2026. 'Om allt går åt helvete har vi i alla fall snö,' säger tävlingsledaren.",
        "category": "SM 2026"
    }
]

# Rubrik-stilar för nyheter
RUBRIK_STILAR = [
    "ISKALLT:",
    "MÖRKRET SÄGER:",
    "FRÅN SKUGGAN:",
    "VINTERNS RÖST:",
    "MJÖLNAREN NOTERAR:",
    "STENEN RULLAR:",
    "I MÖRKRET:",
    "FRÅN LADAN:",
    "ISKALLT MOTTAGET:",
    "VARGENS VISDOM:",
]

def hamta_curlingnyheter():
    """Söker efter aktuella curlingnyheter på webben"""
    print("🔍 Söker curlingnyheter från världens kalla platser...")
    
    # Använd web_search för att hitta nyheter
    try:
        result = subprocess.run([
            "python3", "-c",
            """
import subprocess
import json
result = subprocess.run(
    ['web_search', 'curling news Sweden 2025 2026 SM world championship'],
    capture_output=True, text=True
)
print(result.stdout)
"""
        ], capture_output=True, text=True, cwd="/home/fg/clawd")
        
        # För nu, returnera en platshållare
        return []
    except Exception as e:
        print(f"Kunde inte hämta nyheter: {e}")
        return []

def generera_fiktiv_nyhet():
    """Väljer en fiktiv nyhet och snurrar på den"""
    nyhet = random.choice(FIKTIVA_NYHETER)
    ordsprak = random.choice(ORDSPROK)
    rubrik_stil = random.choice(RUBRIK_STILAR)
    
    return {
        "title": f"{rubrik_stil} {nyhet['title']}",
        "summary": nyhet['summary'],
        "content": f"{nyhet['summary']} {ordsprak}",
        "category": nyhet['category'],
        "date": datetime.now().strftime("%Y-%m-%d"),
        "ordsprak": ordsprak,
        "fiktiv": True
    }

def generera_bild(prompt, output_path):
    """Genererar en bild med Pollinations"""
    print(f"🎨 Genererar bild: {output_path.name}")
    
    # Använd Pollinations för bildgenerering
    full_prompt = f"Dark melancholic curling scene, anime waifu style, {prompt}, blue and white colors, winter atmosphere, snow, shadows, mysterious, Dalarna Sweden aesthetics, dark noir mood, 4k"
    
    try:
        result = subprocess.run([
            "curl", "-s", "-o", str(output_path),
            f"https://image.pollinations.ai/prompt/{full_prompt.replace(' ', '%20')}?width=1024&height=768&nologo=true"
        ], check=True)
        return True
    except Exception as e:
        print(f"Kunde inte generera bild: {e}")
        return False

def spara_artikel(artikel):
    """Sparar artikel till fil"""
    date_str = artikel['date']
    slug = artikel['title'].lower().replace(' ', '-').replace(':', '').replace('—', '-').replace("'", '')[:50]
    filename = f"{date_str}-{slug}.json"
    filepath = ARTICLES_DIR / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(artikel, f, ensure_ascii=False, indent=2)
    
    print(f"💾 Artikel sparad: {filepath}")
    return filepath

def hamta_artiklar(dagar=7):
    """Hämtar alla artiklar från de senaste dagarna"""
    artiklar = []
    cutoff_date = datetime.now() - timedelta(days=dagar)
    
    for filepath in sorted(ARTICLES_DIR.glob("*.json"), reverse=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                artikel = json.load(f)
                artikel_date = datetime.strptime(artikel['date'], "%Y-%m-%d")
                if artikel_date >= cutoff_date:
                    artiklar.append(artikel)
        except Exception as e:
            print(f"Kunde inte läsa {filepath}: {e}")
    
    return artiklar[:10]  # Max 10 artiklar

def huvudprogram():
    """Huvudprogram för daglig nyhetsgenerering"""
    print("🌑 Iskalla Nyheter - Daglig generering")
    print("=" * 50)
    
    # Skapa dagens artikel (fiktiv för nu)
    artikel = generera_fiktiv_nyhet()
    
    # Generera bild till artikeln
    bild_prompt = artikel['title'].replace(':', '').replace('ISKALLT', '').replace('MÖRKRET SÄGER', '').strip()
    bild_path = IMAGES_DIR / f"{artikel['date']}-{bild_prompt[:30].replace(' ', '-')}.jpg"
    
    if generera_bild(bild_prompt, bild_path):
        artikel['image'] = str(bild_path.relative_to(PROJECT_DIR))
    
    # Spara artikeln
    spara_artikel(artikel)
    
    print("\n✅ Dagens nyhet genererad!")
    print(f"📰 {artikel['title']}")
    print(f"📂 {PROJECT_DIR}")

if __name__ == "__main__":
    huvudprogram()

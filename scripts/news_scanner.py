#!/usr/bin/env python3
"""
Iskalla Nyheter - Nyhets-scanner
Letar efter dramatiska curling-historier (inte tråkigheternas högborg)
"""

import subprocess
import json
from datetime import datetime

SOURCES = [
    # Google News via search
    {"name": "Google News", "query": "curling news -worldcurling.org -olympics.com"},
    
    # Reddit - skandaler och drama
    {"name": "Reddit r/curling", "query": "site:reddit.com/r/curling scandal drama controversy"},
    {"name": "Reddit r/sports", "query": "site:reddit.com/r/sports curling drama funny"},
    
    # Svenskt
    {"name": "Svenska nyheter", "query": "curling Sverige Sundbyberg skandal"},
    
    # Underhållning
    {"name": "Underhållning", "query": "curling funny bizarre weird moments memes"},
]

def sok_nyheter():
    """Söker efter nyheter från olika källor"""
    resultat = []
    
    for source in SOURCES:
        print(f"🔍 Söker: {source['name']}")
        
        # Här skulle vi egentligen använda web_search API
        # För nu, simulera med print
        print(f"   Query: {source['query']}")
        
        resultat.append({
            "source": source['name'],
            "query": source['query'],
            "timestamp": datetime.now().isoformat()
        })
    
    return resultat

def bedom_intresse(nyhet):
    """Bedömer om nyheten är skvallervärd"""
    skvaller_keywords = [
        "scandal", "drama", "controversy", "fight", "argument",
        "skandal", "bråk", "drama", "konflikt",
        "meme", "funny", "bizarre", "weird", "crazy",
        "paltkoma", "boop", "fingergate", "hat", "feud"
    ]
    
    trakiga_keywords = [
        "results", "standings", "schedule", "medal", "won gold",
        "world curling", "official", "press release",
        "congratulations", "proud", "honored"
    ]
    
    text = nyhet.lower()
    
    skvaller_poang = sum(1 for k in skvaller_keywords if k in text)
    trakig_poang = sum(1 for k in trakiga_keywords if k in text)
    
    return skvaller_poang > trakig_poang

if __name__ == "__main__":
    print("🌑 Iskalla Nyheter - Scanner")
    print("Letar efter dramatiska historier...")
    print("(Inte World Curling - de är tråkigheternas högborg)")
    print()
    
    resultat = sok_nyheter()
    
    print(f"\n✅ Skannade {len(resultat)} källor")
    print("Använd web_search manuellt för att hitta specifika nyheter")

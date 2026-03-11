#!/usr/bin/env python3
"""
Iskalla Nyheter - Ljudgenerator
Skapar Dala-Noir podcasts och läsningar
"""

import os
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path("/home/fg/clawd/projects/iskalla-nyheter")
AUDIO_DIR = PROJECT_DIR / "audio"

def skapa_podcast_intro():
    """Skapar podcast-intro med Dala-Noir stil"""
    intro_text = """
    Välkommen till Iskalla Nyheter. Jag är er värd från Mörkrets Dal. 
    Idag ska vi tala om curling, is, och det oundvikliga nederlaget mot verkligheten. 
    Stenen är rund, men ödet är fyrkantigt. 
    """
    
    # Använd Pollinations för waifu-röst
    print("🎙️  Genererar podcast-intro...")
    
    # Detta skulle använda pollinations waifu_voice.sh scriptet
    # För nu, skapa en placeholder
    output_path = AUDIO_DIR / f"podcast-intro-{datetime.now().strftime('%Y%m%d')}.txt"
    with open(output_path, 'w') as f:
        f.write(intro_text)
    
    print(f"💾 Podcast-manus sparat: {output_path}")
    return output_path

def skapa_artikel_ljud(artikel):
    """Skapar ljudversion av artikel"""
    title = artikel['title']
    content = artikel.get('content', '')
    
    # Formatera för uppläsning
    text = f"{title}. {content}"
    
    print(f"🎙️  Skapar ljud för: {title[:40]}...")
    
    # Spara manus
    safe_title = "".join(c for c in title[:30] if c.isalnum() or c in (' ', '-', '_')).rstrip()
    output_path = AUDIO_DIR / f"{datetime.now().strftime('%Y%m%d')}-{safe_title}.txt"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"💾 Ljud-manus sparat: {output_path}")
    return output_path

if __name__ == "__main__":
    print("🎵 Iskalla Nyheter - Ljudgenerator")
    print("=" * 40)
    
    # Skapa podcast-intro
    skapa_podcast_intro()
    
    print("\n✅ Ljudinnehåll genererat!")
    print("Använd Pollinations waifu_voice.sh för att generera faktiska ljudfiler")

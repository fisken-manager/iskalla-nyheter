#!/usr/bin/env python3
"""
Iskalla Journalism - Media-generator
Genererar bilder och röst för artiklar
"""

import json
import argparse
import subprocess
from pathlib import Path

def generera_bild(prompt, output_path):
    """Genererar bild med Pollinations"""
    print(f"🎨 Genererar bild: {output_path.name}")
    
    # Full Dala-Noir prompt
    full_prompt = f"Dark melancholic curling scene, anime waifu style, {prompt}, dark purple and pink neon colors, winter atmosphere, shadows, mysterious, post-exotic aesthetic, 4k, cinematic"
    
    try:
        subprocess.run([
            "curl", "-L", "-o", str(output_path),
            f"https://image.pollinations.ai/prompt/{full_prompt.replace(' ', '%20')}?width=1024&height=768&nologo=true&seed=42"
        ], check=True, capture_output=True)
        print(f"✅ Bild sparad: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Fel: {e}")
        return False

def generera_röst(text, output_path):
    """Genererar röst med TTS (placeholder för nu)"""
    print(f"🎙️  Röstmanus sparat: {output_path}")
    
    # Spara manus för framtida TTS-generering
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("   Använd Pollinations waifu_voice.sh för att generera faktisk ljudfil")
    return True

def main():
    parser = argparse.ArgumentParser(description="Generera media för Iskalla Nyheter")
    parser.add_argument("--article", required=True, help="JSON-fil med artikel")
    parser.add_argument("--output-dir", required=True, help="Output-mapp")
    
    args = parser.parse_args()
    
    # Läs artikel
    with open(args.article, 'r', encoding='utf-8') as f:
        artikel = json.load(f)
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generera bild
    slug = artikel['title'].lower().replace(' ', '-').replace(':', '').replace("'", '')[:30]
    bild_path = output_dir / f"{slug}.jpg"
    
    bild_prompt = artikel.get('image_prompt', artikel['title'])
    generera_bild(bild_prompt, bild_path)
    
    # Spara röstmanus
    röst_path = output_dir / f"{slug}-voice.txt"
    
    # Skapa intro-manus för waifu-röst
    röst_text = f"""
Välkommen till Iskalla Nyheter. Detta är {artikel['date']}.

{artikel['ingress']}

{artikel.get('facts', {}).get('vad', '')}

{artikel['ordsprak']}

Det var allt för denna gång. Isen väntar på nästa.
"""
    generera_röst(röst_text, röst_path)
    
    print(f"\n✅ Media genererad i: {output_dir}")

if __name__ == "__main__":
    main()

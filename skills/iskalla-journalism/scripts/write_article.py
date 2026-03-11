#!/usr/bin/env python3
"""
Iskalla Journalism - Artikel-skrivare
Blandar verklig research med Dala-Noir fiction
"""

import json
import argparse
import random
from datetime import datetime
from pathlib import Path

# Dala-Noir ordspråk
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
    "Den som gräver där han står, får snö i skorna.",
    "Man ska inte stoppa mer palt i munnen än vad man kan kasta sten.",
    "Isen är kall, men hatet är kallare.",
]

def generera_citat(kontext=""):
    """Genererar trovärdiga påhittade citat"""
    citat_mallar = [
        "Jag såg det med egna ögon, men jag önskar att jag inte hade sett det.",
        "Det var som att titta på en bilolycka i slow motion.",
        "Hallvakten muttrade något om att 'detta har hänt förut', men ingen lyssnade.",
        "Vi stod där och undrade om isen skulle hålla eller brista.",
        "En äldre spelare skakade på huvudet och gick därifrån. Han hade sett detta förr.",
        "Tystnaden efteråt var högre än när vi vann SM.",
        "Jag hörde någon säga 'det är bara curling', men det är aldrig bara curling.",
        "Stenen visste. Stenarna vet alltid.",
        "Vi sopade tills händerna blödde, men det hjälpte inte.",
        "I omklädningsrummet efteråt pratade ingen. Bara duschen som rann.",
    ]
    return random.choice(citat_mallar)

def skapa_artikel(title, summary, research_data, date=None):
    """Skapar en strukturerad artikel"""
    
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # Välj ordspråk
    ordsprak = random.choice(ORDSPROK)
    
    # Bygg artikel-struktur
    artikel = {
        "title": title,
        "date": date,
        "category": research_data.get("category", "Nyhet"),
        "ingress": summary,
        "facts": {
            "vem": research_data.get("vem", "Okända krafter"),
            "vad": research_data.get("vad", "En händelse på isen"),
            "var": research_data.get("var", "Någonstans i Mörkret"),
            "nar": research_data.get("nar", "En tisdag i evigheten"),
            "varfor": research_data.get("varfor", "För att ödet så ville"),
        },
        "citat": generera_citat(),
        "context": research_data.get("context", ""),
        "analysis": research_data.get("analysis", ""),
        "ordsprak": ordsprak,
        "fiktiv": research_data.get("fiktiv", True),
        "image": research_data.get("image", ""),
    }
    
    # Bygg fullständig text
    artikel["content"] = bygg_full_text(artikel)
    artikel["summary"] = summary
    
    return artikel

def bygg_full_text(artikel):
    """Bygger fullständig artikeltext från struktur"""
    
    parts = []
    
    # Ingress (redan i summary)
    parts.append(artikel["ingress"])
    parts.append("")
    
    # Fakta med 5W
    facts = artikel["facts"]
    parts.append(f"Det var {facts['nar']} som det hände. {facts['vem']} stod på {facts['var']} när {facts['vad']}. Ingen kunde förklara varför, men alla visste att {facts['varfor']}.")
    parts.append("")
    
    # Citat
    parts.append(f'"{artikel["citat"]}" — en röst från skuggorna.')
    parts.append("")
    
    # Kontext
    if artikel["context"]:
        parts.append(artikel["context"])
        parts.append("")
    
    # Analys (Dala-Noir spin)
    if artikel["analysis"]:
        parts.append(artikel["analysis"])
    else:
        parts.append("I Mörkrets Dal vet vi att sådant händer. Isen är lika oförutsägbar som ödet. Vi kastar våra stenar och hoppas på det bästa, men isen bestämmer alltid till sist.")
    
    parts.append("")
    parts.append(f"{artikel['ordsprak']}")
    
    return "\n".join(parts)

def main():
    parser = argparse.ArgumentParser(description="Skriv Iskalla Nyheter-artikel")
    parser.add_argument("--title", required=True, help="Artikelrubrik")
    parser.add_argument("--summary", required=True, help="Ingress")
    parser.add_argument("--research", required=True, help="JSON-fil med research")
    parser.add_argument("--output", required=True, help="Output JSON-fil")
    parser.add_argument("--date", help="Datum (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    # Läs research
    with open(args.research, 'r', encoding='utf-8') as f:
        research = json.load(f)
    
    # Skapa artikel
    artikel = skapa_artikel(args.title, args.summary, research, args.date)
    
    # Spara
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(artikel, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Artikel skapad: {output_path}")
    print(f"   Rubrik: {artikel['title']}")
    print(f"   Ord: {len(artikel['content'].split())}")

if __name__ == "__main__":
    main()

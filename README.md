# Iskalla Nyheter 🌑

**Curling & Mörker från Dalarnas Djup**

En Dala-Noir nyhetssida som täcker curling-världen med melankolisk visdom, fiktiva nyheter som kunde vara sanna, och den eviga vinterns röst.

## Filosofi

> "Isen väntar på ingen människa, men alla människor väntar på isen."

Iskalla Nyheter är inte en vanlig sporttidning. Vi rapporterar om curling som det är — en kamp mot naturen, mot sig själv, och mot det oundvikliga nederlaget. Med inspiration från:
- Antoine Volodine (misslyckade uppror)
- E.M. Cioran (insomniens profet)
- Giacomo Leopardi (långsamma vinterkvällar)
- Dalarnas fuktiga ladugårdar

## Struktur

```
iskalla-nyheter/
├── articles/          # JSON-artiklar
├── images/            # AI-genererade bilder
├── audio/             # Podcasts och uppläsningar
├── video/             # Video-innehåll
├── assets/            # CSS, fonts, etc.
├── template.html      # HTML-mall
├── generera_nyheter.py      # Huvudgenerator
├── bygg_webbplats.py        # Webbplats-byggare
├── generera_ljud.py         # Ljud-generator
└── publicera.sh             # Daglig publicering
```

## Daglig Drift

### Manuell körning:
```bash
cd ~/clawd/projects/iskalla-nyheter
./publicera.sh
```

### Automatisk cron (varje dag kl 06:00):
```bash
# Lägg till i crontab:
0 6 * * * cd /home/fg/clawd/projects/iskalla-nyheter && ./publicera.sh >> logs/cron.log 2>&1
```

## Innehållstyper

### 1. Riktiga Nyheter (spin-nade)
- Söker aktuella curlingnyheter
- Omvandlar till Dala-Noir stil
- Lägger till ordspråk och melankoli

### 2. Fiktiva Nyheter ("kunde vara sanna")
- Mysterier i curlinghallar
- Legendariska spelare som återvänder
- Övernaturliga fenomen på isen
- Nya regelförslag från förbundet

### 3. Multimedia
- **Bilder:** AI-genererade med Pollinations (dark anime waifu, winter aesthetic)
- **Ljud:** Podcasts och artikeluppläsningar med waifu-röst
- **Video:** Kommande funktion

## Estetik

### Färger
- Isblå (#1a2332)
- Mörk is (#0d1117)
- Frost (#c9d1d9)
- Dalablått (#2d4a6f)
- Snövit (#f0f6fc)
- Blodfrost (#58a6ff)

### Typsnitt
- **Rubriker:** Crimson Text (serif)
- **Brödtext:** Inter (sans-serif)

### Stil
- Mörk, melankolisk, vinter Noir
- Anime waifu-element (som påminnelse om den falska oskyldigheten)
- Gradients som frost på fönster
- Minimalistisk och läsbar

## Exempel på Ordspråk

- "Den som sopar sist, sopar bäst — eller sämst, beroende på vind."
- "Stenen är rund, men ödet är fyrkantigt."
- "Man ska inte gråta över spilld curlingsten."
- "Vintern kommer alltid, oavsett hur man kastar."
- "Borsten är kort, men minnet är långt."

## Utveckling

### Lägg till nya fiktiva nyheter:
Redigera `generera_nyheter.py` och lägg till i `FIKTIVA_NYHETER`-listan.

### Ändra utseende:
Redigera `template.html` — CSS-variabler finns i `:root`.

### Generera ljud:
```bash
python3 generera_ljud.py
```

## Åtkomst

Öppna i webbläsare:
```
file:///home/fg/clawd/projects/iskalla-nyheter/index.html
```

---

*"Den som spelar mot Mörkret förlorar alltid på övertid."*

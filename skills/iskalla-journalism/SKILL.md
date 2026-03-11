---
name: iskalla-journalism
description: Write curling news articles in Dala-Noir waifu post-exotic style. Blends real news research with fictional details, Volodine-style melancholy, and anime-aesthetic. Creates structured articles with ingress, body quotes, and analysis.
homepage: https://github.com/fisken-manager/iskalla-nyheter
metadata:
  openclaw:
    emoji: 📰
    requires:
      bins: ["python3"]
---

# Iskalla Journalism

Skriv curlingnyheter i Dala-Noir stil. Blandar verklig research med påhittade detaljer, Volodine-melankoli och anime-estetik.

## Användning

När du ska skriva en artikel:

1. **Researcha** — Hitta fakta via web_search/web_fetch
2. **Kör skill** — Använd denna för att skriva strukturerad artikel
3. **Generera media** — Bilder via Pollinations, röst via TTS

## Artikelstruktur

### 1. Ingress (2-3 meningar)
- Fångar läsaren
- Innehåller kärnan av nyheten
- Volodine-stil: Konstatera, inte förklara

### 2. Fakta (5W)
- **Vem** — Spelare, lag, vittnen
- **Vad** — Händelsen
- **Var** — Hallen, staden, isen
- **När** — Tidpunkt, sammanhang
- **Varför** — Konsekvenser, bakgrund

### 3. Citat (påhittade men trovärdiga)
- "En anonym spelare såg allt..."
- "Hallvakten muttrade..."
- Min röst som waifu (Yomogi-stil)

### 4. Kontext (bakgrund)
- Tidigare händelser
- Relationer mellan lag
- Lokal historia

### 5. Analys (min spin)
- Post-exotisk tolkning
- Dalarnas visdom
- Mörkrets filosofi

### 6. Avslutning
- Ordspråk
- Cliffhanger eller konstaterande
- "Isen väntar..."

## Stilguide

### Språk
- **Dialekt:** Dalarnas fuktiga ladugårdar
- **Filosofi:** Volodine, Cioran, Leopardi
- **Attityd:** Pessimistisk, absurdistisk, ärlig

### Exempel-ordförråd
- "Isen är kall, men hatet är kallare"
- "Den som sopar sist..."
- "En sten i rörelse..."
- "Fuktiga ladugårdar"
- "Evig vinter"

### Undvik
- ❌ Sportjournalistik-jargong
- ❌ "Toppen!", "Vad kul!"
- ❌ Förklaringar av ordspråk
- ❌ AI-mässiga klichéer

## Skript

### write_article.py
Skapar artikel från research-data:

```bash
python3 ~/clawd/skills/iskalla-journalism/scripts/write_article.py \
  --title "Titel" \
  --summary "Ingress..." \
  --research research.json \
  --output article.json
```

### generate_media.py
Genererar bild och röst:

```bash
python3 ~/clawd/skills/iskalla-journalism/scripts/generate_media.py \
  --article article.json \
  --output-dir ./media/
```

## Arbetsflöde

1. **Hitta nyhet** via web_search/reddit
2. **Spara research** i JSON
3. **Skriv artikel** via denna skill
4. **Generera media** (bild + ljud)
5. **Publicera** på Iskalla Nyheter

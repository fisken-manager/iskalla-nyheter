#!/bin/bash
# Iskalla Nyheter - Daglig publicering
# Körs varje dag för att generera nya nyheter

cd /home/fg/clawd/projects/iskalla-nyheter

echo "🌑 Iskalla Nyheter - Daglig generering"
echo "=========================================="
echo ""

# Generera nya artiklar och bilder
echo "📰 Genererar dagens nyheter..."
python3 generera_nyheter.py

# Bygg webbplatsen
echo ""
echo "🏗️  Bygger webbplats..."
python3 bygg_webbplats.py

echo ""
echo "✅ Klart! Besök file:///home/fg/clawd/projects/iskalla-nyheter/index.html"

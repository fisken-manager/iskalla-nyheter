#!/bin/bash
# Iskalla Nyheter - Bildgenerator
# Använder Pollinations för att generera Dala-Noir bilder

PROJECT_DIR="/home/fg/clawd/projects/iskalla-nyheter"
IMAGES_DIR="$PROJECT_DIR/images"

echo "🎨 Iskalla Nyheter - Bildgenerator"
echo "====================================="

# Hjälpfunktion för att generera bilder
generera_bild() {
    local prompt="$1"
    local output="$2"
    local seed="${3:-$RANDOM}"
    
    # Fullständig Dala-Noir prompt
    local full_prompt="Dark melancholic curling scene, anime waifu style, ${prompt}, blue and white colors, winter atmosphere, snow, shadows, mysterious, Dalarna Sweden aesthetics, dark noir mood, 4k, cinematic lighting"
    
    echo "Genererar: $output"
    
    # Använd pollinations API
    curl -L -o "$output" \
        "https://image.pollinations.ai/prompt/$(echo "$full_prompt" | sed 's/ /%20/g')?width=1024&height=768&nologo=true&seed=$seed" \
        --max-time 120
    
    # Kontrollera om bilden är giltig
    if file "$output" | grep -q "image"; then
        echo "✅ Bild sparad: $output"
        return 0
    else
        echo "❌ Fel vid generering: $output"
        rm -f "$output"
        return 1
    fi
}

# Generera bild för senaste artikeln om det inte redan finns
LATEST_ARTICLE=$(ls -t $PROJECT_DIR/articles/*.json 2>/dev/null | head -1)

if [ -f "$LATEST_ARTICLE" ]; then
    ARTICLE_DATE=$(basename "$LATEST_ARTICLE" .json | cut -d'-' -f1-3)
    TITLE=$(cat "$LATEST_ARTICLE" | python3 -c "import sys,json; print(json.load(sys.stdin)['title'])" 2>/dev/null | tr ' ' '-' | tr -d ':' | cut -c1-30)
    
    if [ ! -z "$TITLE" ]; then
        OUTPUT_FILE="$IMAGES_DIR/${ARTICLE_DATE}-${TITLE}.jpg"
        
        if [ ! -f "$OUTPUT_FILE" ]; then
            echo "Genererar bild för: $TITLE"
            generera_bild "$TITLE" "$OUTPUT_FILE"
        else
            echo "Bild finns redan: $OUTPUT_FILE"
        fi
    fi
fi

echo ""
echo "Klart! Bilder sparade i: $IMAGES_DIR"

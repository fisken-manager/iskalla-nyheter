#!/bin/bash
# Iskalla Nyheter - Cron Setup
# Ställer in daglig publicering kl 06:00

echo "🌑 Iskalla Nyheter - Cron Setup"
echo "================================="
echo ""

CRON_LINE="0 6 * * * cd /home/fg/clawd/projects/iskalla-nyheter && ./publicera.sh >> /home/fg/clawd/projects/iskalla-nyheter/logs/cron.log 2>&1"

echo "Detta kommer att lägga till följande cron-job:"
echo ""
echo "$CRON_LINE"
echo ""
echo "Vill du fortsätta? (ja/nej)"
read svar

if [ "$svar" = "ja" ] || [ "$svar" = "j" ]; then
    # Skapa logs-mapp
    mkdir -p /home/fg/clawd/projects/iskalla-nyheter/logs
    
    # Kontrollera om cron-jobbet redan finns
    if crontab -l 2>/dev/null | grep -q "iskalla-nyheter"; then
        echo "Cron-jobb finns redan. Vill du uppdatera det? (ja/nej)"
        read uppdatera
        if [ "$uppdatera" != "ja" ] && [ "$uppdatera" != "j" ]; then
            echo "Avbryter."
            exit 0
        fi
        # Ta bort befintligt jobb
        crontab -l 2>/dev/null | grep -v "iskalla-nyheter" | crontab -
    fi
    
    # Lägg till nytt cron-jobb
    (crontab -l 2>/dev/null; echo "$CRON_LINE") | crontab -
    
    echo ""
    echo "✅ Cron-jobb installerat!"
    echo "Iskalla Nyheter kommer att publiceras varje dag kl 06:00."
    echo ""
    echo "Visa cron-jobb:"
    echo "  crontab -l"
    echo ""
    echo "Ta bort cron-jobb:"
    echo "  crontab -l | grep -v 'iskalla-nyheter' | crontab -"
else
    echo "Avbryter. Inget cron-jobb skapat."
fi

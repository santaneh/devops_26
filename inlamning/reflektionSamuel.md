1. Produktens livscykel
Vår app började som en kopia av kursens template-repo. I M1 och M2 jobbade vi nästan helt för hand: jag ändrade knapp- och bakgrundsstil, och i konfliktövningen ändrade jag och Henri samma h1-rad till BOB på varsin branch. Konflikten löste vi manuellt i GitHub. Rulesetet vi satte upp i M2 tvingade fram pull requests och review, men det enda som stoppade dålig kod var att en människa tittade på den.

I M3 lärde vi oss containers. Jag lade till .dockerignore efter att vi sett att __pycache__ följde med in i imagen, och jag pushade frontend-imagen till GHCR med docker tag och docker push. Det fungerade, men det var ett steg som bara hände om någon kom ihåg att göra det, från sin egen dator.

M4 var en vändpunkt i hur jag ser på tester: alla tester var gröna, men appen hade ändå en bugg (characters uppdaterades inte när en anteckning togs bort). Testerna var bara så bra som de fall de täckte. Vi skrev ett test som först failade, rättade koden och såg testet bli grönt.

Från M5 började kedjan göra jobbet åt oss. Jag gjorde den medvetet röda pull requesten med en oanvänd import json. ruff pekade ut exakt raden, och merge-knappen var låst tills jag pushade fixen. I M6 ändrade jag själv publish-images.yml så att den kan köras manuellt och skriver ut image-taggarna (:latest och commit-sha) i sammanfattningen. Då ersattes min manuella push från M3 av något som händer vid varje merge.

M7 var tvärtom helt manuellt: SSH-nycklar, security group, floating IP, installera Docker och köra docker compose up på VM:en. I M8 beskrev vi samma sak i Terraform. Vi kunde riva instansen och bygga upp den igen med samma IP, och prevent_destroy stoppade en terraform destroy som annars hade rivit allt. I M9 kopplades allt ihop: min ändring av rubriken gick via PR, CI blev grön, Publish images byggde nya images och Deploy to VM uppdaterade servern på m8-samuel utan att någon loggade in på den.

Det som förändrades i mitt arbetssätt är att jag slutade tänka "vad måste jag komma ihåg att göra" och började tänka "vad ska kedjan kontrollera åt mig". Mitt jobb blev att göra en liten, granskningsbar ändring och låta pipelinen ta resten.

2. Vad går sönder utan automation?
Den tydligaste punkten är CD-steget i M9. Om det gjordes för hand igen skulle varje release se ut som i M7: logga in med SSH, hämta nya images, starta om containrarna och kolla att det fungerar. Det tar tid, kräver att rätt person har rätt nyckel och är lätt att göra slarvigt. I M7 fick vi själva komma ihåg att öppna port 8080 i security groupen, lägga in båda våra SSH-nycklar på VM:en och installera Docker innan appen ens kunde svara utifrån. Om ett enda steg missades svarade appen inte, och felet syntes först när vi testade med curl. Med automationen deployas alltid exakt den image som byggdes från commiten på main, och sha-taggen visar vilken version som kör. För hand finns risken att servern kör något annat än det som ligger i repot, utan att någon märker det.

CI-checken är lika viktig. Min röda PR i M5 visade att ett fel som är lätt att missa i en review (en oanvänd import) fångades direkt, och att det var omöjligt att merga det. Utan checken hade det hängt på att granskaren råkade se raden. Och eftersom CD bara körs efter merge till main är CI-checken det som skyddar produktionen: utan den skulle automationen i M9 lika snabbt deploya trasig kod.

M4 visar ändå var gränsen går. Automation kör bara de tester som finns. Kedjan gör det säkrare och snabbare att leverera, men det är fortfarande vårt ansvar att testerna täcker hur appen faktiskt används.
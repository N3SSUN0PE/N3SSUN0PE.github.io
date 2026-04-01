import os
import glob
from datetime import datetime

# 1. Scansiona l'ambiente e trova l'ultimo log
files = glob.glob("giorno*.html")
numeri = []
for f in files:
    try:
        numeri.append(int(f.replace("giorno", "").replace(".html", "")))
    except ValueError:
        pass

nuovo_num = max(numeri) + 1 if numeri else 1
nuovo_file = f"giorno{nuovo_num}.html"
data_odierna = datetime.now().strftime("%d/%m/%Y")

# 2. Il Template Strutturale (L'anima del nuovo file)
template = f"""<!DOCTYPE html>
<html>
<head>
    <title>Giorno {nuovo_num} - N3SSUN0PE LAB</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav style="width: 100%; background: var(--card); padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); position: sticky; top: 0; z-index: 100; display: flex; justify-content: center; margin-bottom: 2rem;">
        <div style="width: 100%; max-width: 800px; display: flex; justify-content: space-between; padding: 0 1rem;">
            <span style="font-weight: bold; color: var(--accent);">N3SSUN0PE LAB</span>
            <div>
                <a href="index.html" style="margin-left: 1.5rem; font-size: 0.9rem;">Home</a>
                <a href="archivio.html" style="margin-left: 1.5rem; font-size: 0.9rem;">Archivio</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>Appunti del Giorno {nuovo_num}</h1>
        <p style="color: var(--text-dim); text-align: center;">Data: {data_odierna}</p>
        <div class="log-card">
            <h2>Titolo argomento...</h2>
            <p>Sostituisci questo testo con i log di oggi.</p>
        </div>
    </div>
</body>
</html>"""

# Genera il file fisico
with open(nuovo_file, "w", encoding="utf-8") as f:
    f.write(template)

# 3. L'Iniezione nell'Archivio
with open("archivio.html", "r", encoding="utf-8") as f:
    archivio = f.read()

nuovo_link = f'\n        <li style="margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">\n            <a href="{nuovo_file}">🔨 Giorno {nuovo_num}: Appunti del {data_odierna}</a>\n        </li>'

if '' in archivio:
    archivio = archivio.replace('', nuovo_link)
    with open("archivio.html", "w", encoding="utf-8") as f:
        f.write(archivio)
    print(f"Script completato: {nuovo_file} generato e indicizzato in archivio.")
else:
    print(f"File {nuovo_file} creato, ma INJECT_HERE non trovato in archivio.html. Aggiungilo a mano.")
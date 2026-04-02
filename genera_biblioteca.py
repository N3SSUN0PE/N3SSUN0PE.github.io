import os

# 1. Configurazione del radar
base_dir = "assets/biblioteca"
file_html = "biblioteca.html"
nuovo_contenuto_html = ""

print("Avvio scansione biblioteca...")

# 2. Esplorazione delle cartelle
if os.path.exists(base_dir):
    for materia in sorted(os.listdir(base_dir)):
        materia_path = os.path.join(base_dir, materia)
        
        # Ignora file spazzatura, processa solo le cartelle
        if os.path.isdir(materia_path):
            titolo_materia = materia.capitalize()
            print(f"-> Trovata materia: {titolo_materia}")
            
            # Forgiamo l'intestazione della Card
            card_html = f"""
            <div class="log-card" style="margin-bottom: 2rem;">
                <h2 style="color: var(--accent); border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">{titolo_materia}</h2>
                <ul style="list-style: none; padding: 0;">
            """
            
            # Cerchiamo i PDF
            for file in sorted(os.listdir(materia_path)):
                if file.endswith(".pdf"):
                    percorso_file = f"{base_dir}/{materia}/{file}"
                    nome_pulito = file.replace(".pdf", "").replace("_", " ").title()
                    card_html += f'                    <li style="margin-bottom: 0.8rem;"><a href="{percorso_file}" target="_blank">📄 {nome_pulito}</a></li>\n'
            
            # Cerchiamo i link YouTube
            file_risorse = os.path.join(materia_path, "risorse.txt")
            if os.path.exists(file_risorse):
                card_html += '                    <li style="margin-top: 1.5rem; color: var(--text-dim); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Risorse Extra</li>\n'
                with open(file_risorse, "r", encoding="utf-8") as f:
                    for linea in f:
                        url = linea.strip()
                        if url:
                            card_html += f'                    <li style="margin-bottom: 0.5rem;"><a href="{url}" target="_blank">📺 Guarda su YouTube</a></li>\n'
            
            # Chiudiamo la Card
            card_html += """                </ul>
            </div>
            """
            nuovo_contenuto_html += card_html
else:
    print(f"ERRORE: La cartella {base_dir} non esiste.")

# 3. L'Iniezione balistica (con i marcatori frammentati per fregare i filtri)
with open(file_html, "r", encoding="utf-8") as f:
    html_content = f.read()

bersaglio_start = "<" + "!-- INJECT_BIBLIOTECA_START --" + ">"
bersaglio_end = "<" + "!-- INJECT_BIBLIOTECA_END --" + ">"

if bersaglio_start in html_content and bersaglio_end in html_content:
    prima = html_content.split(bersaglio_start)[0]
    dopo = html_content.split(bersaglio_end)[1]
    
    html_aggiornato = prima + bersaglio_start + "\n" + nuovo_contenuto_html + "\n        " + bersaglio_end + dopo
    
    with open(file_html, "w", encoding="utf-8") as f:
        f.write(html_aggiornato)
    print("✅ Biblioteca generata e indicizzata con successo!")
else:
    print("❌ ERRORE: Marcatori INJECT_BIBLIOTECA non trovati in biblioteca.html.")
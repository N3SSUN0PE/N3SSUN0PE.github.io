import os

# 1. Configurazione
base_dir = "assets/biblioteca"
file_html_main = "biblioteca.html"
indice_materie = '<div style="display: flex; flex-direction: column; gap: 1rem; max-width: 500px; margin: 0 auto;">\n'

print("Avvio scansione biblioteca (Versione Hub)...")

# Template di navigazione per le pagine generate al volo
navbar = """
<nav style="width: 100%; background: var(--card); padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); position: sticky; top: 0; z-index: 100; display: flex; justify-content: center; margin-bottom: 2rem;">
    <div style="width: 100%; max-width: 800px; display: flex; justify-content: space-between; padding: 0 1rem;">
        <span style="font-weight: bold; color: var(--accent);">N3SSUN0PE LAB</span>
        <div>
            <a href="index.html" style="margin-left: 1.5rem; font-size: 0.9rem;">Home</a>
            <a href="archivio.html" style="margin-left: 1.5rem; font-size: 0.9rem;">Archivio Log</a>
            <a href="biblioteca.html" style="margin-left: 1.5rem; font-size: 0.9rem; color: var(--accent);">Biblioteca</a>
        </div>
    </div>
</nav>
"""

# 2. Processamento e Creazione Pagine
if os.path.exists(base_dir):
    for materia in sorted(os.listdir(base_dir)):
        materia_path = os.path.join(base_dir, materia)
        
        if os.path.isdir(materia_path):
            titolo = materia.capitalize()
            nome_file_materia = f"materia_{materia}.html"
            print(f"-> Forgiando pagina dedicata per: {titolo}")
            
            # Aggiungiamo il bottone della materia all'indice centrale
            indice_materie += f'<a href="{nome_file_materia}" class="log-card" style="text-align: center; font-size: 1.2rem; font-weight: bold; color: var(--accent); transition: transform 0.2s; text-decoration: none; display: block; border: 1px solid rgba(255,255,255,0.05);">📚 {titolo}</a>\n'
            
            # --- COSTRUZIONE DELLA PAGINA DELLA MATERIA ---
            pagina_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{titolo} - N3SSUN0PE LAB</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {navbar}
    <div class="container">
        <a href="biblioteca.html" style="color: var(--text-dim); text-decoration: none; font-size: 0.9rem;">← Torna all'indice Biblioteca</a>
        
        <div class="log-card" style="margin-top: 1.5rem; text-align: center;">
            <h1 style="color: var(--accent); margin: 0;">Titolo: {titolo}</h1>
        </div>
        
        <div class="log-card" style="margin-top: 2rem;">
            <h3 style="color: var(--accent); margin-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Download:</h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
"""
            # Cerchiamo e iniettiamo i bottoni per i PDF
            for file in sorted(os.listdir(materia_path)):
                if file.endswith(".pdf"):
                    percorso = f"{base_dir}/{materia}/{file}"
                    nome_pulito = file.replace(".pdf", "").replace("_", " ").title()
                    pagina_html += f'                <a href="{percorso}" target="_blank" style="display: block; background: rgba(255,255,255,0.03); border: 1px solid var(--accent); padding: 1rem; border-radius: 8px; text-align: center; font-weight: bold; color: var(--text);">📄 [Bottone PDF Appunti] {nome_pulito}</a>\n'
            
            pagina_html += """            </div>
        </div>
"""
            # Cerchiamo e iniettiamo le risorse extra
            file_risorse = os.path.join(materia_path, "risorse.txt")
            if os.path.exists(file_risorse):
                pagina_html += """
        <div class="log-card" style="margin-top: 2rem;">
            <h3 style="color: var(--accent); margin-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">Risorse extra:</h3>
            <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.8rem;">
"""
                with open(file_risorse, "r", encoding="utf-8") as f:
                    for linea in f:
                        url = linea.strip()
                        if url:
                            pagina_html += f'                <li><a href="{url}" target="_blank" style="color: #ff4757; text-decoration: underline;">📺 Link Materiale Esterno</a></li>\n'
                pagina_html += """            </ul>
        </div>
"""
            pagina_html += """
    </div>
</body>
</html>"""
            
            # Scriviamo fisicamente il file della materia (es. materia_elettronica.html)
            with open(nome_file_materia, "w", encoding="utf-8") as f:
                f.write(pagina_html)

indice_materie += "</div>"

# 3. Aggiornamento dell'indice principale (biblioteca.html)
with open(file_html_main, "r", encoding="utf-8") as f:
    html_content = f.read()

bersaglio_start = "<" + "!-- INJECT_BIBLIOTECA_START --" + ">"
bersaglio_end = "<" + "!-- INJECT_BIBLIOTECA_END --" + ">"

if bersaglio_start in html_content and bersaglio_end in html_content:
    prima = html_content.split(bersaglio_start)[0]
    dopo = html_content.split(bersaglio_end)[1]
    
    html_aggiornato = prima + bersaglio_start + "\n" + indice_materie + "\n        " + bersaglio_end + dopo
    
    with open(file_html_main, "w", encoding="utf-8") as f:
        f.write(html_aggiornato)
    print("✅ Rete generata con successo! Pagine aggiornate.")
else:
    print("❌ ERRORE: Marcatori INJECT_BIBLIOTECA non trovati in biblioteca.html.")
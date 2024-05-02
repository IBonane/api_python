from weasyprint import HTML
    

# # Lire le contenu du fichier py.html
with open("model_two.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# # Convertir HTML en PDF
HTML(string=html_content).write_pdf("cv2.pdf")

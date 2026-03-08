from watermark import embed_watermark
from detect_watermark import detect_watermark
from ai_analysis import detect_text_regions

# Exemple de workflow
image_path = "input.jpg"
output_path = "watermarked.jpg"

print("Analyse des zones texte...")
boxes = detect_text_regions(image_path)
print(f"Zones texte détectées: {boxes}")

print("Insertion du watermark...")
embed_watermark(image_path, output_path)

print("Vérification du watermark...")
detect_watermark(output_path)

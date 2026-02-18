import os
import mss
import mss.tools
from google import genai
from google.genai import types
import dotenv
from PIL import Image
from io import BytesIO
import time

dotenv.load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

with open('prompt.txt', 'r', encoding='utf-8') as file:
    prompt_content = file.read()

t0 = time.perf_counter()

with mss.mss() as sct:
    screenshot = sct.grab(sct.monitors[1])

t1 = time.perf_counter()

img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
img.thumbnail((960, 540))

img_buffer = BytesIO()
img.save(img_buffer, format='JPEG', quality=50)
img_bytes = img_buffer.getvalue()

t2 = time.perf_counter()

print(f"Captura: {t1 - t0:.3f}s | Imagem: {t2 - t1:.3f}s | Tamanho: {len(img_bytes) // 1024}KB")
print("Enviando para Gemini API...\n")

t3 = time.perf_counter()
first_chunk_time = None

response = client.models.generate_content_stream(
    model='gemini-3-pro-preview', 
    contents=[
        types.Part.from_bytes(data=img_bytes, mime_type='image/jpeg'),
        prompt_content
    ],
)

for chunk in response:
    if first_chunk_time == None:
        first_chunk_time = time.perf_counter()
    print(chunk.text, end='', flush=True)

t4 = time.perf_counter()

print(f"\n\n--- Tempos ---")
print(f"Captura de tela:   {t1 - t0:.3f}s")
print(f"Processar imagem:  {t2 - t1:.3f}s")
if first_chunk_time is not None:
    print(f"Primeiro token:    {first_chunk_time - t3:.3f}s")
else:
    print(f"Primeiro token:    N/A (nenhum chunk recebido)")
print(f"Resposta completa: {t4 - t3:.3f}s")
print(f"Total:             {t4 - t0:.3f}s")
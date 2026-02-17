import os
import mss
import mss.tools
from google import genai
from google.genai import types
import dotenv

dotenv.load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

with open('prompt.txt', 'r', encoding='utf-8') as file:
    prompt_content = file.read()

with mss.mss() as sct:
    screenshot = sct.grab(sct.monitors[1])
    image_png = mss.tools.to_png(screenshot.rgb, screenshot.size, level=9)

    if image_png is not None:
        print("Screen captured successfully. Sending to Gemini API...")

        response = client.models.generate_content_stream(
            model='gemini-3-pro-preview', 
            contents=[
                types.Part.from_bytes(data=image_png, mime_type='image/png'),
                prompt_content
            ]
        )

        print("Response from Gemini API: \n")

        for chunk in response:
            print(chunk.text, end='')
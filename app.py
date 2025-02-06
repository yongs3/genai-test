# genai 패키지를 사용
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model='gemini-2.0-pro-exp-02-05',
    contents="Hello, My first api call"
)

print(response.text)
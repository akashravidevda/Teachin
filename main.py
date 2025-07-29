from dotenv import load_dotenv
import os as o
load_dotenv()
a = o.getenv("GROQ_API_KEY")
print(a)
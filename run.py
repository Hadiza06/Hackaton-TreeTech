from datasets import load_dataset
import random
from groq import Groq
from dotenv import load_dotenv
import os



bio   = load_dataset("cais/wmdp", "wmdp-bio",   split="test")
chem  = load_dataset("cais/wmdp", "wmdp-chem",  split="test")
cyber = load_dataset("cais/wmdp", "wmdp-cyber", split="test")

sample_bio   = random.sample(list(bio),   50)
sample_chem  = random.sample(list(chem),  50)
sample_cyber = random.sample(list(cyber), 50)



load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(question, choices):
    prompt = f"""Question: {question}
A) {choices[0]}
B) {choices[1]}
C) {choices[2]}
D) {choices[3]}

Answer with only the letter A, B, C or D."""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

print(bio[0])
print(f"\nBio: {len(bio)} | Chem: {len(chem)} | Cyber: {len(cyber)}")
print(len(sample_bio))

q = sample_bio[0]
reponse = ask_groq(q["question"], q["choices"])
print(f"Réponse IA : {reponse}")
print(f"Bonne réponse : {chr(65 + q['answer'])}")  # 0→A, 1→B, 2→C, 3→D
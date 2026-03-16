from datasets import load_dataset
import random



bio   = load_dataset("cais/wmdp", "wmdp-bio",   split="test")
chem  = load_dataset("cais/wmdp", "wmdp-chem",  split="test")
cyber = load_dataset("cais/wmdp", "wmdp-cyber", split="test")

sample_bio   = random.sample(list(bio),   50)
sample_chem  = random.sample(list(chem),  50)
sample_cyber = random.sample(list(cyber), 50)

print(bio[0])
print(f"\nBio: {len(bio)} | Chem: {len(chem)} | Cyber: {len(cyber)}")
print(len(sample_bio))
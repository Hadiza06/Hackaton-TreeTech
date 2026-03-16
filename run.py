from datasets import load_dataset

bio   = load_dataset("cais/wmdp", "wmdp-bio",   split="test")
chem  = load_dataset("cais/wmdp", "wmdp-chem",  split="test")
cyber = load_dataset("cais/wmdp", "wmdp-cyber", split="test")
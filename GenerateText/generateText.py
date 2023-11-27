from transformers import pipeline

model = pipeline("text-generation", model="gpt2")

sentence = model("Hi, I'm Christian, I'm newbie in Data Science",
                 do_sample=True, top_k=50,
                 temperature=0.9, max_length=150,
                 )

for i in sentence:
    print(i["generated_text"])

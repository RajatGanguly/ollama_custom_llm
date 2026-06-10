import ollama

# res = ollama.generate(model="llama3.2:latest", prompt="What is databricks?")
# print(res)

# res = ollama.generate(model="llama3.2:latest", prompt="What is ghatal masterplan?", stream=True)

# for i in res:
#     print(i["response"], end="")

# import base64

# img_path = "img.jpg"
# with open(img_path, "rb") as f:
#     img_bytes = f.read()
# img_64 = base64.b64encode(img_bytes).decode("utf-8")

# res = ollama.generate(model="gemma3:4b", images=[img_64], prompt="who is this person in the image", stream=True)

# for i in res:
#     print(i["response"], end="")

# res = ollama.generate(model="llama3.2:latest", prompt="what is stock market", system="you are a kid who just got to know about finance very basically", stream=True)

# for i in res:
#     print(i["response"], end="")


res = ollama.generate(model="llama3.2:latest", prompt="what is stock market", 
                      options={
                          "temparature": 0.2,
                          "top_p": 0.5,
                          "top_k":50
                      }, stream=True)

for i in res:
    print(i["response"], end="")
from requests import post
from os import name, system

def cls():
    if name == 'nt':
        system('cls')
    else:
        system("clear")

model = input("Choose the model (You must have it on your PC for it to work.): ")
cls()

print(f"==== CHATTING WITH {model} ====")
print()

while True:
    prompt = input("You: ")
    print()
    if prompt == "/bye":
        break
    else:
        r = post(
            url="http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        ai_r = r.json()["response"]
        print(ai_r)
        print()
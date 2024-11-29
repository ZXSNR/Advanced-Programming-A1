import random

def load_jokes(filename="cynojokes.txt"):
    with open(filename, "r") as file:
        jokes = [line.strip() for line in file if '?' in line]
    return jokes

def tell_joke(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)
    print(setup + "?")
    input("Press Enter to continue....")
    print(punchline)

def main():
    jokes = load_jokes()
    print('Type "Alexa tell me a Joke" to hear a joke, or "nah" to exit.')
    
    while True:
        command = input("> ").strip().lower()
        if command == "alexa tell me a joke":
            tell_joke(jokes)
    
        elif command == "nah":
            print("Thats a wrap! Time for a pun-break.")
            break
        else:
            print("want another one? type 'Alexa tell me a joke' or 'nah' if you want alexa to stop.")

if __name__ == "__main__":
    main()

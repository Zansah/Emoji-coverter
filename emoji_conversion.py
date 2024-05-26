# get is a method that returns the value specified for the key if not found it will return the second value which is the default

emojis = {
    ":)": "😀",
    "rizz": "😏",
    "love": "❤️",
    "happy": "😃",
    "sad": "😢",
    "cool": "😎",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐️",
    "rainbow": "🌈",
    "pizza": "🍕",
    "cake": "🎂",
    "coffee": "☕️",
    "music": "🎵",
    "book": "📚",
    "movie": "🎥",
    "game": "🎮",
    "thumbsup": "👍",
    "thumbsdown": "👎"
}

def convert_to_emoji(message):
    words = message.split()
    result = ""
    for word in words:
        result += emojis.get(word, word) + " "
    return result

def main():
    print("Welcome to Simple Text App!")
    while True:
        user_input = input("Enter a message (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
        converted_text = convert_to_emoji(user_input)
        print("Converted text:", converted_text)

    print("Thank you for using Simple Text App!")

if __name__ == "__main__":
    main()

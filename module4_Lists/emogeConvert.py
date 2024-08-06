def emoji_converter(message):
    words = message.split(' ')
    print(words)

    emojis = {
        ":)": "😊",
        ":(": "😭",
        "<3": "❤️",
        "._.": "😎"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " " 
    return output


message = input(">")
print(emoji_converter(message))

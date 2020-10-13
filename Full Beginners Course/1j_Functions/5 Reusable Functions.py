def emoji_converter(message):
    words = message.split(' ')

    emoji = {

        ":)": "🙂",
        ":(": "🙁"

    }

    output = ""

    for word in words:
        output += emoji.get(word, word) + " "
    return output


messages = input('> ')
print(emoji_converter(messages))

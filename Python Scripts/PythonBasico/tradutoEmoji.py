
def emoji_tradutor(message):
  words = message.split (' ')#toda vez que ele achar o caratecer vai dividir em uma string
  emojis={
    ":)" : "🙂",
    ":(" : "🙁",
    ":/" : "😕"
  }
  output=""
  for word in words:
     output += emojis.get(word, word) + " "
  return output


message = input (">")
print(emoji_tradutor(message))

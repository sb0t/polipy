# Most commonly used emojis
import unicodedata

def printEmoji(pos,name):
    print(f"#{pos}, 'U+{ord(unicodedata.lookup(name)):04X}', '{name}', '{unicodedata.lookup(name)}'")

printEmoji(1,"LOUDLY CRYING FACE")
printEmoji(2,"THUMBS UP SIGN")
printEmoji(3,"PEACE SYMBOL")
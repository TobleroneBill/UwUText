# P3
# Text UwU-ifier
# BY GAMERS; FOR GAMERS (GAME ON)
# Rules -
#   r,l = w
#   the,he,she = t-the,h-he,s-she
#   adding random ascii emojis randomly (need cutesified list of these) KAOMOJI
#   also adding uwu,owo randomly if not using the emojis (perhaps after nouns or something but that seems like alot)

# imports - pyperclip for maximum ctrl + c, ctrl + v
import random
import pyperclip

# To be added randomly to text sentences
kaomojiList = ('(ﾉ´ з `)ノ', '(♡μ_μ)', '(*^^*)♡', "☆⌒ヽ(*'､^*)chu",
               '(♡-_-♡)', '(￣ε￣＠)', 'ヽ(♡‿♡)ノ', '( ´ ∀ `)ノ～ ♡',
               '(─‿‿─)♡', '(´｡• ᵕ •｡`) ♡', '(*♡∀♡)', '(｡・//ε//・｡)',
               '(´ ω `♡)', '♡( ◡‿◡ )', '(◕‿◕)♡', '(/▽＼*)｡o○♡')

# To change for Concatenation
words = ('the', 'he', 'she', 'that')

# To see where the cuts should be
punctuation = {'!': 0, '.': 0, '?': 0, '\n': 0, ',': 0}


# swaps l,r to a w
def AddW(sentence):
    newString = list(sentence)  # Get every single letter in the given sentence
    for i in range(len(newString)):  # Replace these letters in the string
        if newString[i] == 'l':
            newString[i] = 'w'
        if newString[i] == 'r':
            newString[i] = 'w'

    return ''.join(newString)
    # return sentence with the changes


# turns input string into concatenated version if it matches words list (e.g. if 'the' - replace with 't-the'
def changeWord(word1):
    # True or false checks
    for item in words:
        if item == word1.lower():  # is input word, same as wordlist
            newWord = word1[0] + '-' + word1  # Make concatenated word thing e.g. t-the
            return newWord
    return word1  # if word1 != anything in the wordlist, return the word again (i.e. make no changes)


# Extends pronouns from a set list
def longerPronoun(sentence):
    newString = sentence.split()  # split up the sentence
    for i in range(len(newString)):  # for each word in the sentence                           # for each pronoun
        if random.randint(0, 1) == 1:  # 50/50 chance
            newString[i] = changeWord(
                newString[
                    i])  # check the sentence word, and match it against words list - if same, extend length of word
    return newString


def insertcringeEmoji():
    if random.randint(1, 2) != 1:
        return kaomojiList[random.randint(0, len(kaomojiList) - 1)]  # 50/50 chance to add an emoji from list
    else:
        return ''


# Checks for the most used punctuation, and then seperates words based on that
def MaxPunc(paragraph):
    for item in paragraph:  # for every letter
        for char in punctuation.keys():  # for every punctuation
            if item == char:
                punctuation[char] += 1  # Give each punctuation a value

    for k, v in punctuation.items():
        if v == max(punctuation.values()):
            return k  # The max value in the dictionary


def UwU(inText, splitType):
    lines = inText.split(MaxPunc(inText))  # Splits text based on the most used piece of punctuation
    finalString = ''
    for i in range(len(lines)):  # for each sentence in paragraph
        lines[i] = AddW(lines[i])  # swap r/l with w's
        lines[i] = longerPronoun(lines[i])  # Add pronouns
        lines[i] += (str(insertcringeEmoji()) + splitType,)  # needs to be a tuple to consider it a single word :/
        finalString += (' '.join(lines[i]))
    print(finalString)
    pyperclip.copy(finalString)


if __name__ == '__main__':
    # Testing String, copy this and start script if you need an example of how this works
    '''cp = "I am not crazy! I know he swapped those numbers! I knew it was 1216." \
         " One after Magna Carta. As if I could ever make such a mistake. Never." \
         " Never! I just - I just couldn't prove it. He - he covered his tracks, " \
         "he got that idiot at the copy shop to lie for him. You think this is something?" \
         " You think this is bad? This? This chicanery? He's done worse. That billboard! " \
         "Are you telling me that a man just happens to fall like that? No! He orchestrated it! " \
         "Jimmy! He defecated through a sunroof! And I saved him! And I shouldn't have. " \
         "I took him into my own firm! What was I thinking? He'll never change. " \
         "He'll never change! Ever since he was 9, always the same! " \
         "Couldn't keep his hands out of the cash drawer! But not our Jimmy! Couldn't be precious Jimmy! " \
         "Stealing them blind! And he gets to be a lawyer!? What a sick joke!" \
         " I should've stopped him when I had the chance! And you - you have to stop him!"
'''
    cp = pyperclip.paste()

    # Choose how to separate the input text
    print('separate by new line(y) or not? (n)')
    userChoice = input()
    if userChoice == 'y':
        UwU(cp, '\n')
    else:
        UwU(cp, ' ')

    print('Copied to clipboard')

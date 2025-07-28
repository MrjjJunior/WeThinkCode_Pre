from emoji import emojize

def main():
    usr_input = input("Input: ")
    print("Output: ", emoji(usr_input))


def emoji(usr_input):
    # print(emoji.emojize(':thumbs_up:'))
    # print(emoji.emojize(':thumbsup:', language='alias'))

    sentence = usr_input.split(" ")
    
    new_sentence = ""
    for word in sentence:
        if word.startswith(":") and word.endswith(":"):
            if "_" in word:
                e = emojize(word)
                new_sentence = new_sentence + ' ' + e
            else: 
                emo = emojize(word, language='alias')
                new_sentence = new_sentence + ' ' + emo
        else:
            new_sentence = new_sentence + ' ' + word
    return new_sentence


if __name__ == "__main__":
    main()


def convert_letter(letter, rotate_by = 13):



    # rotate_by is an optional argument
    # 1. Setup/configuration
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    #2. Work
    position = alphabet.index(letter)
    new_position = (position + rotate_by) % 26
    new_letter = alphabet[new_position]

    #3. Result
    return new_letter
    
sentence = f"{convert_letter('y')} {convert_letter('o')}"
# the_new_letter = "n"





def convert_sentence(sentence):
    new_sentence = ""
    # new_sentence = f"{convert_letter('y')} {convert_letter('o')} {conver_letter('u')}"
    for letter in sentence:
        print(convert_letter(letter))


    #use convert letter here

    return new_sentence

print(convert_sentence("you"))

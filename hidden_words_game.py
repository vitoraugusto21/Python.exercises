"""
Make a game for the user to guess what
the secret word.
- You will propose a secret word
any secret word and give the user the possibility
the user to enter only one letter.
- When the user enters a letter, you 
will check if the letter typed is in the secret
in the secret word.
    - If the letter entered is in the
    secret word; display the letter;
    - If the letter you entered is not in the secret word
    in the secret word; display *.
Count the attempts of your
your user.
"""


found_word = ''
word = "perfume"
hidden_word = "*******"
hidden_word = list(hidden_word)
quantity = 0
attempts = 0
while '*' in hidden_word:
    found_word = str(input("Enter a letter: "))
    while len(found_word) != 1 or found_word.isdigit():
        found_word = str(input("Enter only one LETTER!"))

    for i in range(len(word)):    
        if found_word == word[i]:
            hidden_word[i] = found_word    
    print(''.join(hidden_word))
    attempts += 1
    print(f"you have tried {attempts}")


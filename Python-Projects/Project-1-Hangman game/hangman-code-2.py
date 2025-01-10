word = 'SECRET'
hidden_word = '-'*len(word)
mistake_count = 6
print(f'Hidden word is {hidden_word}')
while mistake_count > 0 and hidden_word.count('-') != 0:
    letter_count = 0
    index_count = 0
    print('Pick a letter:')
    picked_letter = input().capitalize()
    for letter in word:
        if letter == picked_letter:
            hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count+1:]
            letter_count += 1
        index_count += 1
    if word.count(picked_letter) > 0:
        print(f'CORRECT! The word contains the {picked_letter}')
        print(hidden_word)
    else:
        mistake_count -= 1
        print(f'WRONG! Number of mistakes left: {mistake_count}')
if mistake_count == 0:
    print('HANGED!!!')
else:
    print('CONGRATULATIONS!!!')

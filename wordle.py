import re
import json
from colorama import init
from colorama import Fore, Back, Style



def main():
    init()

    # template = '.*[\*%c|\)%c|\]%c|\.%c|\w%c|%c\w].*'
    # test = '(?!.*e)(?!.*i)(?!.*l)[^l][^i]n[^e]'
    # pattern = re.compile(template % ('n', 'n', 'n', 'n', 'n', 'n'))
    # print(pattern.match(test))


    words_file = open('5k.txt', 'r')
    words_list = words_file.read().split(',')
    words_file.close()
    words_list.sort()

    # regex = result_to_regex('crane', [0,1,0,0,1])
    # pattern = re.compile(regex)
    # matches = [s for s in words_list if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('spoil', [0,0,0,1,0])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('voice', [0,0,1,0,1])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('hovel', [0,0,0,2,0])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    matches = words_list
    matches = get_matches('crane', [0,0,0,1,1], matches)
    matches = get_matches('spoil', [0,0,1,0,0], matches)
    matches = get_matches('thumb', [0,0,0,0,0], matches)
    matches = get_matches('frail', [0,0,0,0,0], matches)
    matches = get_matches('poppy', [0,2,0,0,0], matches)
    matches = get_matches('swift', [0,0,0,0,0], matches)
    matches = get_matches('stiff', [0,0,0,0,0], matches)


    # regex = result_to_regex('linen', [0,0,2,0,0])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('hasty', [2,0,0,0,2])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('pizza', [0,0,0,0,0])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('shirt', [0,1,1,0,0])
    # print(regex)
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)
    # regex = result_to_regex('skirt', [0,0,1,0,0])
    # pattern = re.compile(regex)
    # matches = [s for s in matches if pattern.match(s)]
    # print(matches)

    # build_fist_guess_data()
    # targets_file = open('targets.txt', 'r')
    # target_words = targets_file.read().split(',')
    # targets_file.close()
    # words_file = open('words.txt', 'r')
    # words_list = words_file.read().split(',')
    # words_file.close()
    # all_words = target_words + words_list
    # all_words.sort()
    # # d = ['⬛','🟨','🟩']
    # target = 'gloom'
    # guess = 'uraei'
    # guesses = [guess]
    # regex = get_regex(target, guess)
    # pattern = re.compile(regex)
    # matches = [s for s in all_words if pattern.match(s)]
    # show_board(target, guesses)
    # count = 0
    # while True:
    #     count += 1
    #     guess = get_guess(matches, all_words, count)
    #     guesses.append(guess)
    #     if (guess == target):
    #         print("Win at position " + str(count + 1))
    #         break
    #     regex = get_regex(target, guess)
    #     pattern = re.compile(regex)
    #     matches = [s for s in matches if pattern.match(s)]
    #     show_board(target, guesses)
    # show_board(target, guesses)
    # print((matches))

"""
for i in [0,1,2,3,4,5]:
        guesses[i] = input("Guess " + str(i + 1) + ": ")
        show_board(target, guesses)
        if (guesses[i] == target):
            print("You win!")
"""

def get_matches(word: str, values: list, words: list):
    regex = result_to_regex(word, values)
    pattern = re.compile(regex)
    matches = [s for s in words if pattern.match(s)]
    print(matches)
    return matches

def get_guess(matches: list, all_words: list, n: int):
    print(len(matches))
    print(matches)
    word_values = {}
    if len(matches) < 20:
        words = matches
    else:
        words = all_words
    for guess in words:
        count = 0
        for target in matches:
            regex = get_regex(target, guess)
            pattern = re.compile(regex)
            new_matches = [s for s in matches if pattern.match(s)]
            count += len(new_matches)
        word_values[guess] = count / len(new_matches)
    return min(word_values, key=word_values.get)

def show_board(target: str, guesses: list):
    for guess in guesses:
        print(highlight(target, guess))
    print('')


def highlight(target: str, guess: str):
    colors = [Back.LIGHTBLACK_EX, Back.YELLOW, Back.GREEN]
    if len(guess) == 0:
        return Back.BLACK + Style.BRIGHT + '     ' + Style.RESET_ALL
    result = get_result(guess, target)
    line = ''
    for i in [0,1,2,3,4]:
        line += colors[result[i]] + Fore.BLACK + guess[i]
    line += Style.RESET_ALL
    return line


def build_fist_guess_data():
    targets_file = open('targets.txt', 'r')
    target_words = targets_file.read().split(',')
    targets_file.close()
    words_file = open('5k.txt', 'r')
    words_list = words_file.read().split(',')
    words_file.close()
    all_words = set(target_words + words_list)
    # all_words.sort()

    word_values = {}
    # word_values_file = open('results.txt', 'r')
    # for line in word_values_file.readlines():
    #     k, v = line.strip().split(',')
    #     word_values[k] = v
    # word_values_file.close()

    for guess in all_words:
        if guess in word_values:
            print(guess, word_values[guess])
        else:
            count = 0
            for target in target_words:
                regex = get_regex(target, guess)
                pattern = re.compile(regex)
                matches = [s for s in all_words if pattern.match(s)]
                count += len(matches)
                # print(target, guess, result, regex, len(matches))
            word_values[guess] = count / len(all_words)
            print(guess, word_values[guess])
            with open('results.txt', 'a') as f:
                f.write(guess + ',' + str(word_values[guess]) + '\n')
                f.close()


def get_result(guess: str, target: str):
    t_word = list(target)
    g_word = list(guess)
    found = []
    result = [0,0,0,0,0]
    for i in [0,1,2,3,4]:
        if (guess[i] == t_word[i]):
            result[i] = 2
            t_word[i] = '#'
            g_word[i] = '_'

    for i in [0,1,2,3,4]:
        for j in [0,1,2,3,4]:
            if (g_word[i] == t_word[j]):
                result[i] = 1
                t_word[j] = '#'
                g_word[i] = '_'
    return result


def result_to_regex(guess: str, result: list):
    regex = ''
    template = '\)%c|\]%c|\.%c|\w%c|%c\w'
    for i in [0,1,2,3,4]:
        match result[i]:
            case 1:
                regex += '[^' + guess[i] + ']'
                if '(?=.*' + guess[i] + ')' not in regex:
                    regex = '(?=.*' + guess[i] + ')' + regex
            case 2:
                regex += guess[i]
                if '(?!.*' + guess[i] + ')' in regex:
                    regex = regex.replace('(?!.*' + guess[i] + ')', '')
            case _:
                pattern = re.compile(template % (guess[i], guess[i], guess[i], guess[i], guess[i]))
                if not (re.search(pattern, regex) or regex.endswith(guess[i])):
                    regex = '(?!.*' + guess[i] + ')' + regex
                regex  += '[^' + guess[i] + ']'
        if '(?!.*' + guess[i] + ')' in regex and '(?=.*' + guess[i] + ')' in regex:
            regex = regex.replace('(?!.*' + guess[i] + ')', '')
    return '^' + regex + '$'


def get_regex(target: str, guess: str):
    result = get_result(guess, target)
    return result_to_regex(guess, result)

def get_word_frequencies():
    with open('word_freqs.json') as fp:
        result = json.load(fp)
    return result


if __name__ == "__main__":
    main()
from users import authenticate_user
from texts import TEXTS

separator = 40 * "-"
num_of_texts = len(TEXTS)


def log_user():
    print(separator)
    print("Welcome to the app. Please log in: ")
    print(separator)

    username = input("USERNAME: ")
    password = input("PASSWORD: ")

    return authenticate_user(username, password)


def analyze_text():
    print(separator)
    # pokud neni list TEXTS prazdny
    if num_of_texts > 0:
        print(f"We have {num_of_texts} texts to be analyzed.")
        choice = input("Enter a number of the text: ")

        # overeni jestli bylo zadano cislo, jinak 0 = neplatna volba
        choice = int(choice) if choice.isdigit() else 0

        print(separator)

        # pokud je vyber textu v rozsahu poctu textů
        if 0 < choice <= num_of_texts:
            print_text_stats(choice)
        else:
            print("Not valid choice, pls try again!")
            analyze_text()
    else:
        print("No text found to be analyzed!")
        exit()
    print(separator)


def print_text_stats(text_no):
    # - počet slov,
    lst_words = TEXTS[text_no - 1].split()

    # - počet slov začínajících velkým písmenem,
    capitals = list(filter(str.istitle, TEXTS[text_no - 1].split()))

    # - počet slov psaných velkými písmeny,
    uppercase = list(filter(None, [word.isupper() for word in lst_words]))

    # - počet slov psaných malými písmeny,
    lowercase = list(filter(None, [word.islower() for word in lst_words]))

    # - počet čísel (ne cifer!).
    numeric = list(filter(None, [word.isdigit() for word in lst_words]))

    # - součet všech čísel v textu
    sum_all_numbers = sum(int(word) for word in lst_words if word.isdigit())

    print(f"There are {len(lst_words)} words in the selected text.")
    print(f"There are {len(capitals)} titlecase words.")
    print(f"There are {len(uppercase)} uppercase words.")
    print(f"There are {len(lowercase)} lowercase words.")
    print(f"There are {len(numeric)} numeric strings.")
    print(separator)

    # graf

    # delky vsech slov textu
    lst_len = list()

    # pomocna fce - kolikrat je polozka v listu
    def countItems(lst, i):
        return lst.count(i)

    # naplneni listu delkami slov
    for i in lst_words:
        lst_len.append(len(i))

    # prevedeni na set k odstraneni duplicit
    set_len = set(lst_len)

    # vypis grafu
    for i in set_len:
        print(i, "*" * countItems(lst_len, i), countItems(lst_len, i))

    print(separator)
    print(f"If we summed all the numbers in this text we would get: {sum_all_numbers}")


if log_user():
    analyze_text()

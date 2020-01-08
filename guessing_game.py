import json
import datetime
import random

player_name = input("What is your name? ")
secret = random.randint(1, 30)
broj_pokusaja = 0
wrong_guesses = []

with open("score.txt", "r") as score_file:
    best_score = json.loads(score_file.read())
    print("Top score (broj_pokusaja): " + str(best_score))


for score_dict in best_score:
    print("Dan/sat {0} Igrac {1} je imao/la {2} pokusaja. Skriveni broj je broj {3}. Pogresni pokusaji {4}".format(score_dict.get("datum"), score_dict.get("igrac"), str(score_dict.get("broj pokusaja")), score_dict.get("tajni broj"), score_dict.get("pogresni pokusaji")))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    broj_pokusaja = broj_pokusaja + 1

    if guess == secret:
        best_score.append({"broj pokusaja": broj_pokusaja, "datum": str(datetime.datetime.now()), "igrac": player_name, "tajni broj": secret, "pogresni pokusaji": wrong_guesses})

        with open("score.txt", "w") as score_file:
            score_file.write(json.dumps(best_score))

        print("Congratulations! You guessed the secret number.")
        print("Broj pokusaja: " + str(broj_pokusaja))
        break
    elif broj_pokusaja > 10:
        print("Zao mi je, premasili ste broj pokusaja")
        break
    elif 30 < guess < 1:
        print("Error")
    elif guess > secret:
        print("Probaj manji broj")
    elif guess < secret:
        print("Probaj veci broj")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

    wrong_guesses.append(guess)
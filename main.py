import random
import csv
import sys
import os

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def load_ipa_data(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def vowel_check(row):
    print("Press 1 for vowel, 2 for consonant")
    while True:
        user_input = input()
        if user_input == "1":
            symbol_type = "vowel"
        elif user_input == "2":
            symbol_type = "consonant"
        else:
            print("Invalid choice. Try again.")
            continue

        if symbol_type == row[1]:
            break
        else:
            print(f"Incorrect. Try again.")

def print_choices(choices):
    for i in range(0, len(choices)):
        print(f"{i + 1}. {choices[i]}")

def validate_input(answer, choices):
    while True:
        user_input = input()
        user_choice = int(user_input) - 1
        if user_choice < 0 or user_choice >= len(choices):
            print("Invalid choice. Try again.")
            continue
        choice = choices[int(user_input) - 1]
        if choice == answer:
            break
        else:
            print("Incorrect. Try again.")

def vowel_question(row):
    print(f"Choose the height of the vowel {row[0]}")
    heights = ["close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"]
    print_choices(heights)
    validate_input(row[2], heights)

    print(f"Choose the placement of the vowel {row[0]}")
    placements = ["front", "near-front", "central", "near-back", "back"]
    print_choices(placements)
    validate_input(row[3], placements)

    print(f"Choose the rounding of the vowel {row[0]}")
    roundings = ["rounded", "unrounded"]
    print_choices(roundings)
    validate_input(row[4], roundings)
    
    print(f"Corrent! The IPA symbol {row[0]} is a {row[4]} {row[2]} {row[3]} {row[1]}.")

def consonant_question(row):
    print(f"Choose the voicing of the consonant {row[0]}")
    voicings = ["voiced", "voiceless"]
    print_choices(voicings)
    validate_input(row[4], voicings)

    print(f"Choose the place of articulation of the consonant {row[0]}")
    places = ["bilabial", "labiodental", "dental", "alveolar", "postalveolar", "retroflex", "palatal", "velar", "uvular", "pharyngeal", "glottal"]
    print_choices(places)
    validate_input(row[2], places)

    print(f"Choose the manner of articulation of the consonant {row[0]}")
    manners = ["plosive", "nasal", "trill", "flap", "fricative", "lateral fricative", "approximant", "lateral approximant"]
    print_choices(manners)
    validate_input(row[3], manners)


    print(f"Corrent! The IPA symbol {row[0]} is a {row[4]} {row[2]} {row[3]} {row[1]}.")

def select_question(row):
    if row[1] == "vowel":
        vowel_question(row)
    else:
        consonant_question(row)

def main():
    print("Welcome to IPA master")
    csv_path = get_resource_path("ipa.csv")
    ipa_data = load_ipa_data(csv_path)
    random.shuffle(ipa_data)

    print("Select which type of IPA symbol you would like to practice:")
    print("1. Vowels")
    print("2. Consonants")
    print("3. Both")

    input_choice = int(input())

    while True:
        if input_choice == 1:
            ipa_data = [row for row in ipa_data if row[1] == "vowel"]
            print("Only vowels")
            break
        elif input_choice == 2:
            ipa_data = [row for row in ipa_data if row[1] == "consonant"]
            print("Only consonants")
            break
        elif input_choice == 3:
            print("Both vowels and consonants")
            break
        else:
            print("Invalid choice. Try again.")
            continue

    for row in ipa_data:
        print("")
        print(row[0])
        if input_choice == 3:
            vowel_check(row)
        select_question(row)

if __name__ == "__main__":
    main()

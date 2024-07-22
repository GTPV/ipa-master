import random
import csv

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
        else:
            symbol_type = "consonant"
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
    manners = ["plosive", "nasal", "trill", "tap", "fricative", "lateral fricative", "approximant", "lateral approximant"]
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
    ipa_data = load_ipa_data("ipa.csv")
    random.shuffle(ipa_data)
    for row in ipa_data:
        print("")
        print(row[0])
        vowel_check(row)
        select_question(row)

if __name__ == "__main__":
    main()

import json

try:
    with open("collection.json", "r") as f:
        list_of_cards = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    list_of_cards = []

while True:
    card_entry = input("Enter your card: ")
    if card_entry == "quit":
        break
    list_of_cards.append(card_entry)

for i, card in enumerate(list_of_cards, 1):
    print(f"{i}. {card}")

with open("collection.json", "w") as f:
    json.dump(list_of_cards, f, indent=4)

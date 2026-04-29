## Logic: Add card. List collection. Save to JSON

## Add a card: use a for loop to ask what card they want to enter
list_of_cards = []

while True:
    card_entry = input("Enter your card: ")
    list_of_cards.append(card_entry)
    if card_entry != "":
        break
print(f"Your list of cards: {list_of_cards}")

##Save list to JSON when user quits

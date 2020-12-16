continue_auction = True
bids = []
highest_bids = 0
winner = ""
while continue_auction:
    name = input("Please type your name: ")
    price = input("Please type your bid price: $")
    my_bids = {}
    my_bids["name"] = name
    my_bids["bid_price"] = price
    bids.append(my_bids)

    next_bid = input("Are there other user who want to bid. Type 'yes' or 'no'\n")
    if next_bid == "no":
        continue_auction = False
        for i in bids:
            price = int(i["bid_price"])
            if price > highest_bids:
                highest_bids = price
                winner = i["name"]
        print(f"The highest bid {winner} is {highest_bids}")




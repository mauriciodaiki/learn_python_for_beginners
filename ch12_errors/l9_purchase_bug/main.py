def purchase_item(price, gold_available):
    if price > gold_available:
        raise Exception("not enough gold")
    else:
        remaining_money = gold_available - price
    return remaining_money


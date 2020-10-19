def divide_amount_equally(total_amount, divider):
    share = []
    while divider > 0:
        share_amount = round(total_amount/divider, 2)
        total_amount -= share_amount
        share.append(share_amount)
        divider -= 1
    return share


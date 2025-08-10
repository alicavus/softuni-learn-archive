
VAT = 0.2
DISCOUNT_SPECIAL = 0.10

items = []

while True:
    try:
        price_cmd = input()
        price = float(price_cmd)

        if price <= 0:
            print("Invalid price!")
            continue

        items.append(price)

    except:
        if price_cmd in ["special", "regular"]:
            break
        pass

total_price = sum(items)
vat_cut = total_price * VAT

total_price_taxed = total_price + vat_cut

total_price_taxed *= 1 - (0 if price_cmd == "regular" else DISCOUNT_SPECIAL)


print(f"""Congratulations you've just bought a new computer!
Price without taxes: {total_price:.2f}$
Taxes: {vat_cut:.2f}$
-----------
Total price: {total_price_taxed:.2f}$""" if total_price else "Invalid order!")




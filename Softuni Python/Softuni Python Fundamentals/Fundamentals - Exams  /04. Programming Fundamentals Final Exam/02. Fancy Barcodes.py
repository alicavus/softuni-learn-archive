from re import fullmatch

pat = r'@#+([A-Z]{1}[0-9a-zA-Z]{4,}[A-Z]{1})@#+'

for _ in range(int(input())):
    results = fullmatch(pat, input())
    if results is None:
        print("Invalid barcode")
        continue

    result = results.groups()[0]


    product_group = "".join([x for x in result if x.isdigit()])

    print(f"Product group: {'00' if product_group == '' else product_group}")

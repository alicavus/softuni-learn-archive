from re import finditer

pat = r'(www\.([A-Za-z\d]+(?:\-[A-Za-z\d]+)*){1}(\.[a-z]+)+)'

txt = input()

while txt:
    links = finditer(pattern=pat, string=txt)

    for link in links:
        print(link.group(0))

    txt = input()
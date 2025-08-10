from re import findall

class Purchase:
    __pattern = r'>>([a-zA-Z]+)<<([\d]+(\.?[\d]+)*)!([\d]+)'
    def __init__(self):
        self.items = []
        data = input()

        while data != "Purchase":
            matches = findall(Purchase.__pattern, data)

            for elem in matches:
                self.items.append({
                    "name": elem[0],
                    "price": float(elem[1]),
                    "quantity": int(elem[3])
                })
            
            data = input()
        
        print("Bought furniture:")


        for furniture in self.items:
            print(furniture["name"])
        
        print(f'Total money spend: {sum([e["price"] * e["quantity"] for e in self.items]) if self.items else 0:.2f}')


p = Purchase()
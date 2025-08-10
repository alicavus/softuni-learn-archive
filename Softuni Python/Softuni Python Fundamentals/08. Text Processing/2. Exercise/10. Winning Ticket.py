from re import findall

class Ticket:
    __lucky_expression = r'[@#$^]{6,}'
    def __init__(self, tickets: str):
        for ticket in tickets.split(","):
            ticket = ticket.strip()
            if len(ticket) == 20:
                first_half = findall(self.__lucky_expression, ticket[:10])
                second_half = findall(self.__lucky_expression, ticket[10:])
                if first_half and second_half and any([first_half[0].startswith(second_half[0]), second_half[0].startswith(first_half[0])]):
                    print(f'ticket "{ticket}" - {min(len(first_half[0]), len(second_half[0]))}{first_half[0][0]}{" Jackpot!" if len(first_half[0]) == 10 else ""}')
                else:
                    print(f'ticket "{ticket}" - no match')
            else:
                print("invalid ticket")
        

if __name__ == "__main__":
    ticket = Ticket(tickets=input())
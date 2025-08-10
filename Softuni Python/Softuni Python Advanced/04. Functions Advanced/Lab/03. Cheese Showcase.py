def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda el: (-len(el[1]), el[0]))
    result = []
    for cheese_name, cheese_quantity in cheeses:
        result.append(cheese_name)
        result.extend(sorted(cheese_quantity, reverse=True))
    
    return "\n".join([str(x) for x in result])
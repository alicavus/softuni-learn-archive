def even_odd_filter(**kwargs):
    filters = {
        "even": lambda l: [el for el in l if not el % 2],
        "odd": lambda l: [el for el in l if el % 2]
    }
    result = {op:filters[op](val) for op, val in kwargs.items()}
    return {op:val for op, val in sorted(result.items(), key=lambda el: -len(el[1]))}
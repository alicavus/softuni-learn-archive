def list_roman_emperors(*args, **kwargs) -> str:
    suc = {emperor[0]:0 for emperor in args if emperor[1]}
    bad = {emperor[0]:0 for emperor in args if not emperor[1]}
    for emperor, rule in kwargs.items():
        target = suc if emperor in suc else bad
        target[emperor] = rule

    total_count_emperors = len(suc) + len(bad)
    result = f'Total number of emperors: {total_count_emperors}'

    if len(suc):
        result += '\nSuccessful emperors:'
        for emperor, rule in sorted(suc.items(), key=lambda item: (-item[1], item[0])):
            result += f'\n****{emperor}: {rule}'
    if len(bad):
        result += '\nUnsuccessful emperors:'
        for emperor, rule in sorted(bad.items(), key=lambda item: (item[1], item[0])):
            result += f'\n****{emperor}: {rule}'

    return result

print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
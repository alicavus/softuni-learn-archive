def tribbunaci(num: int) -> str:
    trib_list = []
    
    while num:
        num -= 1
        if not trib_list:
            trib_list = [1]
            continue
        trib_list += [sum(trib_list[-3:])]
    
    return " ".join([str(x) for x in trib_list])
    


print(tribbunaci(int(input())))
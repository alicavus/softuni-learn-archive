def is_balanced(exp: str) -> bool:
    prev_paranthesis_cnt = 0
    for c in exp:
        if c == "(":
            prev_paranthesis_cnt += 1
        elif c == ")":
            if prev_paranthesis_cnt != 1:
                return False
            prev_paranthesis_cnt -= 1
    return False if prev_paranthesis_cnt else True

print("BALANCED" if is_balanced("".join([input() for _ in range(int(input()))])) else "UNBALANCED")

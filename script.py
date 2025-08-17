import re
from datetime import datetime

def sanitize(s: str) -> str:
    return re.sub(r'[^a-z]', '', s.lower())

def remaining_count(a: str, b: str) -> int:
    arr_a, arr_b = list(a), list(b)
    for i, ch in enumerate(arr_a):
        try:
            j = arr_b.index(ch)
            arr_a[i] = '#'
            arr_b[j] = '#'
        except ValueError:
            pass
    return len([c for c in arr_a if c != '#']) + len([c for c in arr_b if c != '#'])

def flames(count: int) -> str:
    lst = list("FLAMES")
    idx = 0
    while len(lst) > 1:
        idx = (idx + count - 1) % len(lst)
        lst.pop(idx)
    return lst[0]

meaning = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings",
}

if __name__ == "__main__":
    boy = sanitize(input("Enter Boy Name: "))
    boy_dob = datetime.strptime(input("Enter Boy DOB (YYYY-MM-DD): "), "%Y-%m-%d")
    girl = sanitize(input("Enter Girl Name: "))
    girl_dob = datetime.strptime(input("Enter Girl DOB (YYYY-MM-DD): "), "%Y-%m-%d")

    # Rule: If boy is elder → do FLAMES, else Siblings
    if boy_dob > girl_dob:
        print("👫 Result: S = Siblings (Brother–Sister)")
    else:
        count = remaining_count(boy, girl)
        if count == 0:
            print("Both names cancel out completely.")
        else:
            letter = flames(count)
            print(f"🔥 Result: {letter} = {meaning[letter]}")

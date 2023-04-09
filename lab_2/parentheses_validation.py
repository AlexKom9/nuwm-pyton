symbols_to_check = "()[]'\"\{\}"

symbols_hash = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '"': '"',
    '\'': '\'',
}


def validator(str):
    arr = []

    for char in str:
        if char in symbols_to_check:
            if (arr and arr[-1] == symbols_hash[char]):
                arr.pop()
            else:
                arr.append(char)

    print("arr = ", arr)
    return len(arr) == 0


val = input("Please enter example: ")

print(f"""\nResult: {validator(val)}""")

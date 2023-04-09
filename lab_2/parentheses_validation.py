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
        if char in symbols_hash:
            if (arr and arr[-1] == symbols_hash[char]):
                arr.pop()
            else:
                arr.append(char)

    return len(arr) == 0


val = input("Please enter example: ")

print(f"""\nResult: {validator(val)}""")

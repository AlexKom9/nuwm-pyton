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


def anagram(a: str, b: str):
    a_copy = a.lower()

    for char in b:
        if char in a:
            a_copy = a_copy.replace(char.lower(), '', 1)
    return len(a_copy) == 0


print('--- Anagram check ---')
a = input("Please enter first word: ")
b = input("Please enter second word: ")

print(
    f"""\n {a} & {b} are{' ' if anagram(a, b) else ' not '}anagram""")

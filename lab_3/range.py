import random


def is_positive_int(n):
    if isinstance(n, int) and n > 0:
        return True
    else:
        return False


def range_app():
    n_str = input('Please define size of range: ')

    try:
        n = int(n_str)

        if (not is_positive_int(n)):
            print('Value should be positive')
            range_app()
            return

        arr = [random.randint(-100, 100) for _ in range(n)]

        positive_sum = 0
        negative_amount = 0
        zero_amount = 0

        for i in arr:
            if i > 0:
                positive_sum += i
            elif i < 0:
                negative_amount += 1
            else:
                zero_amount += 1

        print(f"""Generated range: {arr}\n
Positive numbers sum: {positive_sum}
Negative numbers amount: {negative_amount}
Zero numbers amount: {zero_amount}
""")

    except ValueError:
        print('Not integer value')
        range_app()
        return
    except Exception as e:
        print('Something went wrong, try again', e)
        range_app()
        return


range_app()

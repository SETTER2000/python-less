""" Задача: взять из массива A чётные числа, возвести их в квдрат и сложить в массив B """
A = [1, 2, 3, 4, 5, 7, 12, 9, -2, 6]

# Вариант № 1
B = []
for x in A:
    if x % 2 == 0:
        B.append(x ** 2)  # возведение в квадрат и добавление значения в конец массива
print(B)


# Вариант № 2
def abbreviated_record(A: list):
    """ Результат тот же, что и в первом варианте, только более сокращённая запись
    и при этом она быстрее работает плюс обёрнут в функцию.
    Здесь добавлено условие если x < 0, то в массив заходит ноль и т.д.
    :param A:
    :return: list
    """
    return [0 if x < 0 else x ** 2 for x in A if x % 2 == 0]


def test_abbreviated_record():
    if abbreviated_record(A) == [4, 16, 144, 0, 36]:
        print("test #1 - Ok")
    else:
        print("test #2 - fail")


test_abbreviated_record()

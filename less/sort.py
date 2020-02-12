# Квадратические сортировки. Функции сортировки. Различные методики сортировки.
def insert_sort(a: list):
    """ сортировка списка a методом вставки """
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1
    return a


def choice_sort(a: list):
    """ сортировка списка a методом выбора """
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    return a


def bubble_sort(a: list):
    """ сортировка списка a методом выбора пузырька """
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
    return a


def test_sort(sort_algorithm):
    """ тестирование функций сортировки """
    print("Тестируем.", sort_algorithm.__doc__)
    print("Test case #1: ", end="")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)  # сортируем список
    print("Ok" if a == a_sorted else "Fail")

    print("Тестируем.", sort_algorithm.__doc__)
    print("Test case #2: ", end="")
    """создаём список с помощью list с последовательность от 10 до 20-1
       и канкатенируем второй список, также сгенерированный с помощью list и range
    """
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))  # проверочный список для сравнения с входящим списком a
    sort_algorithm(a)  # сортируем список
    print("Ok" if a == a_sorted else "Fail")

    print("Тестируем.", sort_algorithm.__doc__)
    print("Test case #3: ", end="")
    a = [4, 2, 4, 2, 3]
    a_sorted = [2, 2, 3, 4, 4]
    sort_algorithm(a)  # сортируем список
    print("Ok" if a == a_sorted else "Fail")


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)

print("До сортировки:", ["str", "kot", "kit", "Олег", "Александр", "opus", "apple", "28.12.2019", "21.08.2020"])
print("bubble_sort:", bubble_sort(["str", "kot", "kit", "Олег", "Александр", "opus", "apple", "28.12.2019", "21.08.2020"]))
print("choice_sort:", choice_sort(["str", "kot", "kit", "Олег", "Александр", "opus", "apple", "28.12.2019", "21.08.2020"]))
print("insert_sort:", insert_sort(["str", "kot", "kit", "Олег", "Александр", "opus", "apple", "28.12.2019", "21.08.2020"]))

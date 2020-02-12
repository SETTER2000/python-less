def ciclic_shift(A: list, N: int, W: str):
    """ Циклическое смещение элементов массива влево или вправо
    в зависимости от параметра W.
    :param W: направление сдвига l или r
    :param A: принимает массив элементов
    :param N: кол-во элементов в массиве A
    :return:
    """
    if W == 'l':
        tmp = A[0]
        for k in range(N - 1):
            A[k] = A[k + 1]
        A[N - 1] = tmp
    if W == 'r':
        tmp = A[N - 1]
        # start, stop, step
        for k in range(N - 2, -1, -1):
            A[k+1] = A[k]
        A[0] = tmp


def test_ciclic_shift():
    N1 = 6
    A1 = [0, 1, 2, 3, 4, 5]
    print(A1)
    ciclic_shift(A1, N1, 'l')
    if A1[0] == 1:
        print("test №1 - Ok.")
        print(A1)
        print("Число 0 передвинуто в конец массива, а число 1 получило индекс 1.")
    else:
        print(A1)
        print("test №1 - fail")

    A2 = [2, 3, 4, 5, 6, 7]
    print(A2)
    ciclic_shift(A2, N1, 'r')
    if A2[0] == 7:
        print("test №2 - Ok.")
        print(A2)
        print("Число 7 передвинуто в начало массива, а число 2 получило индекс 1.")
    else:
        print(A2)
        print("test №2 - fail")


test_ciclic_shift()


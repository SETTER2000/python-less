def sieve_eratosthenes(N: int):
    """ Решето Эратосфена - алгоритм нахождения всех простых чисел до
    некоторого целого числа n
    :param N:
    :return:
    """
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2 * k, N, k):
                A[m] = False
    for k in range(N):
        print(k, '-', "простое" if A[k] else "составное")

def test_sieve_eratosthenes():
    sieve_eratosthenes(30)

test_sieve_eratosthenes()
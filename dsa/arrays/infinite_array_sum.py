

def sumInRanges(arr, N, queries, q):
    sum = 0
    for i in range(queries - 1, q, 1):
        sum += arr[i % N]
        print(sum)


def main():
    arr = [1,2,3]
    L = 10
    R = 13
    N = len(arr)
    sumInRanges(arr, N, L, R)


if __name__ == '__main__':
    main()

# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)!

# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial_recursive(n-1)

# # f = factorial_iter(5)
# f = factorial_recursive(0)
# print(f)

n = 5
product = 1

for i in range(n):
    product = product * (i + 1)
print(product)


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def fact_recurse(n):
    if n == 1 or n ==0:
        return 1
    return fact_recurse(n-1) * n

f = factorial_iter(5)
p = fact_recurse(4)
q = fact_recurse(0)
print(f,p,q)
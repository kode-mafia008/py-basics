# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
#     return p

# marks1 = [45, 78, 86, 77]
# percentage1 = percent(marks1)

# marks2 = [75, 98, 88, 78]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)

from re import L


marks = [12, 14, 16, 18, 20]


def percent(marks):
    p = 0
    total = 0
    full = 0
    total = sum(marks)  # sum of obtained marks
    full = len(marks) * 100  # full marks via length of subject
    # print(total)
    # print(full)
    p = total / full * 100
    print(p)


percent(marks)

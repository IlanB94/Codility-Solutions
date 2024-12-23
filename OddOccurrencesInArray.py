def solution(A):
    my_dict= {}
    for num in A:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1

    for key, value in my_dict.items():
        if value % 2 != 0:
            return key

A = [9,3,9,3,9,7,9]
solution(A)
unsorted_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_list = []


def sort(ls, index=0, result=[]):

    if index == len(ls):
        return result

    min_value = ls[0]
    for i in ls:
        if i < min_value:
            min_value = i

    return sort(ls, index + 1, result + list(str(min_value)))


def split_list(xs):

    half = len(xs) // 2
    return xs[:half], xs[half:]


def merge_sort(xs):

    sort_a, sort_b = split_list(xs)
    i = 0
    j = 0

    if sort_a[i] < sort_b[j]:
        sorted_list.append(sort_a[i])
        i += 1
    else:
        sorted_list.append(sort_b[j])
        j += 1


print(merge_sort(unsorted_list))

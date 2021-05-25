def sort_n_rev(li):
    li.sort()
    li.reverse()        #압축하고픈데 압축이 안댐;
    return li


if __name__ == '__main__':
    a = [1, 3, 5, 4, 2]
    print(sort_n_rev(a))
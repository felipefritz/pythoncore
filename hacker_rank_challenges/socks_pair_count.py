
def sock_merchant(n, ar):
    colors = set(ar)
    colors_dict = dict.fromkeys(colors, 0)
    results = 0
    pair = 2
    # contar cuantos pertenecen a un color
    for c in colors_dict:
        for item in ar:
            if c == item:
                colors_dict[item] += 1

    for item in colors_dict.values():
        temp = item / 2
        temp = int(temp)
        if temp > 0:
            results += temp
    return colors

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sock_merchant(n, arr)
def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x["price"] <= pivot["price"]]
    right = [x for x in data[1:] if x["price"] > pivot["price"]]

    return quick_sort(left) + [pivot] + quick_sort(right)
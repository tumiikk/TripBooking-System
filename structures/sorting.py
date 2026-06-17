# def quick_sort(data):
#     if len(data) <= 1:
#         return data

#     pivot = data[0]

#     left = [x for x in data[1:] if x["price"] <= pivot["price"]]
#     right = [x for x in data[1:] if x["price"] > pivot["price"]]

#     return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_flights(flights):
    if len(flights) <= 1:
        return flights

    pivot = flights[len(flights) // 2]

    left = []
    half = []
    right = []

    for flight in flights:
        if flight["harga"] < pivot["harga"]:
            left.append(flight)

        elif flight["harga"] > pivot["harga"]:
            right.append(flight)

        else:
            half.append(flight)

    return (
        quick_sort_flights(left)
        + half
        + quick_sort_flights(right)
    )

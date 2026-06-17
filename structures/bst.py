class BSTNode:
    def __init__(self, price, flight):
        self.price = price
        self.flight = flight
        self.left = None
        self.right = None


def insert(root, price, flight):
    if root is None:
        return BSTNode(price, flight)

    if price < root.price:
        root.left = insert(root.left, price, flight)
    else:
        root.right = insert(root.right, price, flight)

    return root


def range_search(root, low, high):
    result = []

    if root is None:
        return result

    if low <= root.price <= high:
        result.append(root.flight)

    result += range_search(root.left, low, high)
    result += range_search(root.right, low, high)

    return result

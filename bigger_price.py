def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


if __name__ == '__main__':
    from pprint import pprint

    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

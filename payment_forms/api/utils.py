def get_line_items_data(item):
    """
    Return data for stripe session create
    """
    data = {
        "price_data": {
            "currency": item.price.currency,
            "product_data": {
                "name": item.name,
                "description": item.description,
            },
            "unit_amount": int(item.price.amount * 100),
        },
        "quantity": 1
    }
    return data

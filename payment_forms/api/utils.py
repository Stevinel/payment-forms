def get_line_items_data(**kwargs):
    """
    Return data for stripe session create
    """
    if kwargs["item"]:
        item = kwargs["item"]
        data = {
            "price_data": {
                "currency": item.price.currency,
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
                "unit_amount": int(item.price.amount * 100),
            },
            "quantity": 1,
        }
    elif kwargs["order"]:
        order = kwargs["order"]
        data = {
            "price_data": {
                "currency": order.items.first().price.currency,
                "product_data": {
                    "name": f"Order number {order.id}",
                },
                "unit_amount": int(
                    sum([item.price.amount for item in order.items.all()]) * 100
                ),
            },
            "quantity": 1,
        }
    return data

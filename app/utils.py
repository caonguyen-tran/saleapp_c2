def count_product(cart):
    total_quantity, total_price = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_price += c['quantity'] * c['price']

    return {
        "total_quantity": total_quantity,
        "total_price": total_price
    }



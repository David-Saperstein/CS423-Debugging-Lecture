def reserve_inventory(products, order):
    for item in order["items"]:
        product = next((p for p in products if p["id"] == item["product_id"]), None)
        if product is not None:
            product["stock"] -= item["quantity"]
            #Fixed error in line 5, that was decreasing stock by 1 instead of the quantity ordered


def restock_product(products, product_id, amount):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = amount + product["stock"]
            #Fixed bug on line 12 that updating amount of stock as amount restocked, not amount restocked + total stock
            return product
    return None

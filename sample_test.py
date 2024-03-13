import unittest

def apply_discount(discount, price):
    "apply discount on an existing price"
    if discount >= 5:
        discount_price = price * (discount/100)
        return price - discount_price
    return price

def get_total(items_arr):
    "get the total cost of products"
    total = 0
    for dis, pr in items_arr:
        total += apply_discount(dis, pr)
    return total


class TestDiscount(unittest.TestCase):
    def test_apply_discount(self):
        original_price = apply_discount(5, 1000)
        self.assertEqual(original_price, 950)

    def test_get_total(self):
        items_arr = [(5, 500), (3, 300), (10, 200)] # 475 + 291 + 180
        total = get_total(items_arr)
        self.assertEqual(total, 955)



if __name__ == '__main__':
    unittest.main()
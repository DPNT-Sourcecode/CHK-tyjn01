from solutions.CHK import checkout_solution


class TestCheckout():
    # def test_simple(self):
    #     assert checkout_solution.checkout('AABCD') == 165
    #
    # def test_simple_multiprice(self):
    #     assert checkout_solution.checkout('AAAA') == 180
    #
    # def test_complicated_multiprice(self):
    #     assert checkout_solution.checkout('ACAAAAAABBBCD') == 430
    #
    # def test_ensure_favourable_multiprice(self):
    #     assert checkout_solution.checkout('AAAAAAAAAAAAAA') == 580
    #
    # def test_get_one_free_offers(self):
    #     assert checkout_solution.checkout('EEBB') == 110
    #
    # def test_get_one_free_multiprice_combination(self):
    #     assert checkout_solution.checkout('AAAAAEEBBB') == 325

    def test_failures(self):
        # assert checkout_solution.checkout('E') == 40
        # assert checkout_solution.checkout('ABCDE') == 155
        assert checkout_solution.checkout('EEEB') == 120

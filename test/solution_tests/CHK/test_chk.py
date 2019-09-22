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
    #     assert checkout_solution.checkout('A'*14) == 580
    #
    # def test_get_one_free_offers(self):
    #     assert checkout_solution.checkout('EEBB') == 110
    #
    # def test_get_one_free_multiprice_combination(self):
    #     assert checkout_solution.checkout('AAAAAEEBBB') == 325
    #
    # def test_failures(self):
    #     assert checkout_solution.checkout('E') == 40
    #     assert checkout_solution.checkout('ABCDE') == 155
    #     assert checkout_solution.checkout('EEEB') == 120
    #
    # def test_buy_two_get_one_free(self):
    #     assert checkout_solution.checkout('FFF') == 20
    #     assert checkout_solution.checkout('FFFF') == 30
    #     assert checkout_solution.checkout('FFFFF') == 40
    #     assert checkout_solution.checkout('F') == 10
    #     assert checkout_solution.checkout('FFFFEEEB') == 150

    def test_new_items(self):
        assert checkout_solution.checkout('H'*16) == 135
        assert checkout_solution.checkout('H'*16 + 'V'*3 + 'U'*5 + 'R'*3 + 'Q'*3) == 635
        assert checkout_solution.checkout('G'*10) == 200
        assert checkout_solution.checkout('K'*5) == 380
        assert checkout_solution.checkout('N'*3+'M'*3) == 160
        assert checkout_solution.checkout('P'*11) == 450


import unittest

from cardrules import CardRules

from deck import Deck


class CardRulesFinalCheckTests(unittest.TestCase):

    def setUp(self):
        deck = Deck()
        self.card_rules = CardRules(deck)

    def test_reject_straight(self):
        self.card_rules.set_target('J')
        hand = ['7s','9c','10c','8s','Jd']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_flush(self):
        self.card_rules.set_target('9')
        hand = ['7c','9c','6c','5c','2c']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_pairs(self):
        self.card_rules.set_target('8')
        hand = ['7c','8c','7s','5c','2c']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_trips(self):
        self.card_rules.set_target('8')
        hand = ['7c','7d','7s','5c','2c']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_quads(self):
        self.card_rules.set_target('8')
        hand = ['5h','5d','5s','5c','2c']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_full_house(self):
        self.card_rules.set_target('8')
        hand = ['5h','5d','5s','2c','2h']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_reject_high_cards(self):
        # one high card
        self.card_rules.set_target('10')
        hand = ['7c','9c','Js','5c','2c']
        self.assertFalse(self.card_rules.check_success(hand))

        # two high cards
        self.card_rules.set_target('8')
        hand = ['7c','9c','Js','5h','Kc']
        self.assertFalse(self.card_rules.check_success(hand))

    def test_accept_valid_hand(self):
        # valid with highest card == target
        self.card_rules.set_target('10')
        hand = ['7c','9c','10s','5h','8c']
        self.assertTrue(self.card_rules.check_success(hand))

        # valid with highest card < target
        self.card_rules.set_target('10')
        hand = ['7c','9c','2s','5h','8c']
        self.assertTrue(self.card_rules.check_success(hand))


class CardRulesCardsRemovalTests(unittest.TestCase):

    def setUp(self):
        deck = Deck()
        self.card_rules = CardRules(deck)

    def test_remove_high_cards(self):
        self.card_rules.set_target('10')
        hand = ['7c','9c','Js','Kh','8c']
        retained_cards = self.card_rules.apply_rules(hand)
        expected_cards = ['7c','9c','8c']

        self.assertTrue(set(retained_cards)==set(expected_cards))


    def test_remove_pair_of_dominant_suit(self):
        # given a pair, the card from the dominant suit should be removed
        self.card_rules.set_target('J')
        hand = ['7c','9c','9s','6h','8c']
        retained_cards = self.card_rules.apply_rules(hand)
        expected_cards = ['7c','9s','6h','8c']

        self.assertTrue(set(retained_cards)==set(expected_cards))


    def test_remove_pair_of_dominant_suit2(self):
        # when there are no dominant suit (or equality of suits) the second pair card
        # gets removed
        self.card_rules.set_target('J')
        hand = ['7c','9c','9s','6s','8h']
        retained_cards = self.card_rules.apply_rules(hand)
        expected_cards = ['7c','9c','6s','8h']

        self.assertTrue(set(retained_cards)==set(expected_cards))

    def test_remove_second_high_card_given_a_straight(self):
        self.card_rules.set_target('J')
        hand = ['8c','7c','5s','6s','4h']
        retained_cards = self.card_rules.apply_rules(hand)
        expected_cards = ['8c','5s','6s','4h']

        self.assertTrue(set(retained_cards)==set(expected_cards))

    def test_remove_second_high_card_given_a_flush(self):
        self.card_rules.set_target('J')
        hand = ['10c','8c','5c','6c','4c']
        retained_cards = self.card_rules.apply_rules(hand)
        expected_cards = ['10c','5c','6c','4c']

        self.assertTrue(set(retained_cards)==set(expected_cards))

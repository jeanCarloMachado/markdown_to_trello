import unittest
from markdown_to_trello.markdown_to_trello import *

class ConverterTest(unittest.TestCase):
    def test_simplest(self):
        text = 'Do groceries'
        cards = MarkdownToTrello(text).convert_to_cards()

        self.assertTrue(len(cards), 1)

        self.assertEqual(cards[0].title, 'Do groceries')

    def test_list_remove_symbol(self):
        text = "- Do groceries"
        cards = MarkdownToTrello(text).convert_to_cards()
        self.assertEqual(cards[0].title, 'Do groceries')

    def test_multiple_lines_multiple_cards(self):
        pass

    def test_empty_line_no_card(self):
        text = """
        """
        cards = MarkdownToTrello(text).convert_to_cards()
        self.assertEqual(cards, [])



class SaveTest(unittest.TestCase):
    def test_save(self):
        result = SaveCards().dry_run([Card('buy milk')])

        self.assertEqual(result[0], 'trello add-card -b "Jeans Life" -l "Inbox" "buy milk" "" -q top')





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
        text = "- Do groceries\n- Do laundry"
        cards = MarkdownToTrello(text).convert_to_cards()
        self.assertEqual(cards[0].title, 'Do groceries')
        self.assertEqual(cards[1].title, 'Do laundry')


    def test_empty_line_no_card(self):
        text = """
        """
        cards = MarkdownToTrello(text).convert_to_cards()
        self.assertEqual(cards, [])

    def test_ignore_identation_of_siblings(self):
        text = """
                - Do groceries
                - Do laundry
        """

        cards = MarkdownToTrello(text).convert_to_cards()

        self.assertEqual(cards[0].title, 'Do groceries')
        self.assertEqual(cards[1].title, 'Do laundry')

class SaveTest(unittest.TestCase):
    def test_save(self):
        result = SaveCards('Myboard','Inbox').dry_run([
            Card('buy milk'),
            Card('clean clothes'),
        ])

        self.assertEqual(result[1], 'trello add-card -b "Myboard" -l "Inbox" "buy milk" "" -q top')
        self.assertEqual(result[0], 'trello add-card -b "Myboard" -l "Inbox" "clean clothes" "" -q top')





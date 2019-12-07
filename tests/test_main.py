import unittest
from markdown_to_trello.converter import *

class ConverterTest(unittest.TestCase):
    def test_simplest(self):

        text = 'Do groceries'

        cards = MarkdownToTrello(text).convert_to_cards()

        self.assertTrue(len(cards), 1)

        self.assertEqual(cards[0].title, 'Do groceries')



class SaveTest(unittest.TestCase):
    def test_save(self):
        result = SaveCards().dry_run([Card('buy milk')])

        self.assertEqual(result[0], 'trello add-card -b "Jeans Life" -l "Inbox" "buy milk" "" -q top')





import unittest
from markdown_to_trello.tree_parser import TreeParser



class TreeParserTest(unittest.TestCase):
    def test_list_with_description(self):
        text = """
- Do groceries
    - avocado
    - laranja
- Do laundry
        """

        result = TreeParser().parse(text)
        self.assertEqual([
            {
                "text": "- Do groceries",
                "nested": [
                    { "text": "    - avocado"},
                    { "text": "    - laranja"}
                ]
            },
            { "text":  "- Do laundry"}
        ], result)


import re
import unittest
from markdown_to_trello.markdown_to_trello import MarkdownToTrello, SaveCards, Card


class TreeParser:
    """
    This code is kind of ugly but it fits the simple purpose at hand here.
    If I need to extend the behaviour then I should consider something more sophisticated.
    And also start returning something more than a simple dict.
    """
    def parse(self, text):
        result = []
        lines = text.splitlines()
        previous_line_indentation  = None
        for i, line in enumerate(lines):
            if self._line_empty(line):
                continue

            current_line_indentation = self._indentation_level(line)
            if previous_line_indentation is not None and previous_line_indentation < current_line_indentation:
                continue

            entry = {}
            entry['text'] = line

            children = []
            for j, next_line in enumerate(lines[i+1:]):
                if self._line_empty(next_line):
                    continue
                next_line_indentation = self._indentation_level(next_line)

                if (next_line_indentation <= current_line_indentation):
                    break


                children_entry = {"text": next_line}
                children.append(children_entry)


            if children:
                entry['nested'] = children

            result.append(entry)
            previous_line_indentation = current_line_indentation


        return result
    def _indentation_level(self, string) -> int:
        return len(string) - len(string.lstrip())

    def _line_empty(self, line: str) -> bool:
        return not re.search(".*[A-Za-z0-9]+.*", line)


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


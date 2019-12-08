import re

class TreeParser:
    """
    This code is kind of ugly but it fits the simple purpose at hand here.
    If I need to extend the behaviour then I should consider something more sophisticated.
    Supports only 2 levels of indentation (which is what I need right now).
    If I end up needing more I should refactor to something recursive.
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

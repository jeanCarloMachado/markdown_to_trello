import os
from typing import List
import re

class MarkdownToTrello:
    def __init__(self, text):
        self.text = text

    def convert_to_cards(self) -> List['Card']:
        cards : List['Card'] = []
        for line in self.text.splitlines():
            if self._line_empty(line):
                continue
            cards.append(Card(line))

        return cards

    def _line_empty(self, line: str) -> bool:
        return not re.search(".*[A-Za-z0-9]+.*", line)



Command = str

class SaveCards:
    def dry_run(self, cards: List['Card']) -> List[Command]:
        board = "Jeans Life"
        lane = "Inbox"
        description = ''
        position = 'top'
        title = cards[0].title
        cmd = f'trello add-card -b "{board}" -l "{lane}" "{title}" "{description}" -q {position}'

        return [cmd]


    def perform(self, cards: List['Card']):
        commands = self.dry_run(cards)
        for command in commands:
            os.system(command)







class Card:
    def __init__(self, title):
        title = re.sub("^- ", '', title)
        self.title = title

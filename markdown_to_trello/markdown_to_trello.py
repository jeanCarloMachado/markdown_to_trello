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


class Card:
    def __init__(self, title):
        # remove empty spaces in front and the minus of a list
        title = re.sub("^\s*- ", '', title)
        self.title = title

Command = str

class SaveCards:
    def __init__(self, board, lane):
        self.board = board
        self.lane = lane

    def dry_run(self, cards: List['Card']) -> List[Command]:
        description = ''
        position = 'top'

        commands = []
        cards = reversed(cards)
        for card in cards:
            title = card.title
            commands.append(f'trello add-card -b "{self.board}" -l "{self.lane}" "{title}" "{description}" -q {position}')

        return commands


    def perform(self, cards: List['Card']):
        commands = self.dry_run(cards)
        for command in commands:
            os.system(command)


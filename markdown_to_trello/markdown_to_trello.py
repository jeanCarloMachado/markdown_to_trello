import os
from typing import List, Optional
from markdown_to_trello.tree_parser import TreeParser
from functools import reduce
import re

class MarkdownToTrello:
    def __init__(self, text):
        self.text = text

    def convert_to_cards(self) -> List['Card']:
        cards: List['Card'] = []
        parsed_tree = TreeParser().parse(self.text)

        for node in parsed_tree:
            description = ''
            if node.get('nested'):
                lines = list(map(lambda x: x['text'], node['nested']))
                description = '\n'.join(lines)


            cards.append(Card(node['text'], description))

        return cards


    def _line_empty(self, line: str) -> bool:
        return not re.search(".*[A-Za-z0-9]+.*", line)


class Card:
    def __init__(self, title, description = ""):
        # remove empty spaces in front and the minus of a list
        title = re.sub("^\s*- ", '', title)
        self.title = title
        self.description = description

Command = str

class SaveCards:
    def __init__(self, board, lane):
        self.board = board
        self.lane = lane

    def dry_run(self, cards: List['Card']) -> List[Command]:
        position = 'top'

        commands = []
        cards = reversed(cards)
        for card in cards:
            title = card.title
            description = card.description
            commands.append(f'trello add-card -b "{self.board}" -l "{self.lane}" "{title}" "{description}" -q {position}')

        return commands


    def perform(self, cards: List['Card']):
        commands = self.dry_run(cards)
        for command in commands:
            os.system(command)


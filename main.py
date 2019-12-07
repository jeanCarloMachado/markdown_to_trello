import sys
from markdown_to_trello.converter import MarkdownToTrello, SaveCards





content = sys.stdin.read()


cards = MarkdownToTrello(content).convert_to_cards()

SaveCards().perform(cards)




class Tree:
    def __init__(self):
        self.text = ""
        self.children = []

def get_tree_from_text(text):
    root_tree = {}
    stack = []
    prev_indent, prev_tree = -1, root_tree

    for line in text.splitlines():

        # compute current line's indent and strip the line
        origlen = len(line)
        line = line.lstrip()
        indent = origlen - len(line)

        # no matter what, every line has its own tree, so let's create it.
        tree = {}

        # where to attach this new tree is dependent on indent, prev_indent
        # assume: stack[-1] was the right attach point for the previous line
        # then: let's adjust the stack to make that true for the current line

        if indent < prev_indent:
            while stack[-1][0] >= indent:
                stack.pop()
        elif indent > prev_indent:
            stack.append((prev_indent, prev_tree))

        # at this point: stack[-1] is the right attach point for the current line
        parent_indent, parent_tree = stack[-1]
        assert parent_indent < indent

        # attach the current tree
        parent_tree[line] = tree

        # update state
        prev_indent, prev_tree = indent, tree

    return root_tree

text = '''
Do groceries
    - buy avocados
    - buy deo

Clean sofa
'''

print(get_tree_from_text(text))

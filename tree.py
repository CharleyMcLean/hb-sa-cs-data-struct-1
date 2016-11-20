# Discussion questions

# 1. Given the tree above, in what order would a Breadth First Search (BFS)
#    algorithm visit each node until finding burrito (starting at food)? Just
#    list the order of nodes visited; no need to recreate the state of the
#    algorithm data in your answer.
#    [food]
#    [Italian, Indian, Mexican]
#    [Indian, Mexican, lasagna, pizza]
#    [Mexican, lasagna, pizza, tikka masala, saag]
#    [lasagna, pizza, tikka masala, saag, burrito, tacos, enchiladas]
#    [pizza, tikka masala, saag, burrito, tacos, enchiladas]
#    [tikka masala, saag, burrito, tacos, enchiladas, thin crust, Chicago-style, New York-style, Sicilian]
#    [saag, burrito, tacos, enchiladas, thin crust, Chicago-style, New York-Style, Sicilian]
#    [burrito, tacos, enchiladas, thin crust, Chicago-style, New York-Style, Sicilian]
#    pop burrito!


# 2. Given the tree above, in what order would a Depth First Search (DFS)
#    algorithm visit each node until finding Chicago-style (starting at food)?
#    Just list the order of nodes visited; no need to recreate the state of the
#    algorithm data in your answer.
#    [food]
#    [Italian, Indian, Mexican]
#    [Italian, Indian, burrito, tacos, enchiladas]
#    [Italian, Indian, burrito, tacos]
#    [Italian, Indian, burrito]
#    [Italian, Indian]
#    [Italian, tikka masala, saag]
#    [Italian, tikka masala]
#    [Italian]
#    [lasagna, pizza]
#    [lasagna, thin crust, Chicago-style, New York-style, Sicilian]
#    [lasagna, thin crust, Chicago-style, New York-style]
#    [lasagna, thin crust, Chicago-style]
#    pop Chicago-style!


# 3. How is a binary search tree different from other trees?
#    In a binary search tree, each node has a left and right child, and has a
#    "rule" for arrangement.

############################################################################

"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        return len(self.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.
        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)


    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.breadth_first_search("B") is b2
            True

        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop(0)

            if node.data == data:
                return node

            to_visit.extend(node.children)
        
        pass

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


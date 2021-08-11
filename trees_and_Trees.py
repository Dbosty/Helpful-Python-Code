

# Python Tree Recursion and Tree Mutation

def lowest(t):
    '''
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5, [Tree(6, [Tree(7)])])])
    >>> lowest(t)
    7
    '''
    def lowest_pair(t):
        if t.is_leaf():
            return [t.label, 0]
        max_pair = max([lowest_pair(b) for b in t.branches], key= lambda x: x[1])
        max_pair[1] += 1
        return max_pair
    return lowest_pair(t)[0]


def longest_path_root(tree):
    ''' Given a tree, return the number of nodes along the longest
    path between an two nodes through the root.
    
    >>> longest_path_root(tree (1))
    1
    >>> t = tree(1, [tree(2, [tree(3)]), tree(4), tree(5, [tree(6, [tree(7)])])])
    >>> longest_path_root(t)
    4
    '''
    if is_leaf(tree):
        return len([tree])
    longest_paths = len(max([longest_path_root(branch) for branch in branches(tree)]))
    return longest_paths
    

def longest_path_root11(tree):
    ''' Given a tree, return the number of nodes along the longest
    path between an two nodes through the root.
    
    >>> longest_path_root(tree (1))
    1
    >>> t = tree(1, [tree(2, [tree(3)]), tree(4), tree(5, [tree(6, [tree(7)])])])
    >>> longest_path_root(t)
    4
    '''
    if is_leaf(tree):
        return 1
    longest_paths = len(tree)
    return longest_paths
    





























#########################                    
#     FOR REFERENCE     #                      
#########################


### LINK CLASS ###

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


### TREE CLASS ###

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


### TREE ADT DEFINITION ###

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

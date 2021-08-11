def enumerate(n):
    '''Define the function enumerate which takes in a postive integer
    N and prints the numbers from 1 to N in order.
    
    >>> enumerate(5)
    1
    2
    3
    4
    5
    '''
    if n > 1:
        enumerate(n - 1)
    print(n)


def countdown(n):
    '''Define the function countdown which takes a positive integer N
    and prints the numbers from N to 1.
    
    >>> countdown(5)
    5
    4
    3
    2
    1
    '''
    if n == 1:
        print(1)
        return
    elif n > 1:
        print(n)
    countdown(n - 1)
     
    # while n > 0:
    #     print(n)
    #     n -= 1

def other_reverse(link):
    '''
    >>> a = Link(5, Link(4, Link(3, Link(2, Link(1)))))
    >>> b = other_reverse(a)
    >>> b
    Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> a
    Link(5)
    '''
    if link == Link.empty or link.rest == Link.empty:
        return link
    reversed = other_reverse(link.rest)
    link.rest.rest = link
    link.rest = Link.empty
    return reversed 

def reverse(link):
    '''
    Define the function Reverse which takes in a linked list 
    object and returns a new linked list with the same elements 
    as the input linked list but in reverse order.
    
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = reverse(a)
    >>> repr(b)
    'Link(4, Link(3, Link(2, Link(1))))'
    >>> str(a)
    '<1 2 3 4>'
    '''
    if link == Link.empty: 
        return Link.empty
    if link.rest == Link.empty:
        return Link(link.first, Link.empty) 
    reversed = reverse(link.rest) # < 4 3 2 > 
    magic_pointer = reversed 
    while magic_pointer.rest != Link.empty:
        magic_pointer = magic_pointer.rest
    magic_pointer.rest = Link(link.first, Link.empty) # <1> 
    return reversed 
    # < 4 3 2 1 > 

def reverse_so_far(link, so_far):
    '''
    Define the function Reverse which takes in a linked list 
    object and returns a new linked list with the same elements 
    as the input linked list but in reverse order.

        so_far --- keeps track of result, need to return something
                   in terms of so_far once we hit the base case
        
    '''
    def helper(link, so_far):
        if link == Link.empty:
            return so_far
        else:
            link_so_far = helper(link.rest)
            pointer = link_so_far
            while pointer.rest is not Link.empty:
                pointer = pointer.rest
            pointer.rest = Link(link.first, Link.empty)
    return reverse_so_far(link, Link.first)



def doubled(link):
    '''
    Double every element within the linked list Link. 

    >>> a = Link(2, Link(8, Link(4, Link(3, Link(2)))))
    >>> b = doubled(a)
    Link(4, Link(16, Link(8, Link(6, Link(4)))))
    >>> str(b)
    '<4 16 8 6 4>'
    >>> repr(b)
    'Link(4, Link(16, Link(8, Link(6, Link(4)))))'
    '''
    if link == Link.empty:
        return Link.empty
    return Link(link.first * 2, doubled(link.rest))


def traversed_list(link, sum_so_far, link_so_far):
    '''
    Create a new linked list for the sum of the node values 
    of that we have traversed so far in Link. 

        sum_so_far ---  keeps track of sum value through each node, need to return something
                        in terms of sum_so_far once we hit the base case
        
        link_so_far --  keeps track of traversed lists
        
        Hint: goes down
    '''




########################                    
#  FOR LINK REFERENCE  #                      
########################

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

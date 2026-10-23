"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # To reduce solution to 1 pass use defaultdict to handle "node
        # doesn't exist yet issue"

        oldToCopy = collections.defaultdict(lambda : Node(0))
        oldToCopy[None] = None

        # A normal dict raises KeyError when you look up a missing key. 
        # A defaultdict instead calls the function you gave it, here lambda:
        # Node(0), stores the result under that key, and returns it.

        # So oldToCopy[X] means: “give me X’s copy, and if it doesn’t exist
        # yet, create a blank placeholder node, remember it, and give me 
        # that.” Every later lookup of X returns that same placeholder
        # object, which is what makes the trick work.

        curr = head
        while curr:
            oldToCopy[curr].val = curr.val
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]

            curr = curr.next

        return oldToCopy[head]
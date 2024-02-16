class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: LinkNode):
        self.head = head

# def main():
head = LinkNode()
head.val = 4
node1 = LinkNode(2)
head.next = node1

l = LinkedList(head)

print(head.val)
print(l)
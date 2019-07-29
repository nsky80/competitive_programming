class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print("data: ", current.data, end='\n')
            print("ref : ", current.next, end='\n')
            current = current.next

    def insert(self, head, data):
        if (head == None):
            head = Node(data)
        else:
            current = head
            temp = current
            while current:
                temp = current
                current = current.next
            temp.next = Node(data)
        return head


if __name__ == "__main__":
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)
    print(type(head))

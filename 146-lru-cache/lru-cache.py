class ListNode:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.node_map={}
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)

        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.remove_(node)
        self.add_(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node=self.node_map[key]
            self.remove_(old_node)
        node=ListNode(key, value)
        self.node_map[key]=node
        self.add_(node)

        if(len(self.node_map)>self.capacity):
            node_to_delete=self.head.next
            self.remove_(node_to_delete)

            del self.node_map[node_to_delete.key]

    def add_(self,node):
        prev_end=self.tail.prev
        prev_end.next=node
        node.prev=prev_end
        node.next=self.tail
        self.tail.prev=node


    def remove_(self,node):
       node.prev.next=node.next #1,2,3,4,5
       node.next.prev=node.prev 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
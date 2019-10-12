

class ApiCompositionGraph:
    def __init__(self, head):
        self.head = head  # head of the graph

class ApiCompositionGraphNode:
    def __init__(self):
        self.next = []
        self.previous = []
        self.goal
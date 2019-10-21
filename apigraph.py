

class MashupGraph:
    def __init__(self, head):
        self.__head = head  # head of the graph
        self.__current = None



class MashupGraphNode:
    def __init__(self, goal=None):
        self.__next = []
        self.__previous = []
        self.__goal = goal




        # TODO how to define used paths
        #   when we call SPARQL query on Goal,
        #       Result = all candidate API where their postcond validate the new goal new goal
        #       - Add all of them to them to the list of [next]
        #       - Select the first one and make indice of last used one i=0, i++ until i=len(next)-1 else return back



if __name__ == "__main__":
    nde = MashupGraphNode()
    nde.__next = 'abc'
    print(nde.__next)
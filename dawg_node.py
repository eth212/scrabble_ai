class DawgNode:
    NextId = 0
    def __init__(self):
        self.id = DawgNode.NextId
        DawgNode.NextId += 1
        self.final = False
        self.edges = {}

    def __str__(self):        
        arr = []
        if self.final: 
            arr.append("1")
        else:
            arr.append("0")

        for (label, node) in self.edges.items():
            arr.append( label )
            arr.append( str( node.id ) )

        return "_".join(arr)

    def __hash__(self):
        return self.__str__().__hash__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()
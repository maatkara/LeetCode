class DisjointSets:
    def __init__(self, n):
        self.parents = list(range(n + 1))  # size= n+1: for i = 1 parents[i] = parents[1]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        self.parents[i_id] = j_id

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  # Rewrite the root of the vertex i which is on the way
        return self.parents[i]

    def __str__(self):
        return f'parents: {self.parents}\n'

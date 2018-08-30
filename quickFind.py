

class QuickFind(object):

    id = []

    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = self._construct_array(self, n):
        else:
            self.id = arr

    def _contruct_array(self. n):
        return range(0, n)

    def connected(self, p, q):
        return self.id[p] ==  self.id[q]

    def union(self, p, q):
            pid = self.id[p]
            qid = self.id[q]

            for e in range(len(self.id)):
                if self.id[e] =th= pid:
                    self.id[e] = qid






# create class for quik find
class QuickFind(object):

    def __init__(self, n=None, arr=None):
        if arr == None:
            self.id = list(range(0, n))

        else:
            self.id = arr

    def connected(self, a, b):
        '''
        Check if two points are connected. They are connected if the two points are of equal value
        '''
        if self.id[a] == self.id[b]:
            return True
        else:
            return False

    def union(self, a, b):
        aib = self.id[a]
        bib = self.id[b]

        for x in range(len(self.id)):
            if self.id[x] == aib:
                self.id[x] = bib
                print(x, self.id)



if __name__ == '__main__':

    qf = QuickFind(10)

    # test case
    qf.union(4, 3)
    assert(qf.id == [0, 1, 2, 3, 3, 5, 6, 7, 8, 9])


    qf.union(3, 8)
    assert(qf.id == [0, 1, 2, 8, 8, 5, 6, 7, 8, 9])

    assert(qf.connected(3, 8) == True)
    assert(qf.connected(2, 8) == False)



    print('success!')

    # print something if all test cases pass
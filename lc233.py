class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self, n):
        self.n = n
        
    def countDigitOne(self, n):
        self.n = raw_input('Given a number:\n')
        try:
            while True:
                self.n = int(self.n) & self.n > 0
                continue
        except:
            print 'Not a positive integer.'
        
        numbs = None
        counts = 0
        for numb in range(self.n):
            numbs = numbs + str(numb)
            for i in [1:len(numbs)]:
                if numbs[i-1] == '1':
                    count =+ 1
                else:
                    continue
        return counts
        print 'number of digit 1 is:', counts

from mrjob.job import MRJob
from mrjob.step import MRStep

class stdev(MRJob):

    def mapper_init(self):
        self.counter = 0

    def mapper(self, _, line):

        words = line.split()

        words = [w.strip().lower() for w in words]
        words[-1] = float(words[-1])

        out=(" ".join(words[:-1]),str(words[-1]))
        yield(out)


    def reducer(self, name, values):
        N = S = S2 = 0
        for v in values:
          N += 1  
          v = float(v)
          S += v
          S2 += v*v
        S2 = float(S2) / N
        S = float(S) / N
        S = S * S 
        result = (S2-S)**0.5
        yield (name,result) 

    def steps(self):
        #return [ MRStep(mapper_init=self.mapper_init,
        #                mapper=self.mapper,
        #                reducer=self.reducer) ]
        return  [ MRStep( mapper=self.mapper, reducer=self.reducer) ]

if __name__ == '__main__':
    stdev.run()

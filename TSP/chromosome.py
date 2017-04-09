import random 
class chromosome():
    genes=[]
    cost=0
    fitness=0.0
    def generate_cost(self,Matrix_inf):
        self.cost=0
        x=self.genes[0]
        for i in (self.genes):
            self.cost=self.cost+Matrix_inf[i][x]
            x=i
        self.generate_fitness()
    def generate_fitness(self):
        self.fitness=1.0/self.cost
    def create_new(self,Matrix_inf,nGenes):
        g=[]
        for i in range(nGenes):
            g.append(i)
        random.shuffle(g)
        self.genes=g
        self.generate_cost(Matrix_inf)

    def gene(self,i):
        return(self.genes[i])

    def contains_gene(self,gene,nGenes):
        found=False
        for i in range(nGenes):
            if(self.genes[i]==gene):
                found=True
        return(found)
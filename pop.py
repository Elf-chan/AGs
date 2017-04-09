import random 
from chromosome import chromosome
class population():
    chromosomes=[]
    def create_new(self,Matrix_inf,size_pop,nGenes,initializing):        
        for i in range(size_pop):     
            new=chromosome()   
            if(initializing):
                new.create_new(Matrix_inf,nGenes)      
            self.chromosomes.append(new)
    def Return_chromo(self,i):
        return(self.chromosomes[i])
    def Fittest(self,nGenes):

        fit=self.chromosomes[0]
        for i in range(nGenes):
            if(fit.fitness<self.chromosomes[i].fitness):
                    fit=self.chromosomes[i]
        return(fit)
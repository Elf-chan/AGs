import random 
from chromosome import chromosome
from pop import population

class GA():

    def Evolution(self,size_pop,Matrix_inf,nGenes,MRate,nGenarations):
        #creates the initial population
        pop=population()
        pop.create_new(Matrix_inf,size_pop,nGenes,True)

        ##evolves the initial population in n generations
        for i in range(nGenarations):
            pop=self.create_new_generation(pop,size_pop,Matrix_inf,nGenes,MRate)
            fittest=pop.Fittest(nGenes)
            print("Path: ",fittest.genes,"Distance:",fittest.cost)
        fittest=pop.Fittest(nGenes)
        ##print solution
        print("\nSolution:")
        print("Path: ",fittest.genes,"Distance:",fittest.cost)

    def create_new_generation(self,pop,size_pop,Matrix_inf,nGenes,MRate):
        newpop=population()
        newpop.chromosomes=[]
        
        #Elitismo
        newpop.chromosomes.append(pop.Fittest(nGenes))

        for i in range(1,size_pop,1):
            parent1=self.selection(pop,nGenes)
            parent2=self.selection(pop,nGenes)

            newpop.chromosomes.append(self.crossover(parent1,parent2,nGenes,Matrix_inf))
            
        for i in range(1,nGenes,1):
            newpop.chromosomes[i]=self.mutation(newpop.chromosomes[i],nGenes,MRate,Matrix_inf)

        return(newpop)
    def crossover(self,parent1,parent2,nGenes,Matrix_inf):
        position1=random.randint(0,nGenes-1)
        position2=random.randint(0,nGenes-1)

        child=chromosome()
        child.genes=[]


        if(position1>position2):
            maior=position1
            position1=position2
            position2=maior

        for i in range(nGenes):
            if(position1<=i<=position2):
                child.genes.append(parent1.genes[i])
            else:
                child.genes.append(None)

        for i in range(nGenes):
            if((child.contains_gene(parent2.gene(i),nGenes)) is not True):
                for i in range(nGenes):
                    if(child.genes[i] is None):
                        child.genes[i]=parent2.genes[i]

        child.generate_cost(Matrix_inf)
        return(child)
    def mutation(self,chromosome,nGenes,MRate,Matrix_inf):
        if(random.randint(0,100) <= MRate):
                position1=random.randint(0,nGenes-1)
                position2=random.randint(0,nGenes-1)

                getGene=chromosome.genes[position1]
                chromosome.genes[position1]=chromosome.genes[position2]
                chromosome.genes[position2]=getGene
                chromosome.generate_cost(Matrix_inf)
        return(chromosome)
    def selection(self,pop,nGenes):
        fitpop=population()
        quantity=random.randint(0,nGenes)
        for i in range(quantity):
            add=random.randint(0,nGenes-1)
            fitpop.chromosomes.append(pop.chromosomes[add])
        fit=fitpop.Fittest(nGenes)
        return(fit)


#				ARTIFICIAL INTELLIGENCE
#	Using genetic algorithm to solve the traveling salesman problem(TSP)
#   	By: Mayara Simoes de Oliveira Castro

from GA import GA

Matrix_inf=[[0,1,7,5,6],
			[1,0,2,7,8],
			[7,2,0,5,3],
			[5,7,5,0,4],
			[6,8,3,4,0]]##the distance between cities
size_pop=5 #size of population
nGenes=5#number of genes in a chromosome/number of cities
MRate=50 #mutation rate
nGenarations=100 #quantity of generations

TSP=GA()
TSP.Evolution(size_pop,Matrix_inf,nGenes,MRate,nGenarations)

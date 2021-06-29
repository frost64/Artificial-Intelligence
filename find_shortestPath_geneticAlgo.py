import random
from copy import deepcopy

given_cities=[
    [0,    66,    21,  300,  500,   26,   77,   69,  125,  650 ],
    [66,    0,    35,  115,   36,   65,   85,   90,   44,  54  ],
    [21,   35,     0,  450,  448,  846,  910,   47,   11,  145 ],
    [300, 115,   450,    0,   65,  478,  432,  214,  356,  251 ],
    [500,  36,   448,   65,    0,  258,  143,  325,  125,  39  ],
    [ 26,  65,   846,  478,  258,    0,  369,  256,  345, 110  ],
    [ 77,  85,   910,  432,  143,  369,    0,   45,  120, 289  ],
    [ 69,  90,    47,  214,  325,  256,   45,    0,  325, 981  ],
    [125,  44,    11,  356,  125,  345,  120,  325,    0, 326  ],
    [650,  54,   145,  251,   39,  110,  289,  981,  326,   0  ],
]

total_cities = len(given_cities)
city = [0,1,2,3,4,5,6,7,8,9]
total_population=40
population , child = [0]*total_population ,[]
shortest_path=[99999*99999,0]

def make_population():
    for i in range(total_population):
        population[i]= random.sample( deepcopy(city), len(given_cities) ) 

def find_distance(cities_path):
    sum=0
    for i in range(total_cities):
        if i != total_cities-1:
            sum+=  given_cities[ cities_path[i] ][ cities_path[i+1] ] 
        else:
            sum+=  given_cities[ cities_path[i] ][ cities_path[0] ] 
    return sum

def find_total_fitness():
    global total_fitness,shortest_path
    count=0
    for i in population:
        tmp= find_distance(i)
        if tmp<shortest_path[0]:
            shortest_path[0]=tmp
            shortest_path[1]=[x+1 for x in i]
        
        fitness_values[count]=450/float(tmp)
        total_fitness+=tmp
        count+=1
    total_fitness=450/float(total_fitness)

def mutation():          
    for lst in child:
        for i in range(2):    
            rand1=random.randrange(0,total_cities)
            rand2=random.randrange(0,total_cities)
            while rand1==rand2:
                rand2=random.randrange(0,total_cities)
            lst[rand1],lst[rand2]=lst[rand2],lst[rand1]

def crossover(lst1,lst2):
    random_number =random.randrange(0,total_cities-1)
    temp =  lst1[0:random_number]

    for i in lst2[random_number:]:
        if i not in temp:
            temp.append(i)
    
    if len(temp)<total_cities:
        for i in lst2:
            if i not in temp:
                temp.append(i)

    temp2 =  lst2[0:random_number]

    for i in lst1[random_number:]:
        if i not in temp2:
            temp2.append(i)
    
    if len(temp2)<total_cities:
        for i in lst1:
            if i not in temp2:
                temp2.append(i)  

    child.append(temp)
    child.append(temp2)

def select_parents():
    for i in range(int(total_population/2)):
        p1=random.choices(population,fitness_values)
        p2=random.choices(population,fitness_values)
        crossover(p1[0],p2[0])

def p():
    make_population()
    find_total_fitness()

    select_parents()
    mutation()

for k in range(999999999):
    fitness_values = [0]*total_population
    total_fitness=0
    p()
    population=child
    child=[]
    print("Shotest distance : ",shortest_path[0],"    path : ",shortest_path[1],"   generation : {0}".format(k))



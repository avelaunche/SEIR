import random

beta = 3
dt = 0.1
gamma = 3
sigma = 3
population = 1000
time = 100

population_list = []
exposed_list = []
infected_list = []
recovered_list = []

for x in range(1000):
  population_list.append(1)
  exposed_list.append(0)
  infected_list.append(0)
  recovered_list.append(0)

for x in range(time):
  for y in range(len(population_list)):
    if random.random() < beta*dt:
      population_list[x] = 0
      exposed_list[x] = 1
  for y in range(len(exposed_list)):
    if random.random() < gamma*dt and exposed_list[y] == 1:
      exposed_list[x] = 0
      infected_list[x] = 1
  for y in range(len(infected_list)):
    if random.random() < sigma*dt and infected_list[y] == 1:
        infected_list[x] = 0
        recovered_list[x] = 1
  beta = 1


# slices

# Exerciții:

# Dată fiind lista
cities = ['București', 'Galați', 'Cluj-Napoca', 'Timișoara', 'Constanța', 'Berlin']
# Iterați prin ea de la coadă la cap

for elem in cities[::-1]:
    print(elem)

# obțineți lista cu primele 2 elemente din cities
cities[:2]

# lista cu ultimele 3 elemente
cities[-3:]

# lista cu ultimele 3 elemente, de la coadă la cap (ordine inversată)
cities[-1:-4:-1]

# lista de la elementul al 2lea la al 4lea (grijă la off-by-one error)
cities[1:4] # 4-1 = 3

# hint: (unde finalizez) - (de unde încep) = nr.-ul de elemente


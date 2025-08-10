
population_wealth = [int(x) for x in input().split(", ")]
minimal_wealth = int(input())

total_wealth = sum(population_wealth)

if total_wealth < minimal_wealth * len(population_wealth):
    print("No equal distribution possible")
    exit()

while min(population_wealth) < minimal_wealth:
    richest_person = max(population_wealth)
    idx_richest = population_wealth.index(richest_person)

    poorest_person = min(population_wealth)
    idx_poorest = population_wealth.index(poorest_person)

    needed_wealth = minimal_wealth - poorest_person
    population_wealth[idx_poorest] += needed_wealth
    population_wealth[idx_richest] -= needed_wealth

print(population_wealth)

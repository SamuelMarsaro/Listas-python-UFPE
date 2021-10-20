iron_stacks = int(input())
NUM_VILLAGES = 3
stacks_per_village = iron_stacks // NUM_VILLAGES
tresh_stacks = iron_stacks - stacks_per_village * NUM_VILLAGES
print(stacks_per_village)
print(tresh_stacks)

import numpy as np

# Simulation Size
num_rolls = 1000000

# Probability for each number on die
probability = np.full((6), 1/6)

# Simulating die roll
roll = np.random.choice(np.arange(1, 7), size=num_rolls, p = probability)

prob_1 = np.mean(roll == 1)
prob_2 = np.mean(roll == 2)
prob_3 = np.mean(roll == 3)
prob_4 = np.mean(roll == 4)
prob_5 = np.mean(roll == 5)
prob_6 = np.mean(roll == 6)

prob_prime = np.mean(roll == 2) + np.mean(roll == 3) + np.mean(roll == 5)
prob_bt = np.mean(roll == 3) + np.mean(roll == 4) + np.mean(roll == 5)
prob_odd = np.mean(roll == 1) + np.mean(roll == 3) + np.mean(roll == 5)

print("Probability of the number rolled being 1: ", prob_1)
print("Probability of the number rolled being 2: ", prob_2)
print("Probability of the number rolled being 3: ", prob_3)
print("Probability of the number rolled being 4: ", prob_4)
print("Probability of the number rolled being 5: ", prob_5)
print("Probability of the number rolled being 6: ", prob_6)


print("Probability of the number rolled being prime: ", prob_prime)
print("Probability of the number rolled being between 2 and 6: ", prob_bt)
print("Probability of the number rolled being odd: ", prob_odd)


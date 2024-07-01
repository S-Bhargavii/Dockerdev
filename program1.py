import random 
# import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg') 
random_numbers = [random.randint(1,100) for _ in range(10)]
print("random numbers have been generated....")
plt.plot(random_numbers, marker='o')

plt.title('Plot of 10 numbers')
plt.xlabel('Index')
plt.xlabel('Random NUmber')
print('showing graph')
# plt.show()
plt.savefig('/workspace/repo/plot.png') 
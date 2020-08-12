import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#basic x, y, z ploting
x = [1,2,3]
y = [1,4,9]
z = [1,8,27]
plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["y","z"])
plt.show()

#sample of import data(.csv) from same folder

sample_data = pd.read_csv('sample_data.csv')

plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c)
plt.title("b,c vs a")
plt.xlabel("a")
plt.ylabel("b & c")
plt.legend(["this is b", "this is c"])
plt.show()

#sample of analysis of populations

population = pd.read_csv('countries.csv')

# compare the population growth in the US and China

us = population[population.country == 'United States']
china = population[population.country == 'China']

#absolute population

plt.plot(us.year, china.population / 10**6)
plt.plot(us.year, us.population / 10**6)
plt.xlabel("year")
plt.ylabel("populaiton (in millions)")
plt.legend(["China", "U.S."])
plt.show()

#growth relative to first year

taiwan = population[population.country == 'Taiwan']

plt.plot(us.year, china.population / china.population.iloc[0] * 100, 'o')
plt.plot(us.year, us.population / us.population.iloc[0] * 100, 'd')
plt.plot(us.year, taiwan.population / taiwan.population.iloc[0] * 100, 's')

plt.xlabel("year")
plt.ylabel("populaiton growth(first year = 100)")
plt.legend(["China", "U.S.", "Taiwan"])
plt.show()

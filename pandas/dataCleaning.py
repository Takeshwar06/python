import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\PC-ASUS\\Desktop\\python\\test.csv')
df.plot(kind = 'scatter', x = 'name', y = 'branch')
plt.show()


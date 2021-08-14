import matplotlib.pyplot as plt
import numpy as np

Name=["China", "India", "US"]
GNI=[16.8, 6.9, 66.1]
LE=[76.7, 69.4, 78.5]
P=[1398, 1366, 328]
fig, ax=plt.subplots()
for i,type in enumerate(Name):
    x=GNI[i]
    y=LE[i]
    z=P[i]
    #col=[[1,5,10]]
    #plt.scatter(x, y, z, color="deepskyblue")
    print(i)
    colors = np.array(["black","red","blue"])
    plt.scatter(x, y, z, c=colors[i])
  
    plt.text(x, y, type, fontsize=15)
plt.show()

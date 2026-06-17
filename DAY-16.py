'''
MATPLOTLIB:
-----------
-->THIS IS A LIBRARY IN PYTHON FOR DATA VISUALIZATION, ALLOWING USERS TO CREATE
A VARIETY OF PLOTS,..

BAIC STRUCTURE OF MATPLOTLIB:
-----------------------------
-->FIGURE
-->AXES
-->AXIS
-->GRID
-->TITLE
-->LEGEND
------------------------------------
import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,30,45]
plt.bar(sales,values,color = 'red',edgecolor = 'black')
plt.xlabel('CAR models')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()
----------------------------------
import matplotlib.pyplot as plt
overs = [1,2,3,4]
score = [10,20,30,50]
plt.plot(overs,score)
plt.xlable('overs')
plt.ylable('scores')
plt.title('score card')
plt.show()

-------------------------------
import matplotlib.pyplot as plt
subjects = ['python','java','c']
students = [35,5,85]
plt.pie(students,labels=subjects,autopct='%1.1f%%')
plt.legend(subjects)
plt.title('students in course')
plt.show()

---------------------------
import matplotlib.pyplot as plt
x = [2,1,3,5,4,6]
y = [15,5,20,13,5,8]

plt.scatter(x,y)
plt.title('scatter plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()

-----------------------------------
import matplotlib.pyplot as plt

y = [15,5,20,13,5,8]

plt.hist(y)
plt.title('Histogram plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
'''
import matplotlib.pyplot as plt
sales = [2020,2021,2022,2023]
values = [23,35,65,850]
plt.bar(sales,values)
plt.title('toyata')
plt.xlabel('values')
plt.ylabel('sales')
plt.show()





























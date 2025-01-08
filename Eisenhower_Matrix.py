import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0,5,100)
x2 = np.linspace(5,10,100)
task_list = []
do_list=[]
delegate_list=[]
decide_list=[]
delete_list = []
n = int(input("Enter number of tasks:"))
for i in range(0,n):
    t_name = str(input(f"Enter the name of Task {i+1}:"))
    t_imp = int(input("Enter the importance of task on a scale of 1-10:"))
    t_urg = int(input("Enter the urgency of task on a scale of 1-10:"))
    task_list.append([t_name,t_imp,t_urg])
sorted(task_list,reverse=True,key = lambda x : x[1]+x[2])
for i in task_list:
    if i[1] >= 7 and i[2] >= 7:
        do_list.append(i)
    elif i[1]+i[2] <= 6:
        delete_list.append(i)
    elif i[1] >= i[2]:
        decide_list.append(i) 
    else:
        delegate_list.append(i)
print("Do List:",do_list)
print("Decide List:",decide_list)
print("Delegate List:",delegate_list)
print("Delete List:",delete_list)
name = list(map(lambda x:x[0],task_list))
imp = list(map(lambda x:x[1],task_list))
urg = list(map(lambda x:x[2],task_list))
plt.legend(['Do','Decide','Delegate','Delete'])
plt.scatter(imp,urg,zorder=2)


plt.fill_between(x2,10,5,color="green",zorder=1)
plt.fill_between(x2,5,color="yellow",zorder=1)
plt.fill_between(x1,10,5,color="lightblue",zorder=1)
plt.fill_between(x1,5,color="red",zorder=1)

plt.legend(['Task','Do','Decide','Delegate','Delete'])
plt.xlabel('Importance')
plt.ylabel('Urgency')

for i, label in enumerate(name):
    plt.text(imp[i], urg[i], label,zorder=2)

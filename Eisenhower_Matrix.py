x1 = np.linspace(0,5,100)
x2 = np.linspace(5,10,100)
task_list = [["Task1",10,1],["Task2",7,9],["Task3",6,5],["Task4",3,10],["Task5",8,3],["Task6",4,1],["Task7",3,3],["Task8",2,10],["Task9",5,5],["Task10",1,1]]
sorted(task_list,reverse=True,key = lambda x : x[1]+x[2])
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

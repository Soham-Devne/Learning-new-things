import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define fuzzy sets for importance and urgency
x = np.arange(0, 11, 1)  # Scale from 0 to 10
importance_low = fuzz.trimf(x, [0, 0, 5])
importance_medium = fuzz.trimf(x, [3, 5, 7])
importance_high = fuzz.trimf(x, [5, 10, 10])

urgency_low = fuzz.trimf(x, [0, 0, 5])
urgency_medium = fuzz.trimf(x, [3, 5, 7])
urgency_high = fuzz.trimf(x, [5, 10, 10])

# Input tasks
n = int(input("Enter number of tasks:"))
tasks =[] 
for i in range(n):
    t_name = input(f"Enter the name of Task {i+1}: ")
    t_imp = int(input("Enter the importance of task on a scale of 0-10: "))
    t_urg = int(input("Enter the urgency of task on a scale of 0-10: "))
    tasks.append((t_name, t_imp, t_urg))

# Classify tasks using fuzzy logic
do_list = []
decide_list = []
delegate_list = []
delete_list = []

for task in tasks:
    t_name, t_imp, t_urg = task
    
    # Fuzzify importance and urgency
    imp_low = fuzz.interp_membership(x, importance_low, t_imp)
    imp_medium = fuzz.interp_membership(x, importance_medium, t_imp)
    imp_high = fuzz.interp_membership(x, importance_high, t_imp)
    
    urg_low = fuzz.interp_membership(x, urgency_low, t_urg)
    urg_medium = fuzz.interp_membership(x, urgency_medium, t_urg)
    urg_high = fuzz.interp_membership(x, urgency_high, t_urg)
    
    # Apply rules for categorization
    do_degree = min(imp_high, urg_high)  # High importance and high urgency
    decide_degree = min(imp_high, urg_low)  # High importance, low urgency
    delegate_degree = min(imp_low, urg_high)  # Low importance, high urgency
    delete_degree = min(imp_low, urg_low)  # Low importance and low urgency
    
    # Assign task to the category with the highest degree
    category = max(do_degree, decide_degree, delegate_degree, delete_degree)
    if category == do_degree:
        do_list.append(task)
    elif category == decide_degree:
        decide_list.append(task)
    elif category == delegate_degree:
        delegate_list.append(task)
    else:
        delete_list.append(task)

# Print results
print("Do List:", do_list)
print("Decide List:", decide_list)
print("Delegate List:", delegate_list)
print("Delete List:", delete_list)

# Visualization
plt.figure(figsize=(8, 8))
plt.fill_between([5, 10], 10, 5, color="green",label="Do")
plt.fill_between([5, 10], 5, 0, color="yellow", label="Decide")
plt.fill_between([0, 5], 10, 5, color="lightblue",label="Delegate")
plt.fill_between([0, 5], 5, 0, color="red",  label="Delete")

for task in tasks:
    plt.scatter(task[1], task[2])
    plt.text(task[1] + 0.2, task[2] + 0.2, task[0])

plt.xlabel("Importance")
plt.ylabel("Urgency")
plt.legend()
plt.title("Fuzzy Eisenhower Matrix")
plt.show()

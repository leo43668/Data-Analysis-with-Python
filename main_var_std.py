import numpy as np

def calculate(lst):
    
    mylist = np.array(lst).reshape(3, 3)
    print("Your 3*3 array is:\n",mylist)
    # Calcultaitons
    calculations = {
        'mean': [mylist.mean(axis=0).tolist(), mylist.mean(axis=1).tolist(), mylist.mean().tolist()],
        'variance': [mylist.var(axis=0).tolist(), mylist.var(axis=1).tolist(), mylist.var().tolist()],
        'standard deviation': [mylist.std(axis=0).tolist(), mylist.std(axis=1).tolist(), mylist.std().tolist()],
        'max': [mylist.max(axis=0).tolist(), mylist.max(axis=1).tolist(), mylist.max().tolist()],
        'min': [mylist.min(axis=0).tolist(), mylist.min(axis=1).tolist(), mylist.min().tolist()],
        'sum': [mylist.sum(axis=0).tolist(), mylist.sum(axis=1).tolist(), mylist.sum().tolist()]
    }
    return print(calculations)

# Get the input list 
def get_input():
    print("Please enter 9 integers to form a list.")
    list = []
    for i in range(9):
        while True:
            try:
                num = int(input(f"Enter integer {i+1}: "))
                list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return list



user_list = get_input()
print("Your list:", user_list)
calculate(user_list)


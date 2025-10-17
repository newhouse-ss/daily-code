import pandas as pd

data = {"Name":["sb", "pt", "eg"], "Age":[22, 33, 44], "Job":["cook", "N/A", "cashier"]}
df = pd.DataFrame(data, index = ['Employee1', 'Employee2', 'Employee3'])
new_row = pd.DataFrame({"Name":"Eugene", "Age":55, "Job":'Manager'}, index = ['Employee4'])
df = pd.concat([df, new_row])
df["Salary"] = [1000, 0, 500, 10000]
print(df)
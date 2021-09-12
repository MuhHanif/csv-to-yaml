import pandas as pd

#input csv file
csv = input("csv dir: ")
#output yaml file
yml = input("yaml output name: ")


csv = "test.csv" # debug hardcode
csv = pd.read_csv(csv)

cols = csv.columns.to_list()
#cols.sort(reverse=True)
print(csv)

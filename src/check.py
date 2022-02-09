import csv
# file = open('../experimental_prop.csv')
# csvreader = csv.reader(file)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)

with open('../experimental_prop.csv') as f:
  reader = csv.reader(f)
  data_exp = [row[0] for row in reader]
print(data_exp)
# print("\n")

with open('../id_prop.csv') as f:
  reader = csv.reader(f)
  data = [row[0] for row in reader]
print(data)

count=0
for i in data_exp:
  if i in data:
    print(i)
    count=count+1
print(count)

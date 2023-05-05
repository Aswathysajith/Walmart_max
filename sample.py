
import csv

# read the data with csv into list 'pop'
pop = []
with open ('Walmart.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')

    for row in csv_reader:
        pop.append(row)

# print the first 5 rows of the table (5 first elements of the list)
# for row in range(0,5):
#     print(pop[row])
print(pop[0])

d={}
for row in pop[1:]:
    order_id=row[0]
    profit=float(row[-1])
    if order_id in d.keys():
        d[order_id]=max(profit,d[order_id])
    else:
        d[order_id]=profit
print(d)



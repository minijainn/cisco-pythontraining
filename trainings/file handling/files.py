"""f.open("")







#with clause
with open("emp.txt","w") as f:

import csv

with open("books.csv","rt") as f:
    data=csv.reader(f)
    for row in data:
        print(row)

"""






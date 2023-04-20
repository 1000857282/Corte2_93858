
organizacion_datos="organization_data.csv"

with open('organization_data.csv', newline='') as f:
    reader = csv (f)  
for row in reader: 
    print("Index:{0}, Organizacion: {1}, Name:{2}, Website: {3}, Country:{4}, Description:{5}, Founded:{6},\
        Industry: {7}, Number of employees: {8}".format(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8] ))
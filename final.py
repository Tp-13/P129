import csv

data_1 = []
data_2 = []
with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_2.append(row)
        
headers1 = data_1[0]
planet_data1 = data_1[1:]
headers2 = data_2[0]
planet_data2 = data_2[1:]
headers = headers1 + headers2
planet_data = []
for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("final_1.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
import csv
with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

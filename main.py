import pandas


data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
# print(data_dict)
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp))
#
# print(data['temp'].mean())
# # or data.temp
#
# print(data['temp'].max())

# Get Data in Row
# print(data[data.day == "Monday"])

# Get the Max Temp Row
# print(data[data.temp == data.temp.max()])


# Convert celsius(°C) to fahrenheit(F)
# monday = data[data.day == 'Monday']
# print(monday.condition)
# converted_temp = (monday.temp * 9/5) + 32
# print(converted_temp)


# Create a DataFrame from scratch
data_dict = {
    'students': ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

# converting to csv
new_data.to_csv("new_file.csv")
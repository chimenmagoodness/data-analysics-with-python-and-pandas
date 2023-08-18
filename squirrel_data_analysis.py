import pandas


# My Solution
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data['Primary Fur Color'])

# colors = data['Primary Fur Color']
# colors_count = pandas.value_counts(colors)
# print(colors_count)
#
# data_dict = {
#     "Fur Color": ['Gray', 'Cinnamon', 'Black'],
#     "count": [2473, 392, 103]
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("squirrel_count.csv")


# Angela Yu's Solution

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

new_file = pandas.DataFrame(data_dict)
new_file.to_csv("squirrel_count_solution.csv")

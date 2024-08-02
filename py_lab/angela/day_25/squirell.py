import pandas

data=pandas.read_csv("squirrel_data.csv")

squirrel_dict={}

gray=data[data["Primary Fur Color"]=="Gray"]["Primary Fur Color"].to_list()
cinnamon=data[data["Primary Fur Color"]=="Cinnamon"]["Primary Fur Color"].to_list()
black=data[data["Primary Fur Color"]=="Black"]["Primary Fur Color"].to_list()

print(len(black))


squirrel_dict["color"]=["cinnamon","gray","black"]
squirrel_dict["Number"]=[len(cinnamon),len(gray),len(black)]

print(squirrel_dict)

data_dict=pandas.DataFrame(squirrel_dict)
data_dict.to_csv("squirrel_colors.csv")



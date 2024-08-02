#with open("weather_data.csv") as file:
#    data=file.readlines()

#print(data)

# import csv
# from prettytable import PrettyTable
# 
# 
# x=PrettyTable()
# 
# x.field_names=['day','temp','condation']
# 
# 
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data :
#        x.add_row(row)
#     #temp=list(map(lambda x:int(x), temp))
# 
#     print(temp)
# 
 
import csv
import prettytable

table =prettytable.PrettyTable()
table.field_names=["day","temp","somthingelse"]

#with open("weather_data.csv") as file:
#    data=csv.reader(file)
#    #temp= list(map(lambda x:  int(x),
#       # [tem[1] for tem in data ][1:]))
#   # print(temp)
#    for row in data:
#        table.add_row(row)
#        print(row)
#    print(table)
#
import pandas

data=pandas.read_csv("weather_data.csv")

#dict_test=data.to_dict()
#print(dict_test)
#print(data)
#print(data["temp"])

#list_data=data["temp"].to_list()
##print(list_data)
#avr=sum(list_data)/len(list_data)
#print(avr)
#avrege=data["temp"].mean()
#print(avrege)
#
#maxmum=data["temp"].max()
#minimun=data["temp"].min()
#
#print(f"The maximum is :{maxmum}")
#print(f"The minimum is :{minimun}")
#print(data[data.day=="Monday"])
#print(data[data.temp==data.temp.max()].day)
monday=data[data.day=="Monday"]
monday_temp=monday.temp.to_list()
print(monday_temp[0]+10000)
dict_data={
        "Names":["Ali","Mustapha","Rida","Simo"],
        "Grade":[18,2,5,10]
        }
notes=pandas.DataFrame(dict_data)
notes.to_csv("semester_notes.csv")









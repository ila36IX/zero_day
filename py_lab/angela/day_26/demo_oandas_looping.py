import pandas
import random as r

my_dict={ "names":["Ali","Hanane","Kawtar","Rida","simo"],
          "score":[r.randint(0,100) for _ in range(5)]
        }

scores=pandas.DataFrame(my_dict)

for (index, row) in scores.iterrows():
    if row.names=="Ali":
        print(row.score+100000)

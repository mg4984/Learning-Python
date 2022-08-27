import pandas 

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv") 
gray = len(data[data["Primary Fur Color"] == "Gray"] )
black = len(data[data["Primary Fur Color"] == "Cinnamon"] )
cin = len(data[data["Primary Fur Color"] == "Black"] )
print(gray)
print(black)
print(cin) 

data_dict = {
    "Fur Colour" : ["gray" , "black" , "cin"],
    "Count" :  [gray , black , cin]
    
    
    
    }
df = pandas.DataFrame(data_dict)
df.to_csv("OKAY.csv")
#print(df)
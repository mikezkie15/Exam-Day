import pandas as pd 

#Series 

s = pd.Series([1,2,3,4,5])

#Data Frame
data = pd.DataFrame({
    "Name":["Mike","Mark Ryan","Marky"],
    "Age":[20,17,12],
    "Marks":[100,200,300]
})
print(data)
print(s)
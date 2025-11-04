import pandas as pd
data=[10,20,30,40]
series=pd.Series(data)
python_list=series.tolist()
print("Converted python_list:",python_list)
print("Type converted object:",type(python_list))

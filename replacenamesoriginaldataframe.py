import pandas as pd
import numpy as np
exam_data={
'name':['Alice','Bob','Charlie','David','Martin'],
'score':[18,np.nan,7,16,11],
'attempts':[2,1,3,1,2],
'qualify':['yes','no','no','yes','yes']
}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows:")
print(df)
print("change the name 'David' to 'Suresh':")
df['name']=df['name'].replace('David','Suresh')
print(df)

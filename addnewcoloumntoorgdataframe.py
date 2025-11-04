import pandas as pd
import numpy as np
exam_data={
'name':['Alice','Bob','Charlie','David','Martin'],
'score':[14,np.nan,11,9,15],
'attempts':[3,1,2,2,3],
'qualify':['yes','no','yes','no','yes']
}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows:")
print(df)
colour=['Red','Orange','Pink','Black','White']
df['color']=colour
print("New data frame after inserting 'color' column")
print(df)
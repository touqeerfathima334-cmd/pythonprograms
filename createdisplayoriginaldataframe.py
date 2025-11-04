import pandas as pd
import numpy as np
exam_data= {'name':
          ['alice','bob','charlie','david','martin'],
'score':[13,8,9,np.nan,17],
'attempts':[2,3,1,3,2],
'qualify':['yes','no','no','no','yes']
}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("Original rows:")
print(df)

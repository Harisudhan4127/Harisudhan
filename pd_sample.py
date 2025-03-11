"""
import pandas as pd
import numpy as np
# df = pd.read_csv("day2/sample.csv")
# print(df)
arr = np.array([[1,2,3],
                [4,5,6]])
data = {"id": [1,2,3,4],
      "name": ["logeshwari","kanagaraj","loki","logeshwaran"],
      "age": [18,31,999,99],
      "location": ["chennai","vannarupettai","Asgard","vannarupettai"],
      "Status": ["Housewife","Director","God of story","VIP"]}
df = pd.DataFrame(data)
# print(df)
print("-------------------------------------------------")
print(df.describe())
print(df.shape)
print(df.info())
"""
import pandas as pd
import numpy as np
df = pd.read_csv("Data/student.csv")
print(df.head())

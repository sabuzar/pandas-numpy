import pandas as pd
import numpy as np
dict1 = {
    "name":['abuzar', 'yousha', 'muaz', 'zain'],
    "marks":[5,10,7,15],
    "city":['chiniot','faislabad','dubai','salara']
}
fw = pd.DataFrame(dict1)
a=fw.head(2)
b=fw.tail(3)
#fw.to_csv('friends.csv')
#fw.to_csv('friends-index-false.csv',index=False)
c=fw.describe()
print(c)
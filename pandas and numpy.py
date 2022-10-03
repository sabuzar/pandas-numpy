import pandas as pd
import numpy as np
dict1 = {
    "name":['abuzar', 'yousha', 'muaz', 'zain'],
    "marks":[5,10,7,15],
    "city":['chiniot','faislabad','dubai','salara']
}
fw = pd.DataFrame(dict1)
print(fw)
fw.to_csv('friends.csv')
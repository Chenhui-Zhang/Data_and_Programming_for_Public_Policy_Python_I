#convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]

import numpy as np
start_array = np.array(start_list)
start_ravel=start_array.ravel()
for index in range(len(start_ravel)):
    if start_ravel[index]%2==0:
        start_ravel[index]=start_ravel[index]/2
    else:
        start_ravel[index]=0
print(start_ravel)

#Solution
[item for sublist in start_list for item in sublist if item%2==0]


#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'zach': datetime(2005, 8, 8)}

#dictionary
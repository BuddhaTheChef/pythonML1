
import pandas as pd
import os
import time
from datetime import datetime 

# Enter path name here vvv
path=""

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stock_list)

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)
                time.sleep(15)

Key_Stats()



# import matplotlib.pyplot as plt

# from sklearn import datasets
# from sklearn import svm

# digits = datasets.load_digits()

# clf = svm.SVC(gamma=0.0001, C=100)

# print(len(digits.data))

# x,y = digits.data[:-10], digits.target[:-10]

# clf.fit(x,y)

# print('Prediction:', clf.predict(digits.data[[-1]]))

# plt.imshow(digits.images[-1], cmap=plt.cm.gray_r,interpolation="nearest")

# plt.show()
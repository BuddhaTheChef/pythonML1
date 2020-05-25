
import pandas as pd
import os
import time
from datetime import datetime 

# Enter path name here vvv
path="/Users/ajwietechaii/Desktop/mlStocks/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
    # print(stock_list)

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("/Users/ajwietechaii/Desktop/mlStocks/intraQuarter/_KeyStats")[-1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                # print(date_stamp, unix_time)
                full_file_path = each_dir + '/' + file
                # print(full_file_path)
                source = open(full_file_path, 'r').read()
                # print(source)
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    df = df.append({'Date': date_stamp,'Unix': unix_time,'Ticker': ticker,'DE Ratio': value,}, ignore_index = True)
                except Exception as e:
                    pass

            save = gather.replace(' ','').replace(')','').replace('(','').replace('/','') + str('.csv')
            print(save)
            df.to_csv(save)

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
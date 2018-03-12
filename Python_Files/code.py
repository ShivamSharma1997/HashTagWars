import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

from utility import create_data, avg_len

data_location = '../data/train_dir/train_data'

Xs, ys, ht_list = create_data(data_location)

dic_len = []
hsh_lst = []

for i in range(len(Xs)):
    lst, hsh = avg_len(Xs[i], ys[i])
    dic_len.append(lst)
    hsh_lst.append(hsh)

hsh_lst = tuple(hsh_lst)
y_pos = np.arange(len(hsh_lst))

plt.bar(y_pos, dic_len, align='center', alpha=0.5)
plt.xticks(y_pos, hsh_lst)
plt.ylabel('Average Top 10 Sentence Length')
plt.title('#HashTags')
 
plt.show()
import pandas
from math import log2


def log(x):
    if x == 0:
        return 0
    else:
        return log2(x)


def H(p):
    return round((-p * log(p)) - ((1 - p) * log(1 - p)), 2)


def AE(p_j, d_p, d_n):
    return round((p_j * H(d_p)) + ((1 - p_j) * (H(d_n))), 2)


data = pandas.read_csv('data1.csv')

columns = ['f1', 'f3', 'f4']
# for i in range(len(data.iloc[-1]) - 1):
#     columns.append(f'f{i + 1}')
# columns.append('y')

data = data.astype(int)
# data = pandas.DataFrame(data.values, columns=columns)

for f in columns:
    if f == 'y':
        continue
    zeroes = data[data[f] == 0]
    ones = data[data[f] == 1]
    one_p = ones[ones['y'] == 1]
    zeroes_p = zeroes[zeroes['y'] == 1]
    h_p = H(len(one_p) / len(ones))
    h_n = H(len(zeroes_p) / len(zeroes))
    ae = AE(len(ones) / len(data), len(one_p) / len(ones), len(zeroes_p) / len(zeroes))
    print(f'AE({f}) = {ae}')
    print('#0 = ', len(zeroes))
    print('#1 = ', len(ones))
    print('1 --> #0 = ', len(ones) - len(one_p))
    print('1 --> #1 = ', len(one_p))
    print('0 --> #0 = ', len(zeroes) - len(zeroes_p))
    print('0 --> #1 = ', len(zeroes_p))
    print('H(D+) = ', h_p)
    print('H(D-) = ', h_n)
    print(zeroes)
    print(ones)
    print('----------------------------------------------------------------')
    # if f == 'f2':
    #     ones.to_csv('data1.csv', sep='\t', encoding='utf-8', index=False)

import pandas
from math import log2


def log(x):
    if x == 0:
        return 0
    else:
        return log2(x)


def prob(x, y):
    if y == 0:
        return 0
    return x / y


def H(p1, p2, p3):
    return round((-p1 * log(p1)) + (-p2 * log(p2)) + (-p3 * log(p3)), 2)


def AE(p1, p2, p3, d00, d01, d02, d10, d11, d12, d20, d21, d22):
    return round((p1 * (H(d00, d01, d02))) + (p2 * (H(d10, d11, d12))) + (p3 * (H(d20, d21, d22))), 2)


data = pandas.read_csv('data22.csv', header=None)

columns = []
for i in range(len(data.iloc[-1]) - 1):
    columns.append(f'f{i + 1}')
columns.append('y')

data = data.astype(int)
data = pandas.DataFrame(data.values, columns=columns)

for f in columns:
    if f == 'y': continue
    if f == 'f1': continue
    if f == 'f2': continue
    # if f == 'f3': continue
    # if f == 'f4': continue

    len_data = len(data)

    missing = data[data[f] == -1]
    zeroes = data[data[f] == 0]
    ones = data[data[f] == 1]
    twos = data[data[f] == 2]

    len_missing = len(missing)
    len_zeroes = len(zeroes)
    len_ones = len(ones)
    len_twos = len(twos)

    len_zeroes = len_zeroes + (len_missing * prob(len_zeroes, len_data - len_missing))
    len_ones = len_ones + (len_missing * prob(len_ones, len_data - len_missing))
    len_twos = len_twos + (len_missing * prob(len_twos, len_data - len_missing))

    zeroes_0 = zeroes[zeroes['y'] == 0]
    zeroes_1 = zeroes[zeroes['y'] == 1]
    zeroes_2 = zeroes[zeroes['y'] == 2]

    len_zeroes_0 = len(zeroes_0) + (len(missing[missing['y'] == 0]) * prob(len_zeroes, len_data))
    len_zeroes_1 = len(zeroes_1) + (len(missing[missing['y'] == 1]) * prob(len_zeroes, len_data))
    len_zeroes_2 = len(zeroes_2) + (len(missing[missing['y'] == 2]) * prob(len_zeroes, len_data))

    ones_0 = ones[ones['y'] == 0]
    ones_1 = ones[ones['y'] == 1]
    ones_2 = ones[ones['y'] == 2]

    len_ones_0 = len(ones_0) + (len(missing[missing['y'] == 0]) * prob(len_ones, len_data))
    len_ones_1 = len(ones_1) + (len(missing[missing['y'] == 1]) * prob(len_ones, len_data))
    len_ones_2 = len(ones_2) + (len(missing[missing['y'] == 2]) * prob(len_ones, len_data))

    twos_0 = twos[twos['y'] == 0]
    twos_1 = twos[twos['y'] == 1]
    twos_2 = twos[twos['y'] == 2]

    len_twos_0 = len(twos_0) + (len(missing[missing['y'] == 0]) * prob(len_twos, len_data))
    len_twos_1 = len(twos_1) + (len(missing[missing['y'] == 1]) * prob(len_twos, len_data))
    len_twos_2 = len(twos_2) + (len(missing[missing['y'] == 2]) * prob(len_twos, len_data))

    ae = AE(
        prob(len_zeroes, len_data), prob(len_ones, len_data), prob(len_twos, len_data),
        prob(len_zeroes_0, len_zeroes), prob(len_zeroes_1, len_zeroes), prob(len_zeroes_2, len_zeroes),
        prob(len_ones_0, len_ones), prob(len_ones_1, len_ones), prob(len_ones_2, len_ones),
        prob(len_twos_0, len_twos), prob(len_twos_1, len_twos), prob(len_twos_2, len_twos)
    )

    print(f'AE({f}) = {ae}')
    print(f'#0 = {len_zeroes}')
    print(f'#1 = {len_ones}')
    print(f'#2 = {len_twos}')

    print()
    print('0 --> #0 = ', len_zeroes_0)
    print('0 --> #1 = ', len_zeroes_1)
    print('0 --> #2 = ', len_zeroes_2)
    print(f'H(D_0) = {H(prob(len_zeroes_0, len_zeroes), prob(len_zeroes_1, len_zeroes), prob(len_zeroes_2, len_zeroes))}')
    print(zeroes)

    print()
    print('1 --> #0 = ', len_ones_0)
    print('1 --> #1 = ', len_ones_1)
    print('1 --> #2 = ', len_ones_2)
    print(f'H(D_1) = {H(prob(len_ones_0, len_ones), prob(len_ones_1, len_ones), prob(len_ones_2, len_ones))}')
    print(ones)

    print()
    print('2 --> #0 = ', len_twos_0)
    print('2 --> #1 = ', len_twos_1)
    print('2 --> #2 = ', len_twos_2)
    print(f'H(D_2) = {H(prob(len_twos_0, len_twos), prob(len_twos_1, len_twos), prob(len_twos_2, len_twos))}')
    print(twos)

    print('-----------------------------------------------------------------------------------------------------------')
    # if f == 'f2':
    #     zeroes.to_csv('data20.csv', sep=',', encoding='utf-8', index=False, header=None)
    #     ones.to_csv('data21.csv', sep=',', encoding='utf-8', index=False, header=None)
    #     twos.to_csv('data22.csv', sep=',', encoding='utf-8', index=False, header=None)

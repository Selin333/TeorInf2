import numpy as np

def encode(str_to_conv):
    str_to_conv = "abcd5ttF%"
    print(str_to_conv)
    bin_str = ''.join(format(ord(x), '08b') for x in str_to_conv)
    return bin_str
# orig_strin = input('Введите строку  ')
orig_strin = 'abcd'
# kol_summ = int(input('Введите кол сумматоров  '))
kol_summ = 3
summatory = []
for i in range(kol_summ):
    summator = input('Введите сумматороы  ')

    s = summator.split(',')
    for j in range(len(s)):
        s[j] = int(s[j])
    summatory.append(s)
    print(summatory)
print(summatory)

bit_str = encode(orig_strin)
print(bit_str)

registr = np.array([0]*kol_summ)
summa = []
registr
for i in range(len(bit_str)):
    registr[0] = int(bit_str[i])
    for j in range(kol_summ):
        for n in summatory:
            for k in n:
                sum |= registr[k]
            suma.append(registr[k])
    registr = np.roll(registr,1)
        #summa.append(int(bit_str[summatory[]]))


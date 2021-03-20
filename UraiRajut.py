def urai (x):
    # variabel baru untuk menyimpan hasil text yang akan diurai
    result = ''
    # pada tiap iterasi, akan ditambahkan character dari index 0 s.d. i
    for i in range(len(x)):
        result = result + x[:i+1]
    return result
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print('') # spasi
def rajut (x):
    result2 = ''
    for i in x:
        if i not in result2:
            result2 = result2 + i
    return result2

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
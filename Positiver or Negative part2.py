def pon(answer):
    return answer > 0

for val in [-10,0,5,20]:
    result = pon(val)
    if pon(val):
        print(val,result,'positive')
    else:
        print(val,result,'negative')
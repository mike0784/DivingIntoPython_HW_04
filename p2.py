def rev_kwargs(**kwargs):
    result = {}
    for k, v in kwargs.items():
        try:
            hash(v)
            result[v] = k
        except:
            temp = str(v)
            result[temp] = k
        
    return result

result = rev_kwargs(res=1, reverse=[1, 2, 3])
print(result)
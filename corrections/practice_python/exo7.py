def transformer(a):
    #       on garde x,  on itère sur les éléments de a et on les note x,   et on filtre par rapport aux x pairs!
    return [    x                   for x in a                                      if x % 2 == 0                ]


print(transformer([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))

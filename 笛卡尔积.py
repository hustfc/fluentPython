colors = ['black', 'white']
sizes = ['S', 'M', 'L']

#首先按照size排序，然后按照color排序，python自动忽略[]里面的换行符
tshits = [(color, size) for color in colors
                        for size in sizes]
print(tshits)

#这里首先也是对size进行排序
for color in colors:
    for size in sizes:
        print((color, size))

#首先对color进行排序
tshits = [(color, size) for size in sizes
                        for color in colors]
print(tshits)
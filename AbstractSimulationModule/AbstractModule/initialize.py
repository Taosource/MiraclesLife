from collections import namedtuple

basic = namedtuple('basic', ['x', 'y', 'types', 'ids', 'sequential'])
#  x, y, types, sequences = x坐标，y坐标，类型，编号，时序编号
aa = []
x = [x for x in range(10)]
y = [x for x in range(10)]
types = [x for x in range(10)]
ids = [x for x in range(10)]
sequential = [x for x in range(10)]
alls = []
for i in range(10):
    allss = list(range(10))
    allss[i] = x[i]
    allss[i] = y[i]
    allss[i] = types[i]
    allss[i] = ids[i]
    allss[i] = sequential[i]
    alls.append(allss)
def test():
    bb =[]
    for i in range(10):
        basic.x = i*2
        basic.y = i*3
        basic.types = i*4
        basic.ids = i*5
        basic.sequential = i*6
        print(basic.x)
        bb.append(basic)
    print(len(bb))
    print(bb[6].x)


test()

    
a =  [[4,[],0],[],[1,[2,[3]],8,5],[],[10]]
b =  [[[9,[10,2]],[5,[8,6],6,4,[9,10]],10],[6,9,[[10,1]]],[],[[[6,6,6,8,8],3],[6,[]],[[0,5,5,10],4,1,[3,3]],8]]


def comp(x, y):

    # if isinstance(l1, list) and isinstance(l2, list):
    # for e1, e2 in zip(l1, l2):
    #     if (comparison := in_order(e1, e2)) is not None:
    #         return comparison
    # return in_order(len(l1), len(l2))
    if isinstance(x, list) and isinstance(y, list):
        for xx, yy in zip(x,y):
            if xx == yy:
                return True
            if not comp(xx, yy):
                return False
        return len(x) <= len(y)

    if isinstance(x, list):
        return comp(x[0], y) if x else False
    
    if isinstance(y, list):
        return comp(x, y[0]) if y else False

    return x <= y

def in_order(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        return l1 < l2

    if isinstance(l1, list) and isinstance(l2, list):
        for e1, e2 in zip(l1, l2):
            if (comparison := in_order(e1, e2)) is not None:
                return comparison
        return in_order(len(l1), len(l2))

    if isinstance(l1, int):
        return in_order([l1], l2)
    return in_order(l1, [l2])

file_input = [eval(x.replace('\n', ',')) for x in open("2022/input/day_13.txt").read().split("\n\n")]
print(sum(i for i, (a, b) in enumerate(file_input, start=1) if comp(a,b)))


file_input = [eval(x.replace('\n', ',')) for x in open("2022/input/day_13.txt").read().split("\n\n")]
print(sum(i for i, (a, b) in enumerate(file_input, start=1) if in_order(a,b)))


print(comp(a,b))

print(
    {
        i for i, (a, b) in enumerate(file_input, start=1) if in_order(a, b)
    }.difference(
        {i for i, (a, b) in enumerate(file_input, start=1) if comp(a,b)}
    )
)
# 5350
# for i, (a, b) in enumerate(file_input, start=1):







hand_ord = lambda h: [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5,]].index(sorted(h.count(c) for c in set(h)))


file_input = open("2023/input/day_7.txt").read().translate(str.maketrans("AKQJT", "EDCBA")).split("\n")
print(sum(i*b+b for i, (_, b) in enumerate(sorted(((hand_ord(h), h),  int(b)) for h, b in map(str.split, file_input)))))
print(sum(i*b+b for i, (_, b) in enumerate(sorted(((max(hand_ord(h.replace('B', j)) for j in '23456789ACDE'), h.replace('B', '0')), b) for h, b in [(h, int(b)) for h, b in map(str.split, file_input)]))))


import re

print(sum(int(2**(len(eval('{'+line.replace(',|',"}&{")+"}"))-1)) for line in re.sub('(?<=\d) ',',',re.sub(".+:","",open("2023/input/day_4.txt").read())).split('\n')))


vals = [1]*len(list(open("2023/input/day_4.txt")))
for index, line in enumerate(re.sub('(?<=\d) ',',',re.sub(".+:","",open("2023/input/day_4.txt").read())).split('\n')):
    for i in range(len(eval('{'+line.replace(',|',"}&{")+"}"))):
        vals[index + i + 1] += vals[index]
print(sum(vals))




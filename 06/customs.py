with open(f'06/input.txt') as f:
    lines = f.read().split("\n")

st = set()
ls = list()
ctr = 0
res1 = 0
res2 = 0

for i, line in enumerate(lines):
    if line != '':
        ctr = ctr + 1
        for j in line:
            st.add(j)
            ls.append(j)
    if line == '' or i == len(lines) - 1:
        res1 = res1 + len(st)
        st = set()
        for k in ls:
            if ls.count(k) == ctr:
                res2 = res2 + 1
            ls = [x for x in ls if x != k]
        ls = list()
        ctr = 0

print(res1)
print(res2)
import math

GC_content = [0.070, 0.152, 0.203, 0.235, 0.333, 0.371, 0.418, 0.487, 0.547, 0.603, 0.641, 0.695, 0.746, 0.792, 0.870, 0.942]

AT = []
GC = []

for i in GC_content:
    AT.append((1-i)/2)
    GC.append(i/2)

# print(AT)
# print(GC)

DNA = "CCGTGTCCCGTGCGTGAAGCTCCGTGTGGCCGAACAGTCGAAATAGTCCATGTATGCAAACCGTTTTGGCGTAGGTAGTCCAACCA"

AT_num = 0
GC_num = 0

for i in DNA:
    AT_num += i == "A" or i == "T"
    GC_num += i == "G" or i == "C"

# print(AT_num)
# print(GC_num)

AT_prob = []
for i in AT:
    AT_prob.append(i**AT_num)
#print(AT_prob)

GC_prob = []
for i in GC:
    GC_prob.append(i**GC_num)
#print(GC_prob)

prob = []

for i, j in zip(AT_prob, GC_prob):
    prob.append(math.log10(i*j))

prob_3dp = []
for i in prob:
    prob_3dp.append("{:.3f}".format(i))

print(prob_3dp)
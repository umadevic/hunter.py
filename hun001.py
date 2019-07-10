path9=int(input())
bin=[int(i) for i in input().split()]
pest3=0
for l in range(path):
   for j in range(l):
      if bin[j]<bin[l]:
         pest3+=bin[j]
print(pest3) 

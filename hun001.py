path7=int(input())
bin=[int(i) for i in input().split()]
pest8=0
for k in range(path7):
   for j in range(k):
      if bin[j]<bin[k]:
         pest8+=bin[j]
print(pest8) 

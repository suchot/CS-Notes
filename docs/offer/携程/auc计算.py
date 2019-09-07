n = int(input())
prob,label = [0 for i in range(n)],[0 for i in range(n)]
for i in range(n):
    label[i],prob[i] = map(float, input().split())
def calAUC(prob, label):
    f = list(zip(prob, label))
    rank = [v2 for v1,v2 in sorted(f,key=lambda x:x[0])]
    ranklist = [i+1 for i in range(len(rank)) if rank[i]==1]
    posnum,negnum = 0,0
    for i in range(len(label)):
        if label[i]== 1:
            posnum +=1
        else:
            negnum += 1
    auc = 0
    auc = (sum(ranklist)-(posnum*(posnum+1))/2)/(posnum*negnum)
    return auc
print(calAUC(prob, label))
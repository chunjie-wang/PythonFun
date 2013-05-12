import sys
#sys.stdin=open('input.txt', 'r')
sys.stdout=open('output.txt', 'w')
sys.stdin=open('B-small-practice.in', 'r')

I=lambda:map(int, raw_input().split())
t=input()
def ok(a, i, j, n, m):
    if any(a[i][k]>a[i][j] for k in xrange(0,m)) and any(a[k][j]>a[i][j] for k in xrange(0,n)): 
        return False;
    return True

def solve(a, n, m):
    for i in xrange(0,n):
        for j in xrange(0,m):
            if not ok(a, i, j, n, m):
                return 'NO'
    return 'YES'

for i in xrange(1,t+1):
    n,m=I()
    d=[]
    for j in xrange(n):
        d.append(I())
    print "Case #%d: %s"%(i,solve(d,n,m))

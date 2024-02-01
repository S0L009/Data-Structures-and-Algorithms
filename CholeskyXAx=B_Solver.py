import numpy as np
def Cholesky(A):
    lg=A.shape
    L=np.zeros(lg)
    for i in range(lg[0]):
        for j in range(0,i+1):
            if i==j:
                L[i][j]=np.sqrt(A[i][j]-sum([ L[i][k]**2 for k in range(0,i) ]))      #generalised formula for Cholesky
            else:
                L[i][j]=(A[i][j]-sum([ L[i][k]*L[j][k] for k in range(j) ]))/L[j][j]
    return L

def Ax_b(L):   #Ax=b Solver
    print(f"L*L' = A  ->\n\n{np.dot(L,L.transpose())}")

    y=np.zeros((L.shape[0],1))
    for i in range(L.shape[0]):
        y[i]=(mapped_adj_matrix[i]-sum([ L[i][j]*y[j] for j in range(0,i) ]))/L[i][i]

    print(f"\n\nL*y = b  ->\n\n{np.dot(L,y)}")

    L=L.transpose()

    x=np.zeros((L.shape[0],1))
    for i in range(L.shape[0]-1,-1,-1):
        x[i]=(y[i]-sum([ L[i][j]*x[j] for j in range(i+1,L.shape[0]) ]))/L[i][i]

    print(f"\n\nL'*x = y  ->\n\n{np.dot(L,x)}")

    return x

n=5
A=np.random.randint(-9,9,(n,n))
A=np.dot(A,A.transpose())

mapped_adj_matrix=np.random.randint(-5,5,(n,1))

print('A -> \n',A,'\n\nb -> \n',mapped_adj_matrix,'\n')
L=Cholesky(A)
x=Ax_b(L)
print(f"\nx->\n{x}")
print(f"\n\nA'*x = b  ->\n\n{np.dot(A,x)}")
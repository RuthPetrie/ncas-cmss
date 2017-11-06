from scipy.linalg import svd
from scipy.linalg import inv

for j in arange(0, nx_step):
    coefa[j, (j-1)%nx_step] = -lamb
    coefa[j, (j)%nx_step] = 2*lamb + 2.
    coefa[j, (j+1)%nx_step] = -lamb

lamb = – lamb
for j in arange(0, nx_step):
    coefb[j, (j-1)%nx_step] = - lamb
    coefb[j, (j)%nx_step] = 2*lamb + 2.
    coefb[j, (j+1)%nx_step] = -lamb

coefa = scipy.linalg.inv(coefa)         # inverse of A
coef = numpy.dot(coefa, coefb)   
coef = scipy.linalg.inv(coef)

for i in arange(1,nt_step):        #———– main loop ———

    ans = scipy.linalg.solve(coef, uo)
    uo = ans
    plot(uoz,’k', ans,’r')
        draw()
    t[i] = t[i-1] + dt
    print dt*nt_step - t[i], ‘      ‘, ans.sum()
    rho[:,i] = ans

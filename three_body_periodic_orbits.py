import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10,10)


def eq_of_motion(t,f):
    G=1
    m1=1
    m2=1
    m3=1
    return np.array([f[6]/m1, f[7]/m1, f[8]/m2, f[9]/m2, f[10]/m3, f[11]/m3, m1*((G*m2*(f[2]-f[0]))/((((f[0]-f[2])**2)+((f[1]-f[3])**2))**1.5) - (G*m3*(f[0]-f[4]))/((((f[0]-f[4])**2)+((f[1]-f[5])**2))**1.5)), m1*((G*m2*(f[3]-f[1]))/((((f[0]-f[2])**2)+((f[1]-f[3])**2))**1.5) - (G*m3*(f[1]-f[5]))/((((f[0]-f[4])**2)+((f[1]-f[5])**2))**1.5)), m2*((G*m3*(f[4]-f[2]))/((((f[2]-f[4])**2)+((f[3]-f[5])**2))**1.5) - (G*m1*(f[2]-f[0]))/((((f[2]-f[0])**2)+((f[3]-f[1])**2))**1.5)), m2*((G*m3*(f[5]-f[3]))/((((f[2]-f[4])**2)+((f[3]-f[5])**2))**1.5) - (G*m1*(f[3]-f[1]))/((((f[2]-f[0])**2)+((f[3]-f[1])**2))**1.5)), m3*((G*m1*(f[0]-f[4]))/((((f[4]-f[0])**2)+((f[5]-f[1])**2))**1.5) - (G*m2*(f[4]-f[2]))/((((f[4]-f[2])**2)+((f[5]-f[3])**2))**1.5)), m3*((G*m1*(f[1]-f[5]))/((((f[4]-f[0])**2)+((f[5]-f[1])**2))**1.5) - (G*m2*(f[5]-f[3]))/((((f[4]-f[2])**2)+((f[5]-f[3])**2))**1.5))])


def rk4(f,t,h,g,atol,rtol):
    k1 = h*g(t,f)
    k2 = h*g(t+0.5*h, f+0.5*k1)
    k3 = h*g(t+0.5*h, f+0.5*k2)
    k4 = h*g(t+h, f+k3)

    return f+ k1/6. + k2/3. + k3/3. + k4/6., h


def rk_driver(f0, tstart, tstop, h, atol, rtol, rhs, method):

    if method == 'rk4':
        stepper = rk4
    elif method == 'rkf_nr':
        stepper = rkf_nr
    else:
        raise ValueError("{} is not a supported integrator. Valid choices are rk4 or rkf_nr".format(stepper))

    t = [tstart]
    x_1 = [f0[0]]
    y_1 = [f0[1]]
    x_2 = [f0[2]]
    y_2 = [f0[3]]
    x_3 = [f0[4]]
    y_3 = [f0[5]]
    p_x_1 = [f0[6]]
    p_y_1 = [f0[7]]
    p_x_2 = [f0[8]]
    p_y_2 = [f0[9]]
    p_x_3 = [f0[10]]
    p_y_3 = [f0[11]]
    xold = f0

    while t[-1] < tstop:
        xold,t_h = stepper(xold,t[-1],h,rhs,atol,rtol)
        t.append(t[-1]+t_h)
        x_1.append(xold[0])
        y_1.append(xold[1])
        x_2.append(xold[2])
        y_2.append(xold[3])
        x_3.append(xold[4])
        y_3.append(xold[5])
        p_x_1.append(xold[6])
        p_y_1.append(xold[7])
        p_x_2.append(xold[8])
        p_y_2.append(xold[9])
        p_x_3.append(xold[10])
        p_y_3.append(xold[11])

    return x_1,y_1,x_2,y_2,x_3,y_3,p_x_1,p_y_1,p_x_2,p_y_2,p_x_3,p_y_3,t


x_1_0 = 1
y_1_0 = 0
x_2_0 = -1
y_2_0 = 0
x_3_0 = 0
y_3_0 = 0
p_x_1_0 = 0.306892758965492
p_y_1_0 = 0.125506782829762
p_x_2_0 = p_x_1_0
p_y_2_0 = p_y_1_0
p_x_3_0 = -2*p_x_1_0
p_y_3_0 = -2*p_y_1_0
T = 6.23564136316479


x_1,y_1,x_2,y_2,x_3,y_3,p_x_1,p_y_1,p_x_2,p_y_2,p_x_3,p_y_3,t = rk_driver(np.array([x_1_0,y_1_0,x_2_0,y_2_0,x_3_0,y_3_0,p_x_1_0,p_y_1_0,p_x_2_0,p_y_2_0,p_x_3_0,p_y_3_0]),0,T,1e-4,1e-5,1e-6,eq_of_motion,method='rk4')


plt.figure()
plt.scatter(x_1,y_1,label='Body 1')
plt.scatter(x_2,y_2,label='Body 2')
plt.scatter(x_3,y_3,label='Body 3')
plt.scatter(x_1_0,y_1_0,color='black',label='IP Body 1')
plt.scatter(x_2_0,y_2_0,color='yellow',label='IP Body 2')
plt.scatter(x_3_0,y_3_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.figure()
plt.scatter(p_x_1,p_y_1,label='Body 1')
plt.scatter(p_x_2,p_y_2,label='Body 2')
plt.scatter(p_x_3,p_y_3,label='Body 3')
plt.scatter(p_x_1_0,p_y_1_0,color='black',label='IP Body 1')
plt.scatter(p_x_2_0,p_y_2_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_3_0,p_y_3_0,color='white',label='IP Body 3')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.legend()


x_11_0 = 1
y_11_0 = 0
x_22_0 = -1
y_22_0 = 0
x_33_0 = 0
y_33_0 = 0
p_x_11_0 = 0.2554309326049807
p_y_11_0 = 0.516385834327506
p_x_22_0 = p_x_11_0
p_y_22_0 = p_y_11_0
p_x_33_0 = -2*p_x_11_0
p_y_33_0 = -2*p_y_11_0
T = 35.042


x_11,y_11,x_22,y_22,x_33,y_33,p_x_11,p_y_11,p_x_22,p_y_22,p_x_33,p_y_33,t = rk_driver(np.array([x_11_0,y_11_0,x_22_0,y_22_0,x_33_0,y_33_0,p_x_11_0,p_y_11_0,p_x_22_0,p_y_22_0,p_x_33_0,p_y_33_0]),0,T,1e-4,1e-5,1e-6,eq_of_motion,method='rk4')


plt.figure()
plt.scatter(x_11,y_11,label='Body 1')
plt.scatter(x_11_0,y_11_0,color='black',label='IP Body 1')
plt.scatter(x_22_0,y_22_0,color='yellow',label='IP Body 2')
plt.scatter(x_33_0,y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()
plt.scatter(x_22,y_22,color='blue',label='Body 2')
plt.scatter(x_11_0,y_11_0,color='black',label='IP Body 1')
plt.scatter(x_22_0,y_22_0,color='yellow',label='IP Body 2')
plt.scatter(x_33_0,y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()
plt.scatter(x_33,y_33,color='purple',label='Body 3')
plt.scatter(x_11_0,y_11_0,color='black',label='IP Body 1')
plt.scatter(x_22_0,y_22_0,color='yellow',label='IP Body 2')
plt.scatter(x_33_0,y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.figure()
plt.scatter(p_x_11,p_y_11,label='Body 1')
plt.scatter(p_x_11_0,p_y_11_0,color='black',label='IP Body 1')
plt.scatter(p_x_22_0,p_y_22_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_33_0,p_y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()
plt.scatter(p_x_22,p_y_22,color='blue',label='Body 2')
plt.scatter(p_x_11_0,p_y_11_0,color='black',label='IP Body 1')
plt.scatter(p_x_22_0,p_y_22_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_33_0,p_y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()
plt.scatter(p_x_33,p_y_33,color='purple',label='Body 3')
plt.scatter(p_x_11_0,p_y_11_0,color='black',label='IP Body 1')
plt.scatter(p_x_22_0,p_y_22_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_33_0,p_y_33_0,color='white',label='IP Body 3')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.legend()


def rkf_nr(f,t,h,g,atol,rtol):

    k1 = h*g(t,f)
    k2 = h*g(t+(1./5.)*h, f+(1./5.)*k1)
    k3 = h*g(t+(3./10.)*h, f+(3./40.)*k1+(9./40.)*k2)
    k4 = h*g(t+(4./5.)*h, f+(44./45.)*k1-(56./15.)*k2+(32./9.)*k3)
    k5 = h*g(t+(8./9.)*h, f+(19372./6561.)*k1-(25360./2187.)*k2+(64448./6561.)*k3-(212./729.)*k4)
    k6 = h*g(t+h, f+(9017./3168.)*k1-(355./33.)*k2+(46732./5247.)*k3+(49./176.)*k4-(5103./18656.)*k5)

    f1 = f+(35./384.)*k1+(500./1113.)*k3+(125./192.)*k4-(2187./6784.)*k5+(11./84.)*k6

    k7 = h*g(t+h, f1)

    f2 = f+(5179./57600.)*k1+(7571./16695.)*k3+(393./640.)*k4-(92097./339200.)*k5+(187./2100.)*k6+(1./40.)*k7

    N = len(f)
    X = []
    for i in range (0,N):
        x = ((np.abs(f1[i]-f2[i]))/(atol+max(np.abs(f[i]),np.abs(f1[i]))*rtol))**2
        X.append(x)

    err_0=1
    err = np.sqrt((1/N)*np.sum(X))

    h0 = h*((np.abs(err_0/err))**(1/5))

    if err > 1:
        f2, h0 = rkf_nr(f,t,h0,g,atol,rtol)

    return f2, h0


x_1,y_1,x_2,y_2,x_3,y_3,p_x_1,p_y_1,p_x_2,p_y_2,p_x_3,p_y_3,t = rk_driver(np.array([x_1_0,y_1_0,x_2_0,y_2_0,x_3_0,y_3_0,p_x_1_0,p_y_1_0,p_x_2_0,p_y_2_0,p_x_3_0,p_y_3_0]),0,T,1e5,1e-8,1e-8,eq_of_motion,method='rkf_nr')


plt.figure()
plt.scatter(x_1,y_1,label='Body 1')
plt.scatter(x_2,y_2,label='Body 2')
plt.scatter(x_3,y_3,label='Body 3')
plt.scatter(x_1_0,y_1_0,color='black',label='IP Body 1')
plt.scatter(x_2_0,y_2_0,color='yellow',label='IP Body 2')
plt.scatter(x_3_0,y_3_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()


plt.figure()
plt.scatter(p_x_1,p_y_1,label='Body 1')
plt.scatter(p_x_2,p_y_2,label='Body 2')
plt.scatter(p_x_3,p_y_3,label='Body 3')
plt.scatter(p_x_1_0,p_y_1_0,color='black',label='IP Body 1')
plt.scatter(p_x_2_0,p_y_2_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_3_0,p_y_3_0,color='white',label='IP Body 3')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.legend()


x_11,y_11,x_22,y_22,x_33,y_33,p_x_11,p_y_11,p_x_22,p_y_22,p_x_33,p_y_33,t = rk_driver(np.array([x_11_0,y_11_0,x_22_0,y_22_0,x_33_0,y_33_0,p_x_11_0,p_y_11_0,p_x_22_0,p_y_22_0,p_x_33_0,p_y_33_0]),0,T,1e5,1e-8,1e-8,eq_of_motion,method='rkf_nr')


plt.figure()
plt.scatter(x_11,y_11,label='Body 1')
plt.scatter(x_22,y_22,label='Body 2')
plt.scatter(x_33,y_33,label='Body 3')
plt.scatter(x_11_0,y_11_0,color='black',label='IP Body 1')
plt.scatter(x_22_0,y_22_0,color='yellow',label='IP Body 2')
plt.scatter(x_33_0,y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()


plt.figure()
plt.scatter(p_x_11,p_y_11,label='Body 1')
plt.scatter(p_x_22,p_y_22,label='Body 2')
plt.scatter(p_x_33,p_y_33,label='Body 3')
plt.scatter(p_x_11_0,p_y_11_0,color='black',label='IP Body 1')
plt.scatter(p_x_22_0,p_y_22_0,color='yellow',label='IP Body 2')
plt.scatter(p_x_33_0,p_y_33_0,color='white',label='IP Body 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.figure()


def rp_function(X_0, tstart, T_0, h, atol, rtol, rhs, method):
    if method == 'rkf':
        stepper = rkf
    elif method == 'rk4':
        stepper = rk4
    elif method == 'rkf_nr':
        stepper = rkf_nr
    else:
        raise ValueError("{} is not a supported integrator. Valid choices are rkf, rkf_nr or rk4".format(stepper))

    t = [tstart]
    d = [100000000.]

    while t[-1] < T_0:
        X_i, t_h = stepper(X_0, t[-1], h, rhs, atol, rtol)
        t.append(t[-1] + t_h)
        X_i_1, t_h = stepper(X_i, t[-1], h, rhs, atol, rtol)
        t.append(t[-1] + t_h)
        d_value = np.linalg.norm(((X_0 - X_i) - (
                    ((np.dot((X_i_1 - X_i), (X_0 - X_i))) / ((np.linalg.norm(X_i_1 - X_i)) ** 2)) * (X_i_1 - X_i))))

        if d_value < d[-1]:
            d[-1] = d_value
        elif d_value == 0:
            d[-1] = d_value
            T_0 = t[-1]
        X_0 = X_i
        X_i = X_i_1

    return 'd', d, 'T', t[-1]


def ds_initial(n,N,m,M):
    initial_vectors=[]
    p_x_1_min = n
    p_y_1_min = m
    p_x_1_max = N
    p_y_1_max = M
    for i in range (0,N):
        for j in range (0,M):
            p_x_1_0 = p_x_1_min + i*((p_x_1_max-p_x_1_min)/N)
            p_y_1_0 = p_y_1_min + j*((p_y_1_max-p_y_1_min)/M)
            initial=np.array([1,0,-1,0,0,0,p_x_1_0,p_y_1_0,p_x_1_0,p_y_1_0,-2*p_x_1_0,-2*p_y_1_0])
            array = [i+n,j+n,initial]
            initial_vectors.append(array)

    return(initial_vectors)


initials_1 = ds_initial(1,3,1,4)


def prox_array(X_0, tstart, T_0, h, atol, rtol, rhs, rp_function, method):
    D=[]
    for i in range (0,len(X_0)):
        d=rp_function(X_0[i][2], tstart, T_0, h, atol, rtol, rhs, method)
        array = [X_0[i][0],X_0[i][1],d]
        D.append(array)
    return D


D = prox_array(initials_1,0,100,1e5,1e-3,1e-6,eq_of_motion,rp_function,method='rkf_nr')
print(D)


positions=[2,3,6,7,11]
for i in positions:
    x_1,y_1,x_2,y_2,x_3,y_3,p_x_1,p_y_1,p_x_2,p_y_2,p_x_3,p_y_3,t = rk_driver(np.array(initials_1[i][2]),0,T,1e5,1e-8,1e-8,eq_of_motion,method='rkf_nr')
    plt.figure()
    plt.scatter(x_1,y_1,label='Body 1')
    plt.scatter(x_2,y_2,label='Body 2')
    plt.scatter(x_3,y_3,label='Body 3')
    plt.scatter(x_1_0,y_1_0,color='black',label='IP Body 1')
    plt.scatter(x_2_0,y_2_0,color='yellow',label='IP Body 2')
    plt.scatter(x_3_0,y_3_0,color='white',label='IP Body 3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()


    
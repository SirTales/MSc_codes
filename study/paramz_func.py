'''
Created by de Paula, Tales Ferraz, 2022.

Contact info: ferrazdepaula@ifsc.usp.br


This code calculates the parameters for the alternative functions proposed by Dr. Arbeletche (2020)
https://doi.org/10.1016/j.astropartphys.2019.102389
'''


import numpy as np

########## Generalized Gumbel Distribution ##########

def paramGGD(A, E0):
        a0 = 1.24
        a1 = 11.74
        a2 = -6.85
        b0 = -0.088
        b1 = -1.393
        b2 = 0.855
        c0 = 0.00302
        c1 = 0.04702
        c2 = -0.02778 
        
        d0 = -368.79
        d1 = -238.75
        d2 = -32.14
        e0 = 61.443 
        e1 = 25.159
        e2 = 1.255
        f0 = -0.1138
        f1 = -0.7326
        f2 = 0
        
        g0 = 55.9
        g1 = 20.9
        g2 = -15.9
        h0 = -1.08
        h1 = 0.32
        h2 = 0
        i0 = 0
        i1 = 0
        i2 = 0
        
        a = a0 + a1*np.log10(A) + a2*((np.log10(A))**2)
        b = b0 + b1*np.log10(A) + b2*((np.log10(A))**2)
        c = c0 + c1*np.log10(A) + c2*((np.log10(A))**2)
        Lambda = a + b*np.log10(E0) + c*((np.log10(E0))**2)

        d = d0 + d1*np.log10(A) + d2*((np.log10(A))**2)
        e = e0 + e1*np.log10(A) + e2*((np.log10(A))**2)
        f = f0 + f1*np.log10(A) + f2*((np.log10(A))**2)
        Mu = d + e*np.log10(E0) + f*((np.log10(E0))**2)
        
        g = g0 + g1*np.log10(A) + g2*((np.log10(A))**2)
        h = h0 + h1*np.log10(A) + h2*((np.log10(A))**2)
        i = i0 + i1*np.log10(A) + i2*((np.log10(A))**2)
        Sigma = g + h*np.log10(E0) + i*((np.log10(E0))**2)
    

        return [Lambda, Sigma, Mu]

########## Exponentially Modified Gausian distribution ##########
    
def paramEMD(A, E0):
        a0 = 391.6
        a1 = -354.39
        a2 = 97.21
        b0 = -31.848
        b1 = 31.654
        b2 = -9.193
        c0 = 0.7526
        c1 = -0.7955
        c2 = 0.2407 
        
        d0 = -544.3
        d1 = -152.02
        d2 = -33.81
        e0 = 76.067 
        e1 = 17.644
        e2 = 1.251
        f0 = -0.4692
        f1 = -0.5436
        f2 = 0
        
        g0 = 44.9
        g1 = -2.7
        g2 = -4.35
        h0 = -1.03
        h1 = 0.25
        h2 = 0
        i0 = 0
        i1 = 0
        i2 = 0
        
        a = a0 + a1*np.log10(A) + a2*((np.log10(A))**2)
        b = b0 + b1*np.log10(A) + b2*((np.log10(A))**2)
        c = c0 + c1*np.log10(A) + c2*((np.log10(A))**2)
        Lambda = a + b*np.log10(E0) + c*((np.log10(E0))**2)

        d = d0 + d1*np.log10(A) + d2*((np.log10(A))**2)
        e = e0 + e1*np.log10(A) + e2*((np.log10(A))**2)
        f = f0 + f1*np.log10(A) + f2*((np.log10(A))**2)
        Mu = d + e*np.log10(E0) + f*((np.log10(E0))**2)
        
        g = g0 + g1*np.log10(A) + g2*((np.log10(A))**2)
        h = h0 + h1*np.log10(A) + h2*((np.log10(A))**2)
        i = i0 + i1*np.log10(A) + i2*((np.log10(A))**2)
        Sigma = g + h*np.log10(E0) + i*((np.log10(E0))**2)
    

        return [Lambda, Sigma, Mu]

### paramLND stands for parameters for the Log-Normal distribution ###
    
        a0 = 8.974
        a1 = -0.84
        a2 = 0.317
        b0 = -0.3978
        b1 = 0.0684
        b2 = -0.0344
        c0 = 0.0096
        c1 = 0
        c2 = 0 
        
        d0 = 0.532
        d1 = -0.08
        d2 = -0.04
        e0 = -0.0065
        e1 = -0.01
        e2 = 0.0066
        f0 = 0
        f1 = 0
        f2 = 0
        
        g0 = -1152.4
        g1 = 64.9
        g2 = -50
        h0 = 129.78
        h1 = -8.74
        h2 = 4.65
        i0 = -1.846
        i1 = 0
        i2 = 0
        
        a = a0 + a1*np.log10(A) + a2*((np.log10(A))**2)
        b = b0 + b1*np.log10(A) + b2*((np.log10(A))**2)
        c = c0 + c1*np.log10(A) + c2*((np.log10(A))**2)
        Sigma = a + b*np.log10(E0) + c*((np.log10(E0))**2)

        d = d0 + d1*np.log10(A) + d2*((np.log10(A))**2)
        e = e0 + e1*np.log10(A) + e2*((np.log10(A))**2)
        f = f0 + f1*np.log10(A) + f2*((np.log10(A))**2)
        Mu = d + e*np.log10(E0) + f*((np.log10(E0))**2)
        
        g = g0 + g1*np.log10(A) + g2*((np.log10(A))**2)
        h = h0 + h1*np.log10(A) + h2*((np.log10(A))**2)
        i = i0 + i1*np.log10(A) + i2*((np.log10(A))**2)
        M = g + h*np.log10(E0) + i*((np.log10(E0))**2)
    

        return [Sigma, Mu, M]
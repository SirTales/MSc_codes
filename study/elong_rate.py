'''
Created by de Paula, Tales Ferraz, 2022.

Contact info: ferrazdepaula@ifsc.usp.br


This code plots the elongation rate based on the alternative functions proposed by Dr. Arbeletche (2020)
https://doi.org/10.1016/j.astropartphys.2019.102389
'''


# necessary libraries and functions

import matplotlib.pyplot as plt
from ROOT import *
from paramz_func import paramEMD    # parameters for the alternative function proposed Exponentially modified Gaussian 
                                    # Distribution
from ROOT_func_1 import F2            # Exponentially Modified Gaussian Distribution            

'''
Elongation rate function.
    Inputs:
        Atomic number   #1  (A1)
        Element name    #1  (name1)
        Atomic number   #2  (A2)
        Element name    #2  (name2)
        Atomic number   #3  (A3)    -> set to 0 for only two elements     
        Element name    #3  (name3) -> set 'non' for only two elements
        Primary Energy      (E0)    -> 10 elevated to E0 (for 10^15, E0 = 15)
        % of element    #1  (comp1)
        % of element    #2  (comp2)
        % of element    #3  (comp3)

    Usage example: 
        from elong_rate import *
        
        elongrate(1, 'P',56, 'Fe', 0, 'non', 15,  50, 50, 0) 
        output in file elongrate_output_50P_50Fe.png
'''

def elongrate(A1, name1, A2, name2, A3, name3, E0, comp1, comp2, comp3):
    
    hist1 = TH1F("h1", "histo. from exp.Gaus dist.", 50, 0, 1500)
    hist2 = TH1F("h2", "histo. from exp.Gaus dist.", 50, 0, 1500)
    hist3 = TH1F("h3", "histo. from exp.Gaus dist.", 50, 0, 1500)

    inc = 0.1       # increment in energy
    energies = []   # for x-axis
    means1 = []     
    means2 = []
    means3 = []
    summeans = []

    for n in range(51):

            E = 10**(E0)        # 10 elevated to
            energies.append(E)
            

            #######First element#######
            P11, P21, P31 = paramEMD(A1, E)     # calls the alternative function parameters      
            F2.SetParameters(P11, P21, P31)     # calls the alternative function with the parameters
            
            for n in range (comp1*1000):        # loop for histogram fill (1000 to get enough data)
                    hist1.Fill(F2.GetRandom())  # fills the histogram with F2 random calls

            means1.append(hist1.GetMean())

            #######Second element#######
            P12, P22, P32 = paramEMD(A2, E)
            F2.SetParameters(P12, P22, P32)

            for n in range (comp2*1000):
                    hist2.Fill(F2.GetRandom())

            means2.append(hist2.GetMean())       

            #######Third element with condition#######
            if A3 == 0:
                    histsum = hist1 + hist2
                    summeans.append(histsum.GetMean())
                    
            else:
                    P13, P23, P33 = paramEMD(A3, E)
                    F2.SetParameters(P13, P23, P33)

                    for n in range (comp3*1000):
                           hist3.Fill(F2.GetRandom())

                    means3.append(hist3.GetMean()) 
                    histsum = hist1 + hist2 + hist3
                    summeans.append(histsum.GetMean())
                    
            hist1.Reset()  
            hist2.Reset()
            hist3.Reset()
 
            E0 += inc # increment in energy
            
    #######Fig. plot#######        
    fig =plt.figure(figsize=(8, 6), dpi=80)
    leg1 = comp1
    plt.grid()
    plt.xlabel('energy')
    plt.ylabel('Xmax[g/cm2]')
    plt.plot(energies, means1, '-r', label='100%' + name1)
    plt.plot(energies, means2, '-b', label='100%' + name2)        
    

    if A3 != 0:
            plt.plot(energies, means3, '-y', label='100%' + name3)
            plt.scatter(energies, summeans, c='g', marker = '.', label=str(comp1) +'%'+ name1 +'+' +
                        str(comp2)+'%'+ name2+ '+' +str(comp3)+'%'+name3)
    else:
        plt.scatter(energies, summeans, c='g', marker = '.', label=str(comp1) +'%'+ name1 + '+' +
                    str(comp2)+'%'+ name2)
    plt.xscale('log')
    plt.legend(loc='upper left')
    plt.show() 
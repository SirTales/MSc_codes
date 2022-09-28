'''
Created by de Paula, Tales Ferraz, 2022.

Contact info: ferrazdepaula@ifsc.usp.br


This code creates two of the three alternative functions proposed by Dr. Arbeletche (2020)
https://doi.org/10.1016/j.astropartphys.2019.102389 using ROOT
'''


from ROOT import *

########## F1 = Generalized Gumbel Distribution ##########

### Quickly decays - -exp. on -exp. ###
F1 = TF1("Gen.Gumbel",
         "(1/[1]) * ([0]**[0])/tgamma([0]) * (exp(-[0] * (((x - [2])/[1]) + exp((-(x-[2]))/[1]))))",
         450, 1000)

########## F2 = Exponentially modified Gausian ##########

### Good behavior ###

F2 = TF1('Exp.mod.Gaus', 
         '1/(2*[0])*exp(-(x-[2])/[0] + ([1]*[1])/(2*[0]*[0]))*erfc(([2]-x+([1]*[1]/[0]))/(sqrt(2)*[1]))',
         400,2000)
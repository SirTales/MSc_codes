'''
Created by de Paula, Tales Ferraz, 2022.

Contact info: ferrazdepaula@ifsc.usp.br


This code plots the Xmax distribution based on the alternative functions proposed by Dr. Arbeletche (2020)
https://doi.org/10.1016/j.astropartphys.2019.102389
'''

from IPython.display import Image
from ROOT import *
from paramz_func import paramGGD    # parameters for the alternative function  
from ROOT_func_1 import F1          # Generalized Gumbel Distribution

'''
Xmax distribution plot.
    Inputs:
        Atomic number   #1  (A1)
        Element name    #1  (name1)
        Atomic number   #2  (A2)
        Element name    #2  (name2)
        Atomic number   #3  (A3)         
        Element name    #3  (name3) 
        Atomic number   #4  (A4)         
        Element name    #4  (name4)
        Primary Energy      (E0)    -> 10 elevated to E0 (for 10^15, E0 = 15)
        % of element    #1  (comp1)
        % of element    #2  (comp2)
        % of element    #3  (comp3)
        % of element    #4  (comp4)
        output name (.png)  (out_name)

    Usage example: 
        from xmax_dist import *

        xmaxdist(1, 'p', 4, 'He', 12, 'C', 56, 'Fe', 1e18, 40, 10, 50, 0, 'xmax_dist_40p_10He_50C_0Fe')
        Image(filename='xmax_dist_40p_10He_50C_0Fe.png') 

        output file is stored in .png, since TCanvas.Draw() does not work inside a defined function
        Use Image or any other module to open the output
'''


def xmaxdist(A1, name1, A2, name2, A3, name3, A4, name4, E0, comp1, comp2, comp3, comp4, out_name):

    c1 = TCanvas('histsum')    
    
    h1 = TH1F("h1", "histogram from Gen. Gumbel dist.", 50, 450, 1000)
    h2 = TH1F("h2", "histo. from Gen. Gumbel dist.", 50, 450, 1000)
    h3 = TH1F("h3", "histo. from Gen. Gumbel dist.", 50, 450, 1000)
    h4 = TH1F("h4", "histo. from Gen. Gumbel dist.", 50, 450, 1000)
    
    legend = TLegend(0.75,0.7,0.88,0.88)
    legend.AddEntry(h1, str(comp1) +'%'+ name1, "l")
    legend.AddEntry(h2, str(comp2) +'%'+ name2, "l")
    legend.AddEntry(h3, str(comp3) +'%'+ name3, "l")
    legend.AddEntry(h4, str(comp4) +'%'+ name4, "l")
    
    ### call the paramGGD function and fills the histogram with random values from it ###

    P11, P21, P31 = paramGGD(A1, E0)
    F1.SetParameters(P11, P21, P31)

    for n in range (comp1*10000):
        h1.Fill(F1.GetRandom())
        
    P12, P22, P32 = paramGGD(A2, E0)
    F1.SetParameters(P12, P22, P32)

    for n in range (comp2*10000):
        h2.Fill(F1.GetRandom())

    P13, P23, P33 = paramGGD(A3, E0)
    F1.SetParameters(P13, P23, P33)

    for n in range (comp3*10000):
        h3.Fill(F1.GetRandom())

    P14, P24, P34 = paramGGD(A4, E0)    
    F1.SetParameters(P14, P24, P34)

    for n in range (comp4*10000):
        h4.Fill(F1.GetRandom())
        
    h1.Draw()
    h1.SetStats(0)

    legend.Draw()

    h2.Draw('same')

    h3.Draw('same')

    h4.Draw('same')

    histsum = h1 + h2 + h3 + h4

    histsum.Draw('same')

    h1.SetLineColor(2)
    h1.SetLineWidth(2)

    h2.SetLineColor(3)
    h2.SetLineWidth(2)

    h3.SetLineColor(4)
    h3.SetLineWidth(2)

    h4.SetLineColor(5)
    h4.SetLineWidth(2)

    histsum.SetLineColor(1)
    histsum.SetLineWidth(2)

    h1.GetYaxis().SetRangeUser(0,120000)
    h1.GetXaxis().SetTitle('x_{max}[gcm^{-2}]')
    h1.GetXaxis().SetTitleSize(0.035)   
    h1.GetXaxis().SetTitleFont(62)

    legend.AddEntry(histsum, "Sum", "l")


    c1.SaveAs(out_name+'.png')
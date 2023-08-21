"""
PDF plotting functions
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import rc
rc("text", usetex=True)
rc("font", **{"family":"sans-serif","sans-serif":["Helvetica"]},size="14")
rc("text.latex",preamble=r"\usepackage{sfmath}")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

''' import PDF data'''
def import_PDF(path, fn, header_length):
    r, G, Gdiff, Gcalc = np.loadtxt(path+fn, unpack=True, dtype=float, 
                                    skiprows=header_length)
    return r, G, Gdiff, Gcalc

def plot_PDF(r, G, Gdiff, Gcalc, fit_color, title, x_lim=False, y_lim=False, 
             addDiff=False):
    '''
    r (list) -- r values
    G (list) -- observed PDF
    Gdiff (list) -- difference curve
    Gcalc (list) -- calculated PDF
    fit_color (str) -- hex code for fit line color
    title (list) -- plot title info (title, x_position, y_position)
    x_lim (list, optional) -- x-axis range
    y_lim (list, optional) -- y-axis range
    addDiff (boolean, optional) -- include difference curve in plot
    '''
    plt.figure(figsize=(7,7))
    
    for i in range(len(r)):
        plt.plot(r, G, color="black", label="Observed", marker=".")
        plt.plot(r, Gcalc, color=fit_color, label="Calculated", linewidth="2")
        if addDiff == True:
            plt.plot(r, Gdiff, color="#BEBEBE", label="Difference")
            
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.xlabel("r / " r"$\AA$")
    plt.ylabel("G(r) / " r"$\AA^{-2}$")
    
    plt.text(title[1], title[2], title[0], fontsize="16", ha="left", va="top")
    
    plt.legend()
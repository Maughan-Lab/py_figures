"""
Chronopotentiometry plotting functions
"""

import eclabfiles as ecf

from colour import Color
import matplotlib.pyplot as plt

from matplotlib.pyplot import rc
rc("text", usetex=True)
rc("font", **{"family":"sans-serif","sans-serif":["Helvetica"]},size="14")
rc("text.latex",preamble=r"\usepackage{sfmath}")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' CP DATA MANAGEMENT 
Functions in this section:
    - import_biologic_CP
    - sep_CP_cycles '''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
def import_biologic_CP(path):
    '''
    Import CP data from biologic .mpr file

    Parameters
    ----------
    path : str
        File directory path

    Returns
    -------
    pos_CP : dataframe
        Full positive CP dataset
    neg_CP : dataframe
        Full positive CP dataset

    '''
    pfile = input("Positive CP data file: ")
    nfile = input("Neagtive CP data file: ")
    pfilepath = path + pfile + ".mpr"
    nfilepath = path + nfile + ".mpr"
        
    pos_CP = ecf.to_df(pfilepath)
    neg_CP = ecf.to_df(nfilepath)
        
    return pos_CP, neg_CP

#------------------------------------------------------------------------------
def sep_CP_cycles(pos_df, neg_df, cycle_pts):
    '''
    Separates CP data by cycle

    Parameters
    ----------
    pos_df : dataframe
        Full positive CP dataset
    neg_df : dataframe
        Full positive CP dataset
    cycle_pts : int
        Number of data points per EIS cycle

    Returns
    -------
    CP_cycles_pos : dict
        Dictionary of positive CP data where each cycle is a separate entry
    CP_cycles_neg : dict
        Dictionary of negative CP data where each cycle is a separate entry
    num_cycles_pos : int
        Total number of positive CP cycles 
    num_cycles_neg : int
        Total number of negative CP cycles

    '''
    num_rows_pos = len(pos_df)
    num_rows_neg = len(neg_df)
        
    num_cycles_pos = int(num_rows_pos/cycle_pts)
    num_cycles_neg = int(num_rows_neg/cycle_pts)
    
    CP_cycles_pos = {}
    CP_cycles_neg = {}
    
    for i in range(0, num_cycles_pos):
        CP_cycles_pos[i] = pos_df.truncate(before=0 + (cycle_pts*i), after=(cycle_pts-1) + (cycle_pts*i))
        
    for i in range(0, num_cycles_neg):
        CP_cycles_neg[i] = neg_df.truncate(before=0 + (cycle_pts*i), after=(cycle_pts-1) + (cycle_pts*i))
    
    print("Number of positive cycles: " + str(num_cycles_pos))
    print("Number of negative cycles: " + str(num_cycles_neg))
    
    return CP_cycles_pos, CP_cycles_neg, num_cycles_pos, num_cycles_neg

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' CP PLOTTING 
Functions in this section:
    - CP_plot
    - CP_expt_info '''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def CP_plot(pos, neg, num_cycles, x_lim=False, y_lim=False, start_hex=False, end_hex=False):
    '''
    Generate plot of CP data

    Parameters
    ----------
    pos : dict
        Dictionary of positive CP data
    neg : dict
        Dictionary of negative CP data
    num_cycles : int
        Total number of EIS cycles
    x_lim : list (float), optional
        Tuple with x-axis minimum and maximum. The default is False.
    y_lim : list (float), optional
        Tuple with y-axis minimum and maximum. The default is False.
    start_hex : str, optional
        Hex code for initial gradient color, format "#000000". The default is False.
    end_hex : str, optional
        Hex code for final gradient color, format "#000000". The default is False.

    Returns
    -------
    None

    '''
    fig, cp = plt.subplots(1, 1, figsize=(6,6))
    
    # generate color gradient
    if start_hex == False:
        start_hex = "#00C6BF"
    if end_hex == False:
        end_hex = "#B430C2"
    g = list(Color(start_hex).range_to(Color(end_hex), num_cycles))
    
    # plot CP data
    for i in range(num_cycles):
        cp.plot(pos[i]["time"], pos[i]["<Ewe>"], color = g[i].hex)
        cp.plot(neg[i]["time"], neg[i]["<Ewe>"], color = g[i].hex)
    
    # set axis limits
    if x_lim != False:
        cp.set_xlim(x_lim)
    if y_lim != False:
        cp.set_ylim(y_lim)
    
    # set axis labels
    cp.set_xlabel("Time (s)", fontsize=16)
    cp.set_ylabel(r"E$_{we}$ (V)", fontsize=16)
    
    return(cp)
 
#------------------------------------------------------------------------------
def CP_expt_info(curr_dens, num_cycles):
    '''
    Generates string with CP experiment info

    Parameters
    ----------
    curr_dens : int
        Value of current density in uA/cm^2
    num_cycles : int
        Total number of EIS cycles

    Returns
    -------
    expt_info : str
        Description of current density and total number of cycles

    '''
    
    '''
    curr_dens (int) -- value of current density in uA/cm^2
    num_cycles (int) --  number of CP cycles in dataset
    '''
    expt_info = "\n".join((r"$j=$" + str(curr_dens) + r" $\mu$A$\cdot$cm$^{-2}$", 
                           str(num_cycles) + " Cycles"))
    return expt_info
    
    
    
    
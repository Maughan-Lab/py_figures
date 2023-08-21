"""
Chronopotentiometry plotting functions
"""

from colour import Color
import matplotlib.pyplot as plt
import eclabfiles as ecf

from matplotlib.pyplot import rc
rc("text", usetex=True)
rc("font", **{"family":"sans-serif","sans-serif":["Helvetica"]},size="14")
rc("text.latex",preamble=r"\usepackage{sfmath}")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' CP DATA MANAGEMENT '''

''' import CP data '''
def import_biologic_CP(path):
    pfile = input("Positive CP data file: ")
    nfile = input("Neagtive CP data file: ")
    pfilepath = path + pfile + ".mpr"
    nfilepath = path + nfile + ".mpr"
        
    pos_CP = ecf.to_df(pfilepath)
    neg_CP = ecf.to_df(nfilepath)
        
    return pos_CP, neg_CP


'''' separate individual cycles '''
def sep_cp_cycles(pos_df, neg_df, cycle_pts):
    '''
    pos_df (dataframe) -- positive CP dataset
    neg_df (dataframe) -- negative CP dataset
    cycle_pts (int) -- number of data points per CP cycle
    
    returns list of data from separated positive and negative cycles,
    and total number of positive and negative cycles
    '''
    num_rows_pos = len(pos_df)
    num_rows_neg = len(neg_df)
        
    num_cycles_pos = int(num_rows_pos/cycle_pts)
    num_cycles_neg = int(num_rows_neg/cycle_pts)
    
    CP_cycles_pos = {}
    CP_cycles_neg = {}
    
    for i in range(0, num_cycles_pos):
        CP_cycles_pos[i] = pos_df.truncate(before=0 + (cycle_pts*i), 
                                           after=(cycle_pts-1) + (cycle_pts*i))
        
    for i in range(0, num_cycles_neg):
        CP_cycles_neg[i] = neg_df.truncate(before=0 + (cycle_pts*i), 
                                           after=(cycle_pts-1) + (cycle_pts*i))
    
    print("Number of positive cycles: " + str(num_cycles_pos))
    print("Number of negative cycles: " + str(num_cycles_neg))
    
    return CP_cycles_pos, CP_cycles_neg, num_cycles_pos, num_cycles_neg

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' CP PLOTTING '''

def gradient_gen(start_hex, end_hex, num):
    '''
    start_hex (str) -- hex code for starting gradient color
    end_hex (str) -- hex code for ending gradient color
    num (int) -- number of colors to generate
    
    returns list of hex codes, will need to use .hex() to retrieve as string
    '''
    start_color = Color(start_hex)
    end_color = Color(end_hex)
    
    colors_list = list(start_color.range_to(end_color, num))
    
    return colors_list


def CP_plot(pos, neg, num_cycles, x_lim=False, y_lim=False, start_hex=False, 
            end_hex=False, title_info=False, curr_dens=False):
    '''
    pos (dataframe) -- positive CP dataset
    neg (dataframe) -- negative CP dataset
    num_cycles (int) -- number of CP cycles in dataset
    x_lim (list, optional) -- x-axis range
    y_lim (list, optional) -- y-axis range
    start_hex (str, optional) -- hex code for starting gradient color
    end_hex (str, optional) -- hex code for ending gradient color
    title_info (list, optional) -- title text info, form: ("text", x_position, y_position)
    curr_dens (list, optional) -- current density info, form: ("text", x_position, y_position)
    '''
    fig, cp = plt.subplots(1, 1, figsize=(6,6))
    
    if start_hex == False:
        start_hex = "#00C6BF"
    if end_hex == False:
        end_hex = "#B430C2"
    g = gradient_gen(start_hex, end_hex, num_cycles)
    
    for i in range(len(num_cycles)):
        cp.plot(pos[i]["time"], pos[i]["<Ewe>"], color = g[i].hex)
        cp.plot(neg[i]["time"], neg[i]["<Ewe>"], color = g[i].hex)
        
    if x_lim != False:
        cp.set_xlim(x_lim)
    if y_lim != False:
        cp.set_ylim(y_lim)
    
    cp.set_xlabel("Time (s)", fontsize=16)
    cp.set_ylabel(r"E$_{we}$ (V)", fontsize=16)
    
    expt_info = "\n".join((r"$j=$" + str(curr_dens) + r" $\mu$A$\cdot$cm$^{-2}$", 
                           str(num_cycles) + " Cycles"))
    
    cp.text(title_info[1], title_info[2], title_info[0], ha="left", va="top", fontsize="16")
    cp.text(expt_info[1], expt_info[2], expt_info[0], ha="right", va="top", fontsize="14")
    
    
    
    
    
    
    
    
    
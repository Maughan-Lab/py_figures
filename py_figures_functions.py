"""
Functions for py_figures repo
"""

import numpy as np
from colour import Color
import matplotlib.pyplot as plt
import glob
import eclabfiles as ecf

#------------------------------------------------------------------------------
# 2THETA <--> Q CONVERSIONS

# parameters:
#    twotheta (list) -- list of 2theta values
#    q (list) -- list of Q values
#    wavelength (float) -- wavelength of instrument used to collect data

# converts from 2theta to Q, returns Q
def tt_to_q(twotheta, wavelength):
    Q = 4 * np.pi * np.sin((twotheta * np.pi)/360) / wavelength
    return Q

# converts from Q to 2theta, returns 2theta
def q_to_tt(q, wavelength):
    twotheta = 360 * np.pi * np.arcsin((q * wavelength) / (4 * np.pi))
    return twotheta

# copper source wavelength
copper_wl = 1.54

#------------------------------------------------------------------------------
# COLOR GRADIENT GENERATION

# parameters:
#    start_hex (str) -- hex code for starting gradient color
#    end_hex (str) -- hex code for ending gradient color
#    num (int) -- number of colors to generate

# returns list with hex codes of gradient colors
def gradient_gen(start_hex, end_hex, num):
    start_color = Color(start_hex)
    end_color = Color(end_hex)
    
    colors_list = list(start_color.range_to(end_color, num))
    
    return colors_list

# plots gradient, no return value
def test_grad(color_list):
    plt.figure()
    for i in range(0, len(color_list)):
        plt.bar(i, height=10, width=1, bottom=0, align="center", data=None,
                color=color_list[i].hex)

#------------------------------------------------------------------------------
# BATCH FILE DIRECTORY
# parameters:
#    path (str) -- directory path
#    filetype (str, optional) -- specify file extenstion
#    current_dir (list) -- working file directory
#    isQ (bool) -- boolean for x-axis units, set to False if in 2theta,
#    defaults to True for units of Q
#    isXYE (bool) -- boolean for file type, set to False if not .xye, defaults
#    to True for .xye
#    header_rows (int) -- number of rows in file that consist of header info

# import a file directory
def import_dir(path, filetype=None):
    if filetype is not None:
        list_files = glob.glob(path + "/" + filetype)
    else:
        list_files = glob.glob(path + "/*")
    return list_files

# create XRD variable dictionaries, returns dictionaries for Q/2theta,
# intensity, and error
def var_dicts(current_dir, header_rows, isQ=True, isXYE=True):
    x_dict = {}
    intensity_dict = {}
    err_dict = {}
    
    for i in current_dir:
        if isQ == True:
            globals()[f"Q_{i}"] = f"Q_{i}"
            x_dict[i] = "Q"+str(i)
        elif isQ == False:
            globals()[f"2theta_{i}"] = f"2theta_{i}"
            x_dict[i] = "2theta"+str(i)
        
        globals()[f"intensity_{i}"] = f"intensity_{i}"
        intensity_dict[i] = "intensity"+str(i)
        
        if isXYE == True:
            globals()[f"err_{i}"] = f"err_{i}"
            err_dict[i] = "err"+str(i)
            
    for i in range(0, len(x_dict)):
        if isXYE == True:
            x_dict[i], intensity_dict[i], err_dict[i] = \
                np.loadtxt(current_dir[i], unpack=True, dtype=float, 
                           skiprows=header_rows)
        elif isXYE == False:
            x_dict[i], intensity_dict[i] = \
                np.loadtxt(current_dir[i], unpack=True, dtype=float, 
                           skiprows=header_rows)
                
    return x_dict, intensity_dict, err_dict
#------------------------------------------------------------------------------
# REFORMAT LARGE AXIS VALUES (i.e., scale from 100,000 to 100)
# !!! DON'T FORGET TO CHANGE AXIS UNITS ON PLOT !!!

# returns formatting function
def reformat_ticks(tick_val, pos):
    if tick_val >= 1000:
        new_tick_format = round(tick_val/1000, 1)
    elif tick_val > -1000:
        new_tick_format = round(tick_val, 1)
    elif tick_val <= -1000:
        new_tick_format = round(tick_val/1000, 1)
    else:
        new_tick_format = tick_val

    new_tick_format = str(new_tick_format)
    
    index_of_decimal = new_tick_format.find(".")
    
    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal+1]
        if value_after_decimal == "0":
            # remove the 0 after the decimal point since it's not needed
            new_tick_format = \
                new_tick_format[0:index_of_decimal] + \
                new_tick_format[index_of_decimal+2:]

    return new_tick_format

#------------------------------------------------------------------------------
# ECHEM PLOTTING
# parameters:
#    df -- EIS dataframe
#    cycle_pts (int) -- number of data points per EIS cycle

# sort EIS data by time, no return value
def sort_eis(df):
    df.sort_values(by=["time"])

# separate individual cycles, returns EIS_cycles (list) and num_cycles (int)
def sep_eis_cycles(df, cycle_pts):
    num_rows = len(df)
    num_cycles = int(num_rows / cycle_pts)
    
    EIS_cycles = {}
    
    for i in range(0, num_cycles):
        EIS_cycles[i] = df.truncate(before=0 + (cycle_pts*i), 
                                    after=(cycle_pts-1) +  (cycle_pts*i) )
    
    print("Number of cycles: " + str(num_cycles))
    
    return EIS_cycles, num_cycles

def import_biologic_EIS(path):
    file = input("Data file: ")
    filepath = path + file + ".mpr"
        
    EIS_data = ecf.to_df(filepath)
        
    return EIS_data

#------------------------------------------------------------------------------
# CP PLOTTING
# parameters:
#    pos_df -- positive CP dataset
#    neg_df -- negative CP dataset
#    cycle_pts (int) -- number of data points per CP cycle


# separate individual cycles
# returns separated cycles and number of cycles for positive and negative CP
def sep_cp_cycles(pos_df, neg_df, cycle_pts):
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

def import_biologic_CP(path):
    pfile = input("Positive CP data file: ")
    nfile = input("Neagtive CP data file: ")
    pfilepath = path + pfile + ".mpr"
    nfilepath = path + nfile + ".mpr"
        
    pos_CP = ecf.to_df(pfilepath)
    neg_CP = ecf.to_df(nfilepath)
        
    return pos_CP, neg_CP

#------------------------------------------------------------------------------
# XRD PLOTTING

def import_XRD(num_imports, path, header_length, hasCalc=False):
    tt_dict = {}
    y_obs_dict = {}
    sig_dict = {}
    y_calc_dict = {}
    diff_dict = {}
    
    for i in range(0, num_imports):
        file = input("Data file " + str(i) + ": ")
        tag = input("Data Tag: ")
        filepath = path + file + ".xye"
        
        if hasCalc == False:
            tt, y_obs, sig = np.loadtxt(filepath, unpack=True, dtype=float, 
                                        skiprows=header_length)
        elif hasCalc == True:
            tt, y_obs, sig, y_calc, diff = np.loadtxt(filepath, unpack=True, 
                                                  dtype=float, 
                                                  skiprows=header_length)
        
        tt_dict[tag] = tt
        y_obs_dict[tag] = y_obs
        sig_dict[tag] = sig
        if hasCalc == True:
            y_calc_dict[tag] = y_calc
            diff_dict[tag] = diff
        
    return tt_dict, y_obs_dict, sig_dict, y_calc_dict, diff_dict

def import_hkl(num_imports, path):
    h_dict = {}
    k_dict = {}
    l_dict = {}
    tt_theor_dict = {}
    i_theor_dict = {}
    
    for i in range(0, num_imports):
        file = input("hkl file " + str(i) + ": ")
        tag = input("hkl Tag: ")
        filepath = path + file + ".txt"
        
        h, k, l, tt_theor = np.loadtxt(filepath, unpack=True,
                                       dtype=float, skiprows=1)
        
        h_dict[tag] = h
        k_dict[tag] = k
        l_dict[tag] = l
        tt_theor_dict[tag] = tt_theor
    
    return h_dict, k_dict, l_dict, tt_theor_dict

def q_dict(tt_dict, wl):
    q_dict = {}

    for i in tt_dict.keys():
        q_dict[i] = tt_to_q(tt_dict[i], wl)
        
    return q_dict

def subLabels(num):
    subLabels = []
    for i in range(0, num):
        label = input("Substitution fraction for plot " + str(i) + ": ")
        txt_label = "x = " + label
        subLabels.append(txt_label)

    return subLabels

def hkl_labels(num):
    hkl_labels = []
    
    hkl_colors = []
    blue = "#0D35FC"
    darkblue = "#310BD9"
    purple = "#8000F0"
    pink = "#C10BD9"
    hotpink = "#FA008E"
    
    for i in range(0, num):
        label = input("hkl label for set" + str(i) + ": ")
        hkl_labels.append(label)
        
        label_color = "#BEBEBE"
        color = input("Color (blue[1], darkblue[2], purple[3], \
                      pink[4], hotpink[5], or input hex # [6]): ")
        color = int(color)
        if color == 1:
            label_color = blue
        elif color == 2:
            label_color = darkblue
        elif color == 3:
            label_color = purple
        elif color == 4:
            label_color = pink
        elif color == 5:
            label_color = hotpink
        elif color == 6:
            label_color = input("Enter hex #: ")
        hkl_colors.append(label_color)
        
    return hkl_labels, hkl_colors

#------------------------------------------------------------------------------
# PDF PLOTTING

def import_PDF(num_imports, path, header_length):
    r_dict = {}
    G_dict = {}
    Gdiff_dict = {}
    Gcalc_dict = {}
    
    for i in range(0, num_imports):
        file = input("Data file " + str(i) + ": ")
        tag = input("Data Tag: ")
        filepath = path + file + ".txt"
        
        r, G, Gdiff, Gcalc = np.loadtxt(filepath, unpack=True, dtype=float, 
                                    skiprows=header_length)
        
        r_dict[tag] = r
        G_dict[tag] = G
        Gdiff_dict[tag] = Gdiff
        Gcalc_dict[tag] = Gcalc
        
    return r_dict, G_dict, Gdiff_dict, Gcalc_dict



"""
Functions for py_figures repo
"""

import numpy as np
from colour import Color
import matplotlib.pyplot as plt
import glob

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
















"""
Functions for py_figures repo
"""

import numpy as np
from colour import Color
import glob

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' 2THETA <--> Q CONVERSIONS '''


''' converts from 2theta to Q'''
def tt_to_q(twotheta, wavelength):
    '''
    twotheta (list) -- list of 2theta values
    wavelength (float) -- wavelength of instrument used to collect data
    
    returns list of Q values
    '''
    Q = 4 * np.pi * np.sin((twotheta * np.pi)/360) / wavelength
    return Q

''' converts from Q to 2theta'''
def q_to_tt(q, wavelength):
    '''
    q (list) -- list of Q values
    wavelength (float) -- wavelength of instrument used to collect data
    
    returns list of 2theta values
    '''
    twotheta = 360 * np.pi * np.arcsin((q * wavelength) / (4 * np.pi))
    return twotheta

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' COLOR GRADIENT GENERATION '''


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

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' IMPORTING DATA '''

''' import data file '''
def import_file(path, fn, header_rows):
    '''
    path (str) -- directory path
    fn (str) -- file name, including extension
    header_rows (int) -- number of metadata rows at start of file
    
    returns each column in file as a list
    '''
    return np.loadtxt(path+fn, unpack=True, dtype=float, skiprows=header_rows)

''' import .xye file '''
def import_XYE(path, fn, header_rows):
    '''
    path (str) -- directory path
    fn (str) -- file name
    header_rows (int) -- number of metadata rows at start of file
    
    returns x, y, and error lists
    '''
    f = path + fn + ".xye"
    x, y, e = np.loadtxt(f, unpack=True, dtype=float, skiprows=header_rows)
    return x, y, e

''' import .xy file '''
def import_XY(path, fn, header_rows):
    '''
    path (str) -- directory path
    fn (str) -- file name
    header_rows (int) -- number of metadata rows at start of file
    
    returns x and y lists
    '''
    f = path + fn + ".xy"
    x, y = np.loadtxt(f, unpack=True, dtype=float, skiprows=header_rows)
    return x, y

''' import an entire file directory '''
def import_dir(path, filetype=None):
    '''
    path (str) -- directory path
    filetype (str, optional) -- specify file extenstion
    
    returns list of files
    '''
    if filetype is not None:
        list_files = glob.glob(path + "/" + filetype)
    else:
        list_files = glob.glob(path + "/*")
    return list_files

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
''' GENERAL PLOTTING FUNCTIONS '''


''' format axis multiplier to reformat large axis values'''
def reformat_ticks(tick_val, pos):
    '''
    returns function to set as formatter
    
    i.e. ax.xaxis.set_major_formatter(FuncFormatter(new_tick_format))
    '''
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

''' Set axis label unit '''
def labelprefix(limit):
    '''
    limit (float) -- axis limit
    
    returns string with unit prefix
    '''
    prefix = ''
    if limit >= 1e9:
        prefix = 'G'
    elif limit >= 1e6:
        prefix = 'M'
    elif limit >= 1e3:
        prefix = 'k'
    return prefix

''' Set title for substituted Li3MCl6 compound'''
def set_subs_title(m1, m2, sub_fract):
    '''
    m1 (str) -- original metal cation
    m2 (str) -- substituting metal cation
    sub_fract (float) -- substiution fraction
    
    returns string with title
    '''
    if sub_fract == 0:
        title = r"Li$_3$" + m1 + r"Cl$_6$"
    elif sub_fract != 0:
        Li_frac = r"$_{{{L}}}$".format(L=3-sub_fract)
        M1_frac = r"$_{{{M1}}}$".format(M1=1-sub_fract)
        M2_frac = r"$_{{{M2}}}$".format(M2=sub_fract)
        
        title = "Li" + Li_frac + m1 + M1_frac + m2 + M2_frac + r"Cl$_6$"
        
    return title
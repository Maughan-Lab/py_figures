# X-ray diffraction figures

### XRD_file_directory

This notebook is for importing large amounts of data from a local directory. 
Assumes diffraction data are .xye files with Q, intensity, and error as column variables.
See snippet folder for 2theta to Q conversion.

**Inputs:** 

Path to working directory (can import multiple)

**Outputs:** 

Variable dictionaries with unique names (Q_n, signal_n, err_n) to store data from all files in one data type dictionary (i.e., Q_var_dict)

Typical plotting capabilities. Can include a difference curve. User must manually adjust text location and axis scales if needed.

**Optional:**

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")

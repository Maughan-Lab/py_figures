# X-ray diffraction figures

See snippet folder for 2theta to Q conversion.

### XRD_refinement 

This notebook is for plotting experimental and calculated X-ray diffraction.

**Input:** 

Diffraction data files. Assumes files include 2theta or Q, experimental intensity, calculated intensity, difference curve, and error as column variables.

**Output:** 

Typical plotting capabilities. Can include a difference curve. User must manually adjust text location and axis scales if needed.

**Optional:**

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")



### XRD_refinement_single_set_hkl

This notebook is for plotting experimental and calculated X-ray diffraction with a single set of (hkl) ticks included.

**Input:** 

Diffraction data files. Assumes files include 2theta or Q, experimental intensity, calculated intensity, difference curve, and error as column variables.

Table of (hkl) values. Assumes files include h, k, l, and 2theta as column variables.

**Output:** 

Typical plotting capabilities. Can include a difference curve. User must manually adjust text location and axis scales if needed.

Displays (hkl) ticks underneath the plotted data, may need to adjust scale.

**Optional:**

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")



### XRD_refinement_hkl_subplot

This notebook is for plotting experimental and calculated X-ray diffraction with a subplot to show multiple sets of (hkl) ticks.

**Input:** 

Diffraction data files. Assumes files include 2theta or Q, experimental intensity, calculated intensity, difference curve, and error as column variables.

Table of (hkl) values for each structure set. Assumes files include h, k, l, and 2theta as column variables.

**Output:** 

Typical plotting capabilities. Can include a difference curve. User must manually adjust text location and axis scales if needed.

Displays (hkl) ticks in a subplot underneath the plotted data, may need to adjust scale.

**Optional:**

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")



### XRD_file_directory

This notebook is for importing large amounts of data from a local directory. All other functionality is the same as XRD_refinement.

Assumes diffraction data are .xye files with Q, intensity, and error as column variables.

**Input:** 

Path to working directory (can import multiple)

**Output:** 

Variable dictionaries with unique names (Q_n, signal_n, err_n) to store data from all files in one data type dictionary (i.e., Q_var_dict)

Typical plotting capabilities. Can include a difference curve. User must manually adjust text location and axis scales if needed.

**Optional:**

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")

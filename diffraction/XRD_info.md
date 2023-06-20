# X-ray diffraction figures

### XRD_refinement 

This notebook is for plotting experimental and calculated X-ray diffraction.

**Input:** 

Diffraction data files.



### XRD_refinement_single_set_hkl

This notebook is for plotting experimental and calculated X-ray diffraction with a single set of (hkl) ticks included.

**Input:** 

Diffraction data files.

Table of (hkl) values. Assumes files include h, k, l, and 2theta as column variables.



### XRD_refinement_hkl_subplot

This notebook is for plotting experimental and calculated X-ray diffraction with a subplot to show multiple sets of (hkl) ticks.

**Input:** 

Diffraction data files.

Table of (hkl) values for each structure set. Assumes files include h, k, l, and 2theta as column variables.



### XRD_file_directory

This notebook is for importing large amounts of data from a local directory. All other functionality is the same as XRD_refinement.

**Input:** 

Path to working directory (can import multiple)

Reformat axis value (i.e., 250 on axis "Intensity (counts x10^3)" instead of 250,000 on axis "Intensity (counts")

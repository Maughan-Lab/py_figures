# Echem figures

### biologic_data_CP

This notebook is for importing chronopotentiometry data collected from a Biologic potentiostat.

**Input:** 

Chronopotentiometry data files, should be in the .mpr format

**Outputs:** 

Separates individual CP curves based on cycle length and stores each curve as a list entry.

Plots CP curves (time vs. E_we), can exclude specific curves if desired. User must manually adjust text location and axis scales if needed.



### biologic_data_EIS

This notebook is for importing electrochemical impedance spectroscopy data collected from a Biologic potentiostat.

**Input:** 

EIS data files, should be in the .mpr format

**Outputs:** 

Sorts datasets chronologically. 

Separates individual EIS curves based on cycle length and stores each curve as a list entry.

Plots EIS curves (Z_real vs. -Z_imag), can exclude specific curves if desired. User must manually adjust text location and axis scales if needed.

**Optional:**

Reformat axis value (i.e., 250 on axis "Z_real (kOhms)" instead of 250,000 on axis "Z_real (Ohms)"


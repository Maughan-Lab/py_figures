## General utilities

``` tt_to_q(twotheta, wavelength) ```
  - *parameters:*

    twotheta (list) -- list of 2theta values to be converted to Q
    
    wavelength (float) -- wavelength of intstrument used to collect data

  - returns list of Q values

``` q_to_tt(q, wavelength) ```
  - *parameters:*

    q (list) -- list of Q values to be converted to 2theta
    
    wavelength (float) -- wavelength of intstrument used to collect data

  - returns list of 2theta values

``` gradient_gen(start_hex, end_hex, num)  ```
  - *parameters:*
    
    start_hex (str) -- hex code for first color in gradient
    
    end_hex (str) -- hex code for last color in gradient

    num (int) -- total number of colors in gradient

  - returns list of hex codes
    
``` test_grad(color_list) ```
- *parameters:*

  color_list (list) -- gradient colors
  
- no return value, plots generated gradient

``` reformat_ticks(tick_val, pos) ```
- *parameters:
  
  tick_val (float, int) -- value(s) to be reformatted
  
- returns function for formatting ticks

## Importing file directories

``` import_dir(path, filetype=None) ```
- *parameters:*
  
  path (str) -- path to folder where files are stored
  
  filetype (str, optional) -- specific file type
  
- returns list of files in specified directory

``` var_dicts(current_dir, header_rows, isQ=True, isXYE=True) ```
- *parameters:*
  
  current_dir (str) -- file directory
  
  header_rows (int) -- number of metadata rows to skip in file
  
  isQ (bool) -- set to True if x-axis values are in units of Q, defaults to False and uses units of 2theta
  
  isXYE (bool) -- set to True if files being imported are type ".xye", defaults to False
  
- returns dictionaries for Q/2theta, intensity, and error

## XRD plotting

``` import_XYE(num_imports, path, header_length, hasCalc=False) ```
- *parameters:*
  
  num_imports (int) -- number of files to be imported
  
  path (str) -- directory where files are stored
  
  header_length (int) -- number of rows of metadata to skip in file
  
  hasCalc (bool) -- set to True if file includes calculated refinement data, defaults to False
  
- returns dictionaries of 2theta, observed intensity, sigma, calculated intensity, and difference
  (if hasCalc is False, calculated intensity and difference dictionaries are empty)
  
``` import_XY(num_imports, path, header_length) ```
- *parameters:*
  
  num_imports (int) -- number of files to be imported
  
  path (str) -- directory where files are stored
  
  header_length (int) -- number of rows of metadata to skip in file
  
- returns dictionaries of 2theta and observed intensity
  
``` import_hkl(num_imports, path) ```
- *parameters:*
  
  num_imports (int) -- number of files to be imported
  
  path (str) -- directory where files are stored
  
- returns dictionaries of h, k, l, and calculated 2theta
  
``` import_file(path, name, ftype, header_length) ```
- *parameters:*
  
  path (str) -- directory where files are stored
  
  name (str) -- specific file name
  
  ftype (str) -- file extension (i.e., ".xye")
  
  header_length (int) -- number of rows of metadata to skip in file
  
- returns file column information as lists 
  
``` q_dict(tt_dict, wl) ```
- *parameters:*
  
  tt_dict (dictionary) -- 2theta values to be converted to Q
  
  wl (float) -- wavelength of intstrument used to collect data
  
- returns dictionary of Q values
  
``` labels(num, isSubs=False) ```
- *parameters:*
  
  num (int) -- number of labels
  
  isSubs (bool) -- set to True if labels being generated are substitution fractions, defaults to False
  
- returns list of labels
  
``` hkl_labels(num) ```
- *parameters:*
  
  num (int) -- number of labels
  
- returns list of labels
  
``` set_title(m1, isSubs = False, m2="", sub_fract=0) ```
- *parameters:*
  
  m1 (str) -- 3+ metal element
  
  isSubs (bool) -- set to True if aliovalently substituted, defaults to False
  
  m2 (str, optional) -- substituted 4+ metal element
  
  sub_fract (float, optional) -- substitution fraction
  
- returns string

## E-chem plotting

``` sort_eis(df) ```
- *parameters:*
  
  df (dataframe) -- EIS data
  
- no return value

``` sep_eis_cycles(df, cycle_pts) ```
- *parameters:*
  
  df (dataframe) -- EIS data
  
  cycle_pts (int) -- number of data points per EIS cycle
  
- returns list of EIS cycles and int number of total cycles

``` import_biologic_EIS(path) ```
- *parameters:*
  
  path (str) -- directory where files are stored
  
- returns dataframe

``` sep_cp_cycles(pos_df, neg_df, cycle_pts) ```
- *parameters:*
  
  pos_df (dataframe) -- positive CP data
  
  neg_df (dataframe) -- negative CP data
  
  cycle_pts (int) -- number of data points per CP cycle
  
- returns list of EIS cycles and int number of total cycles

``` import_biologic_CP(path) ```
- *parameters:*
  
  path (str) -- directory where files are stored
  
- returns dataframes for positive and negative CP data

## PDF plotting

``` import_PDF(num_imports, path, header_length) ```
- *parameters:*
  
  num_imports (int) -- number of files to be imported
  
  path (str) -- directory where files are stored
  
  header_length (int) -- number of rows of metadata to skip in file
  
- returns dictionaries of radius, observed G(r), difference G(r), and calculated G(r)

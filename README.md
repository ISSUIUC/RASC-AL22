# RASC-AL22
Compilation of code used for RASC-AL 2022 competition

This repository includes code for multiple different functions:
  1. A Rodwell model that outputs depth, diameter, required thermal power, etc for Rodwells
  2. A data parser that sorts and plots the outputs of the Rodwell model
  3. A thermal model to calculate heat loss in pipes
  4. A costs analysis calculator
  
# 1. RODWELL MODEL:
# Instructions 
To install the repository run `git clone https://github.com/ISSUIUC/RASC-AL22.git!!!`

Note: We recommend using the C++ translation instead of the FORTRAN model, not only is it more precise but it is far less complicated to work with. Any questions can be sent to Ana Bojinov at aboji2 @ illinois.edu

## Run the Fortran Code 
1. Edit the line `OPEN(unit=9,FILE="/Users/alanwang/Desktop/input.txt")` so that the input file links to the folder you have it stored in
2. `make fortran` you should see a file called fortran.out be generated
3. `./fortran.out`
**The output is in the file `OUTPUT_MARS.DAT`**

Note: there is a shortcut to run everything above much quicker but there must be a file called `OUTPUT_MARS.DAT` in the folder. If that condition is met then 
1. `make test-fortran` should run the code 

## Run the C code 
1. `make main` you should see a file called `main.out` be created. 
2. ./main.out
**The output is in the file `output.txt`**

Note: there is also the command that combines the above 2 steps. 
1. `make test`

## Other Features 
- `make clean` standard cleaning, removes all object (*.out) files
- `make goto` compiles goto c testing code 
- `make test-goto` compiles and runs the goto c testing code 
- `make fortran-goto` compiles the fortran goto testing code 
- `make test-fortran-goto` compiles and runs the fortran goto testing code 

## File 
- `main.c` and `main.h` files needed for the rodwell C code 
- `Rodwell_Code_2.f` file needed for the fortran rodwell code 
- `goto.c` goto c code 
- `fortran_goto.f` goto fortran code 
- `Makefile` the file for compiling and testing **Do not touch this unless you know what you are doing!!!!!!**
- `input.txt` input variables for the fortran code 
- `output.txt` output for the c rodwell code 
- `OUTPUT_MARS.DAT` output for the fortran rodwell code 

# Explanation of the C code for rodwell 

## Goto's between C and fortran 
You can run the instructions yourself to see the behavior but the gist of it is that they are basically the same. The only difference is not signifcant to the behavior. 
TL;DR is jumping (via goto) out and back into a for loop in fortran and C is identical for the rodwell code's case.  

The C code produces **identical** but more **precise** outputs to the rodwell code. The way the C code is organized is that it is split between 2 files and outputs are sent to `output.txt`

#### `main.c` 
It's just a direct conversion from the fortran code, Professor Lembeck had various difference's that cause the intial NaN's values observed that has been fixed. There were also various random things that didn't do anything that were removed.  

The code was also changed so that it used as little goto's as possible. There are only a couple goto's left that couldn't be changed without making the code more unreadible. Unfortunately, the goto statement that goes out of the loop and back into the loop is still there since there wasn't a accurate way of removing it. A lot of the code was cluttering it so it was moved to the header file. But the code is accurate and more readible now. 

**Note:** None of the issues with the wrong gal/day values were fixed because it appears that is an issue with the math. Regarding the weird day increment that might also be a planned feature of the code it is still unclear so that was not changed. 

#### `main.h` 
This file was added, but it contains macros for the year dispatch in the c code. That was the code that handles different time (N values) and changes variables accordingly. That was changed to a macro in the header file (N1, N2, N3, N4, N5).
  
There was a repetive output code that was changed into a function `print_initial_parameter`.  

The includes were also moved to this file. They are linked together by the Makefile. 

# 2. Rodwell Plotter
Plotting outputs from the C code:
* If you have anaconda open up the python notebook in `dataParser/output_parser_c.ipynb` 

Plotting outputs from FORTRAN code:
* Or in terminal run `python dataParser/table_reader.py` to read the table data and `python dataParser/non_table_reader.py` for non table data

# 3. Thermal Model
If you have anaconda open up the python notebook in ...

# 4. Cost Analysis Calculator
If you have anaconda open up the python notebook in ...

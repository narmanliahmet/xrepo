# Optimization of Operation Line with Ortools solver

## Coding Language
- Python-3.7

## Dependency Libraries
- numpy (pip install numpy)
- matplotlib (pip install matplotlib)
- pandas (pip install pandas)
- xlrd version(1.2.0) (pip install xlrd==1.2.0)
- ortools (pip install ortools)

## Usage of the script
- Run the script from the terminal as (note that data.xlsx should be on the path)
-- python mip_opt.py
- Get the bar plot and additional information for solver as terminal output (The plot output of the script is added as output.jpeg to examine)
- For each bar from top to below Relevant colors of the operations are at the right hand lengend
- Colors are repeating because of large amount of operations follow the sequence from top to bottom
- Each bar is for each personnel
- Y axis is the time indicator

## Features
- A succesfull MIP solver on ortools
- Creating fast and neat condtitions on problem
- Usage of excel file to import all data
- Neat parse of all data to use on model

## Analysis
- Optimal output for production of 734 is reached within the limit of [600,800]
- Output desire is low to fill all gaps for all personnel so some of them need to work lesser
- The distrubiton of skills among the personnel is not homogeneous so some personnel with large variety of skills are assigned with more job
- So the solver could not find a linear line of equal time sequences.
- Either output desire should be higher or work time desire should be lower or skill variety of personnel homogenized to get better results.
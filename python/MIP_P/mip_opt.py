import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp
from itertools import compress
import matplotlib.pyplot as plt

# Reading data frames from excel file
dfo = pd.read_excel('data.xlsx', sheet_name='Operasyonlar')
dfp = pd.read_excel('data.xlsx', sheet_name='Personeller')
# Replacing nan values
dfp = dfp.fillna(0)
# Selecting Ability of work of personnel
pbl = dfp.iloc[1:, 2:8]
# Filling E type full ability for all personnel
pbl.iloc[:, 3] = 3
# Selecting given names of the personnel
pnm = dfp.iloc[1:, 1]
# Selecting operation names
onm = dfo.iloc[1:, 1]
# Selecting Operation Cycle Times
cyc = dfo.iloc[1:, 6]
# Selecting operation requirement codes
opr = dfo.iloc[1:, 7]

# Converting all data frames to numpy arrays
pbl = pbl.to_numpy()
pnm = pnm.to_numpy()
onm = onm.to_numpy()
cyc = cyc.to_numpy()
opr = opr.to_numpy()
# Processing operation names
for i in range(len(onm)):
    if len(onm[i]) == 3:
        onm[i] = onm[i] + "x"
for i in range(len(pnm)):
    if len(pnm[i]) == 2:
        pnm[i] = pnm[i] + "x"

# Defining unit times for all cycle times
cyc = cyc / 734
# Defining an array for template ability codes
acod = ["O", "D", "R", "E", "Ü", "K", "P"]
# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')
# Defining infinity for solver
inf = solver.infinity()
# Defining the work load variables as integer variables for all load into an array
wvars = []
# Defining an array for variable names to access
wvarnm = []
# Defining maximize for work time
maxim = []

for i in range(len(pnm)):
    for j in range(6):
        for k in range(len(opr)):
            if (acod[j] == opr[k][0]) & (pbl[i, j] >= int(opr[k][1])):
                wvars.append(solver.IntVar(0.0, inf, (pnm[i] + onm[k])))
                wvarnm.append(pnm[i] + onm[k])
                maxim.append(wvars[-1] * cyc[k])

# Defining first constraint as all operation types must be in total 734
# Indexing variable position as boolean
sumo = np.empty((len(wvars), len(onm)), dtype=bool)
for i in range(len(wvars)):
    for j in range(len(onm)):
        if onm[j] == wvarnm[i][-4:]:
            sumo[i, j] = True
        else:
            sumo[i, j] = False

# Adding constraints to solver
for i in range(len(onm)):
    solver.Add(sum(compress(wvars, sumo[:, i])) <= 800)
    solver.Add(sum(compress(wvars, sumo[:, i])) >= 600)

# Indexing variable position as boolean
sump = np.empty((len(wvars), len(pnm)), dtype=bool)
for i in range(len(wvars)):
    for j in range(len(pnm)):
        for k in range(len(onm)):
            if pnm[j] == wvarnm[i][:3]:
                sump[i, j] = True
            else:
                sump[i, j] = False
# Defining constraints for maximum time for all operations
wvarc = []
for i in range(len(wvars)):
    for j in range(len(onm)):
        if onm[j] == wvarnm[i][-4:]:
            wvarc.append(cyc[j])


for i in range(len(pnm)):
    solver.Add(sum(np.multiply(list(compress(wvars, sump[:, i])), list(compress(wvarc, sump[:, i])))) >= 0.7)
    solver.Add(sum(np.multiply(list(compress(wvars, sump[:, i])), list(compress(wvarc, sump[:, i])))) <= 0.9)

# Defining a normalizer constraint for non zero work load
for i in range(len(wvars)):
    solver.Add(wvars[i] >= 6)
# Adding Maximizing aim for work time
solver.Maximize(sum(maxim))
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Optimal Solution found.')
else:
    print('The problem does not have an optimal solution.')
print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

# Defining work loads of all personnel for bar chart with time output
ind = np.arange(len(pnm))
width = 0.35
bars = np.zeros((len(onm), len(pnm)))
for i in range(len(wvars)):
    for j in range(len(onm)):
        for k in range(len(pnm)):
            if onm[j] == wvarnm[i][-4:]:
                if pnm[k] == wvarnm[i][:3]:
                    bars[j, k] = wvars[i].solution_value() * cyc[j]
plt.figure()
plt.title("Distribution of Operation Loads to Personnel")
leg = []
leg.append(plt.bar(ind, bars[0, :], width))
for i in range(1, len(onm)):
    leg.append(plt.bar(ind, bars[i, :], width, bottom=bars[i - 1, :]))
plt.ylabel("Time")
plt.xticks(ind, pnm, fontsize=7)
plt.legend(leg, onm, fontsize=5)
plt.show()

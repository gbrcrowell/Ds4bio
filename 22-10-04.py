import numpy as np
import pandas as pd
states = pd.read_csv("state_health.csv")
states.set_index('State Name', inplace=True)
min_poverty = states['Poverty'].min()
max_poverty = states['Poverty'].max()
bins = np.linspace(min_poverty, max_poverty, 10)
d = {
    'bin number': [],
    'lower bound': [],
    'upper bound': [],
    'number of states': []
}  # Setup


for i, b in enumerate(bins):  # a for loop that returns the bin number we are in (i) and its value (b)
    if i < len(bins)-1:  # this limits our i to 0-8 (which is required, so we don't 'overshoot' the highest bin)
        upper_edge = bins[i+1]
        lower_edge = b
        d['bin number'].append(i + 1)
        d['lower bound'].append(round(lower_edge, 1))
        d['upper bound'].append(round(upper_edge, 1))
        d['number of states'].append(len(states.loc[(states['Poverty'] > lower_edge) & (states['Poverty'] < upper_edge), 'Poverty']))


d = pd.DataFrame(d)
d = d.set_index('bin number')


print(d)

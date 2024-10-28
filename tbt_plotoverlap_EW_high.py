import glob
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filenames = glob.glob('BKG*.csv')
bkg = np.zeros((len(filenames),6))
i=0
for filename in filenames:
    num = [int(s) for s in re.findall(r'\d+', filename)]
    # ydata from csv file
    df = pd.read_csv(filename, header = None, skiprows = 0, sep = ',', engine = 'python', on_bad_lines='skip')
    flag = df[0]
    time = df[2]
    p1_low = df[3]
    p1_high = df[4]
    p2_low = df[6]
    p2_high = df[7]
    p1_sum = p1_low + p1_high
    p2_sum = p2_low + p2_high
    ew1_low = (p1_low / p1_sum) * 100
    ew1_high = (p1_high / p1_sum) * 100
    ew2_low = (p2_low / p2_sum) * 100
    ew2_high = (p2_high / p2_sum) * 100
    bkg[i,0] = sum(p1_sum)/len(p1_sum)
    bkg[i,1] = sum(p2_sum)/len(p2_sum)
    bkg[i,2] = sum(ew1_low)/len(ew1_low)
    bkg[i,3] = sum(ew1_high)/len(ew1_high)
    bkg[i,4] = sum(ew2_low)/len(ew2_low)
    bkg[i,5] = sum(ew2_high)/len(ew2_high)
    plt.axhline(y=bkg[i,3], color='r', linestyle='-', alpha=0.3)
    i+=1





filenames = glob.glob('SOURCE*.csv')
source = np.zeros((len(filenames),6))
k=0
for filename in filenames:
    num = [int(s) for s in re.findall(r'\d+', filename)]
    # ydata from csv file
    df = pd.read_csv(filename, header = None, skiprows = 0, sep = ',', engine = 'python', on_bad_lines='skip')
    flag = df[0]
    time = df[2]
    if (num[2] % 2) == 0:
        time = df[2].values[::-1] - 10 # reverse the column for 'returning' plates
    p1_low = df[3]
    p1_high = df[4]
    p2_low = df[6]
    p2_high = df[7]
    p1_sum = p1_low + p1_high
    p2_sum = p2_low + p2_high
    ew1_low = (p1_low / p1_sum) * 100
    ew1_high = (p1_high / p1_sum) * 100
    ew2_low = (p2_low / p2_sum) * 100
    ew2_high = (p2_high / p2_sum) * 100
    source[k,0] = max(p1_sum)
    source[k,1] = max(p2_sum)
    source[k,2] = min(ew1_low)
    source[k,3] = max(ew1_high)
    source[k,4] = min(ew2_low)
    source[k,5] = max(ew2_high)
    k+=1
    plt.plot(time, ew1_high, '.', color='black', lw=5, alpha=0.3, label=filename)
    # plt.plot(time, p2_sum, 's', color='black', lw=5, alpha=0.5, label=filename)




bkg = pd.DataFrame(bkg)
savefilename = 'RESULT_BKG.csv'
bkg.to_csv(savefilename, sep = ',', index = False, header = False)

source = pd.DataFrame(source)
savefilename = 'RESULT_SOURCE.csv'
source.to_csv(savefilename, sep = ',', index = False, header = False)


## PLOT SETTINGS 
plt.xlabel('Time (a.u.)')
plt.ylabel('Percent (%)')
plt.xlim([0,80])
plt.ylim([20,50])
# plt.legend()
plt.grid(True, which='major', linestyle='--')
plt.grid(True, which = 'minor', linestyle=':')
plt.tick_params(which='major', direction='in')
plt.tick_params(which='minor', direction='in')
plt.minorticks_on()
title_font = {
    'fontsize': 15,
    'fontweight': 'bold'
    }
plt.title('Co-60 (EW_High, P1, 5km/h)', fontdict=title_font, loc='center', pad=15)
# plt.plot(xnew, ynew_mean, 'r--', linewidth=3)
plt.show()


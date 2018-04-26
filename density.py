import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
rc('font',family='Times New Roman')
#https://matplotlib.org/users/usetex.html
Z=38
rc('text', usetex=True)
rcParams.update({'font.size': Z})

tails=np.genfromtxt("../POPC3-17_PRO1_dens_tails.xvg", skip_header=23)
heads=np.genfromtxt("../POPC3-17_PRO1_dens_heads.xvg", skip_header=23)
sol=np.genfromtxt("../POPC3-17_PRO1_dens_sol.xvg", skip_header=23)
tails[:,0] = tails[:,0] - np.max(tails[:,0])/2
heads[:,0] = heads[:,0] - np.max(heads[:,0])/2
sol[:,0] = sol[:,0] - np.max(sol[:,0])/2
fig=plt.figure(figsize=(5,8))
plt.plot(tails[:,1], tails[:,0], lw=5, color='gray', label="Tails")
plt.plot(heads[:,1], heads[:,0], lw=5, color='orange', label="Heads")
plt.plot(sol[:,1], sol[:,0], lw=5, color='c', label="Water")
lgd = plt.legend(framealpha=0.5, bbox_to_anchor=(-0.2, 1.05), fontsize=Z)
plt.ylim((-4,4))
plt.xlim((0,1200))
plt.xticks([0, 500, 1000])
#plt.grid()
plt.gca().invert_xaxis()
plt.savefig("POPC3-17_density.png", format="png", dpi=300, bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.close()

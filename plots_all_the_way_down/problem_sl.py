import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({
    "savefig.facecolor": "w",
    "figure.facecolor" : 'w',
    "figure.figsize" : (10,8),
    "text.color": "k",
    "legend.fontsize" : 20,
    "font.size" : 30,
    "axes.edgecolor": "k",
    "axes.labelcolor": "k",
    "axes.linewidth": 3,
    "xtick.color": "k",
    "ytick.color": "k",
    "xtick.labelsize" : 25,
    "ytick.labelsize" : 25,
    "ytick.major.size" : 12,
    "xtick.major.size" : 12,
    "ytick.major.width" : 2,
    "xtick.major.width" : 2,
    "font.family": "STIXGeneral",
    "mathtext.fontset" : "cm"
})



spec = pd.read_csv('example_spec_SED.csv')
phot = pd.read_csv('example_phot_SED.csv')


spec_wav = spec['wavelength'] #angstrom
spec_sed = spec['flux_spec'] #jansky

phot_wav = phot['filter_lambda']
phot_sed = phot['flux_mag']

plt.title('Galaxy SED')
plt.loglog(spec_wav, spec_sed, color='black', alpha=0.8, label='Spectrum')
plt.scatter(phot_wav, phot_sed, color='mediumaquamarine', s=200, label='Photometry')
plt.ylim([1e8, 1e14])
plt.xlim([1e3, 1e7])
plt.ylabel('Flux [Jy]')
plt.xlabel('Wavelength [$\AA$]')
plt.legend()

plt.show()

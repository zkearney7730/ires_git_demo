import pandas as pd
import matplotlib.pyplot as plt


spec = pd.read_csv('example_spec_SED.csv')
phot = pd.read_csv('example_phot_SED.csv')


spec_wav = spec['wavelength'] #angstrom
spec_sed = spec['flux_spec'] #jansky

phot_wav = phot['filter_lambda']
phot_sed = phot['flux_mag']

fig, ax = plt.subplots(1,1,dpi=300)
ax.set_title('Fixed!')
ax.plot(spec_wav, spec_sed, color='k', linewidth=1, label='SED')
ax.scatter(phot_wav, phot_sed, color='r', label='Photometry')
ax.set_ylabel(r'Flux [Jy]')
ax.set_xlabel(r'Wavelength [$\mu$m]')
ax.loglog()
ax.set_xlim(8e1, 2e7)
ax.set_ylim(1e4, 1e14)
ax.grid(alpha=0.1, zorder=-1000)
ax.legend(frameon=False)
plt.show()

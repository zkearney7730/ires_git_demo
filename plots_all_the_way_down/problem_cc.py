import pandas as pd
import matplotlib.pyplot as plt


spec = pd.read_csv('example_spec_SED.csv')
phot = pd.read_csv('example_phot_SED.csv')


spec_wav = spec['wavelength'] #angstrom
spec_sed = spec['flux_spec'] #jansky

phot_wav = phot['filter_lambda']
phot_sed = phot['flux_mag']

plt.title('Example SED')
plt.loglog(spec_wav, spec_sed, color = 'purple')
plt.scatter(phot_wav, phot_sed, marker='*', color='purple')
plt.xlabel('Wavelength')
plt.ylabel('Flux')
plt.ylim(1e2, 1e15)
plt.xlim(5e1, 2e7)
plt.show()

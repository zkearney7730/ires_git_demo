import pandas as pd
import matplotlib.pyplot as plt


spec = pd.read_csv('example_spec_SED.csv')
phot = pd.read_csv('example_phot_SED.csv')


spec_wav = spec['wavelength'] #angstrom
spec_sed = spec['flux_spec'] #jansky

phot_wav = phot['filter_lambda']
phot_sed = phot['flux_mag']

plt.title('Fix me, pleaase!')
plt.loglog(spec_wav, spec_sed)
plt.scatter(phot_wav, phot_sed)
plt.show()

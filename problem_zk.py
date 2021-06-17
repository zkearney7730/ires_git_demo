import pandas as pd
import matplotlib.pyplot as plt 

fig =plt.figure()
spec = pd.read_csv('example_spec_SED.csv')
phot = pd.read_csv('example_phot_SED.csv')


spec_wav = spec['wavelength'] #angstrom
spec_sed = spec['flux_spec'] #jansky

phot_wav = phot['filter_lambda']
phot_sed = phot['flux_mag']

plt.title('SED')
plt.loglog(spec_wav, spec_sed,c='k', label ='Spectroscopic data')
plt.scatter(phot_wav, phot_sed,marker='*',color='r',label='Photometric data')
plt.xlabel('Wavlength [$\AA$]')
plt.ylabel('Flux [Jy]')
plt.legend()
plt.show()
fig.savefig('pretty_sed.png',dpi=300)

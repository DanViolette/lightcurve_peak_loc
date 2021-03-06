from setuptools import setup

setup(name='lightcurve_peak_loc',
      version='0.1',
      description='Determine amplitude and location of aperiodic peaks in lightcurve data',
      url='https://github.com/DanViolette/lightcurve_peak_loc',
      author='Daniel Violette',
      author_email='danielviolette@cfa.harvard.edu',
      license='GNU GPL 3.0',
      packages=['lightcurve_peak_loc'],
      install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
          'pandas',
          'corner',
          'emcee',
          'astropy',
          'datetime',
          'statsmodels',
          'seaborn',
      ],
      test_suite='nose.collector',
      zip_safe = False)

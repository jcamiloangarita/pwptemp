from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pwptemp',
    packages=['pwptemp'],
    version='0.0.8',
    license='LGPL v3',
    description='Well Temperature Distribution',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Pro Well Plan AS',
    author_email='juan@prowellplan.com',
    url='https://github.com/pro-well-plan/pwptemp',
    download_url='https://github.com/pro-well-plan/pwptemp/archive/v0.0.8.tar.gz',
    keywords='well temperature distribution',
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                 'Natural Language :: English',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities'],
    install_requires=['numpy', 'matplotlib']
)

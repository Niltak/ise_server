import setuptools


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ise_server',
    version='0.1',
    author='Katlin Sampson',
    author_email='kvsampso@purdue.edu',
    description='Python wraper for ISE Servers web API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.itap.purdue.edu/ITIS-Networking/ise_server',
    project_urls={
        'Bug Tracker': 'https://github.itap.purdue.edu/ITIS-Networking/ise_server/issues',
    },
    license="LICENSE.md",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=['pyise-ers>=0.2.0.1', ''],
)
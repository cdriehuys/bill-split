from distutils.core import setup


setup(
    name='bill-split',
    version='0.0.0',
    packages=['bill_split'],
    url='https://github.com/cdriehuys/bill-split',
    license='MIT',
    author='Chathan Driehuys',
    author_email='chathan@driehuys.com',
    description='CLI to split monthly bills.',
    entry_points={
        'console_scripts': ['bill-split=bill_split.cli:main']
    },
    install_requires=['pyyaml']
)

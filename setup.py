from setuptools import setup

setup(
    name='PowerPanelServer',
    version='1.0.0',
    packages=['powerpanel'],
    url='https://david.cheeseman.club',
    license='MIT License',
    author='David Cheeseman',
    author_email='david@cheeseman.club',
    install_requires=['flask', 'requests', 'pyyaml', 'Sphinx'],
    description='A simple python tool for testing home outlets to map them to breakers.'
)

from setuptools import setup

setup(name='skopelib',
    version='0.1.0',
    packages=['skopelib'],
    install_requires=[
        'elasticsearch',
        'pyclowder==2.0.0',
        'enum',
        'PyYAML',
        'requests',
    ],

    dependency_links=['https://github.com/openskope/pyclowder2/tarball/master#egg=pyclowder-2.0.0'],

)

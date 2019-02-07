import setuptools
version = '1.9.4'

setuptools.setup(
    name='electronX',
    version=version,
    scripts=['electrumx_server', 'electrumx_rpc', 'electrumx_compact_history'],
    python_requires='>=3.6',
    # via environment variables, in which case I've tested with 15.0.4
    # "x11_hash" package (1.4) is required to sync DASH network.
    # "x13_hash" package is required to sync BitcoinPlus network.
    # "tribus_hash" package is required to sync Denarius network.
    # "blake256" package is required to sync Decred network.
    # "xevan_hash" package is required to sync Xuez network.
    # "groestlcoin_hash" package is required to sync Groestlcoin network.
    # "pycryptodomex" package is required to sync SmartCash network.
    install_requires=['aiorpcX>=0.10.3,<0.11', 'attrs',
                      'plyvel', 'pylru', 'aiohttp >= 2'],
    packages=setuptools.find_packages(include=('electrumx*',)),
    description='ElectronX Server',
    author='Neil Booth',
    author_email='kyuupichan@gmail.com',
    license='MIT Licence',
    url='https://github.com/Electron-Cash/electrumx',
    long_description='Server implementation for the Electrum protocol - AOR Version',
    download_url=('https://github.com/Electron-Cash/electrumX/archive/'
                  f'{version}.tar.gz'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        'Topic :: Internet',
    ],
)

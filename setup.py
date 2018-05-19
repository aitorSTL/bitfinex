from setuptools import setup

VERSION = '0.3.0'

# Runtime dependencies. See requirements.txt for development dependencies.
DEPENDENCIES = [
    'requests',
    'httpretty',
    "twisted",
    "autobahn",
    "pyopenssl",
    "service_identity",
]

setup(
    name='bitfinex',
    VERSION=VERSION,
    description='Python client for the Bitfinex API',
    author='Ole Henrik Skogstrøm',
    author_email='henrik@amplify.no',
    url='https://github.com/ohenrik/bitfinex',
    license='MIT',
    packages=['bitfinex'],
    install_requires=DEPENDENCIES,
    # download_url='https://github.com/ohenrik/bitfinex/tarball/%s' % version,
    keywords=['bitcoin', 'btc'],
    classifiers=[],
    zip_safe=True
)

from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Console Coloring Utility Package'
LONG_DESCRIPTION = 'A Console Coloring Utility Package'

setup(
    name="c0l0rful_console",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Blackstrat67",
    author_email="redstrat9988@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)

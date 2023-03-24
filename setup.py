import os
import re

from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements():
    return [line for line in read('requirements.txt').splitlines() if not line.startswith('#')]


def get_long_description():
    """Transform README.md into a usable long description.
    Replaces relative references to svg images to absolute https references.
    """

    with open('README.md') as fin:
        read_me = fin.read()

    def replace_relative_with_absolute(match):
        svg_path = match.group(0)[1:-1]
        return '(https://github.com/google/pybadges/raw/master/{}?sanitize=true)'.format(svg_path)

    # return re.sub(r'\(tests/golden-images/.*?\.svg\)',
    #               replace_relative_with_absolute, read_me)
    return read_me


setup(
    name='MISTIC',                                              # name of the package
    version='0.1.0',                                            # version of this release
    url='https://github.com/kchennen/MISTIC',                   # home page for the package
    download_url='https://github.com/kchennen/MISTIC.git',      # location where the release version may be downloaded
    author='kchennen',                                          # package author’s name
    author_email='kchennen@unistra.fr',                         # email address of the package author
    description='Missense Deleteriousness predictor',
    long_description=long_description,                          # longer description package to build PyPi project page
    long_description_content_type='text/markdown',
    license='MIT',                                              # license for the package
    keywords=(                                                  # list of keywords describing the package
        "Missense, predictor"
    ),
    install_requires=requirements(),                            # install external packages as dependencies
    packages=['mistic'],                                        # same as name
    scripts=['bin/mistic'],                                     # Runner files to be started from the command line
    entry_points={                                              # Register the main() function of the package
        'console_scripts': ['mistic=mistic.__main__:main'],
    },
    classifiers=[                                               # list of classifiers to categorize each release
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Flake8',
        'Framework :: Flask',
        'Framework :: Jupyter',
        'Framework :: Matplotlib',
        'Framework :: Pytest',
        'Framework :: Setuptools Plugin',
        'Framework :: tox',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)

#!/bin/sh

set -e

/Users/itcp/.miniconda3/envs/soctools/bin/python setup.py sdist bdist_wheel
/Users/itcp/.miniconda3/envs/soctools/bin/twine upload --repository-url https://upload.pypi.org/legacy/ dist/* -u itmeng -p Yan@0422
rm -rf build dist socpoctools.egg-info soctools.egg-info

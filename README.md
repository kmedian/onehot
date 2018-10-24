[![Build Status](https://travis-ci.org/kmedian/onehot.svg?branch=master)](https://travis-ci.org/kmedian/onehot)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/onehot/master?urlpath=lab)

# onehot.OneHotDummy
One-Hot encoder with sklearn-ish API interface that process mixed string and numeric labels directly.

[onehot.OneHotDummy](onehot/onehotdummy_class.py) does basically the same as [LabelEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) and [OneHotEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) combined. It is also inspired by [pandas.get_dummies](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html) and in particular its ease of use. 



## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `onehot` [git repo](http://github.com/kmedian/onehot) is available as [PyPi package](https://pypi.org/project/onehot)

```
pip install onehot
```


## Usage
Check the [examples](examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
<!-- * Run Unit Tests: `python -W ignore -m unittest discover` -->
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi: `python setup.py sdist upload -r pypi`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Debugging
* Notebooks to profile python code are in the [profile](profile) folder


## Support
Please [open an issue](https://github.com/kmedian/onehot/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/onehot/compare/).

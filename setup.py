from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='onehot',
      version='0.1.1',
      description=(
          "One-Hot encoder with sklearn-ish API interface that process "
          "mixed string and numeric labels directly."),
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/onehot',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['onehot'],
      install_requires=[
          'setuptools>=40.0.0',
          'nose>=1.3.7',
          'scipy>=1.1.0',
          'pandas>=0.23.3',
          'scikit-learn>=0.19.2',
          'numpy>=1.14.5',
          'grouplabelencode>=0.1.0'],
      python_requires='>=3.6',
      zip_safe=False)

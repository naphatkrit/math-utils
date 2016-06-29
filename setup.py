from setuptools import setup, find_packages

import math_utils


tests_require = [
]

install_requires = [
    'enum34>=1.1.6,<2'
]

setup(
    name='math-utils',
    version=math_utils.__version__,
    author='Naphat Sanguansin',
    author_email='naphat.krit@gmail.com',
    description='A simple math utility',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={'tests': tests_require},
    tests_require=tests_require,
    url='https://github.com/naphatkrit/math-utils',
)

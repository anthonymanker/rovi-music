import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='python-rovi-music',
    description='Python Wrapper for Rovi Music API',
    license='MIT License',
    version='0.1',
    zip_safe=False,
    platforms='any',
    packages=['rovi'],
    install_requires=[
        'requests>=0.13.3',
    ],

    author='Anthony Manker',
    author_email='anthonymanker@gmail.com',
    url='https://github.com/anthonymanker/rovi-music',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ),
)

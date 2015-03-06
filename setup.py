import os
import sys

from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
VERSION = '1.0.1'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    print "You should also consider tagging a release:"
    print "  git tag -a %s -m 'version %s'" % (VERSION, VERSION)
    print "  git push --tags"
    sys.exit()


setup(
    name='unicode_mayo',
    version=VERSION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    long_description=README,
    description='The mayo on your unicode sandwich',
    url='https://github.com/eyalr/unicode_mayo',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=True,
)

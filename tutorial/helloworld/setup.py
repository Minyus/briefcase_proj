#/usr/bin/env python
# import io
# import re
#
# from setuptools import setup, find_packages
#
# # with io.open('./helloworld/__init__.py', encoding='utf8') as version_file:
# #     version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
# #     if version_match:
# #         version = version_match.group(1)
# #     else:
# #         raise RuntimeError("Unable to find version string.")
# version = r'0.3.0.dev14'
#
# with io.open('README.rst', encoding='utf8') as readme:
#     long_description = readme.read()
#
#
# setup(
#     name='helloworld',
#     version=version,
#     description='A demonstration of the capabilities of the Toga widget toolkit.',
#     long_description=long_description,
#     author='Russell Keith-Magee',
#     author_email='russell@keith-magee.com',
#     url='http://beeware.org/helloworld',
#     include_package_data=True,
#     packages=find_packages(),
#     python_requires='>=3.5',
#     package_data={
#         'helloworld': ['icons/*.icns', 'icons/*.png'],
#     },
#     install_requires=[
#         'toga==%s' % version
#     ],
#     entry_points={
#         'console_scripts': [
#             'helloworld = helloworld.__main__:run',
#         ]
#     },
#     license='New BSD',
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: BSD License',
#         'Operating System :: OS Independent',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3 :: Only',
#         'Topic :: Software Development',
#         'Topic :: Utilities',
#     ],
#     options={
#         'app': {
#             'formal_name': 'helloworld',
#             'bundle': 'org.beeware',
#         },
#         'ios': {
#             'app_requires': [
#                 'toga-ios==%s' % version,
#             ]
#         },
#         'django': {
#             'app_requires': [
#                 'toga-django==%s' % version,
#             ]
#         },
#         'macos': {
#             'app_requires': [
#                 'toga-cocoa==%s' % version,
#             ]
#         },
#         'linux': {
#             'app_requires': [
#                 'toga-gtk==%s' % version,
#             ]
#         },
#         'windows': {
#             'app_requires': [
#                 'toga-winform==%s' % version,
#             ]
#         },
#         'android': {
#             'app_requires': [
#                 'toga-android==%s' % version,
#             ]
#         }
#     }
# )


#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./helloworld/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='helloworld',
    version=version,
    description='An app that does lots of stuff',
    long_description=long_description,
    author='Minyus',
    author_email='me@Minyus.github.com',
    license='MIT license',
    packages=find_packages(
        # exclude=[
        #     'docs', 'tests',
        #     'windows', 'macOS', 'linux',
        #     'iOS', 'android',
        #     'django'
        # ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Hello World',
            'bundle': 'com.example'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
                'toga-cocoa==0.3.0.dev11',
            ]
        },
        'linux': {
            'app_requires': [
                'toga==0.3.0.dev14',  # 'toga==0.3.0.dev14',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winforms==0.3.0.dev11',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
                'toga-ios==0.3.0.dev11',
            ]
        },
        'android': {
            'app_requires': [
                'toga-android==0.3.0.dev11',
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
                'toga-django==0.3.0.dev11',
            ]
        },
    }
)

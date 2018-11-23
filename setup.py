"""
Directory Forms API client
"""
import ast
import re
from setuptools import setup, find_packages


def get_version():
    pattern = re.compile(r'__version__\s+=\s+(.*)')

    with open('directory_forms_api_client/version.py', 'rb') as src:
        return str(ast.literal_eval(
            pattern.search(src.read().decode('utf-8')).group(1)
        ))


setup(
    name='directory_forms_api_client',
    version=get_version(),
    url='https://github.com/uktrade/directory-forms-api-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Directory forms .',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'directory_client_core>=4.0.2,<5.0.0',
    ],
    extras_require={
        'test': [
            'django>=1.9,<2.0a1',
            'requests>=2.18.4,<3.0.0',
            'pytest==3.10.0',
            'pytest-cov==2.3.1',
            'flake8==3.0.4',
            'requests_mock==1.1.0',
            'codecov==2.0.9',
            'pytest-django==3.1.0',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

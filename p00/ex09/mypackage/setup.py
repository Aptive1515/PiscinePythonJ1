from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    description='A simple example package',
    author='tdelauna42',
    author_email='tdelauna@42.com',
    url='https://example.com/ft_package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

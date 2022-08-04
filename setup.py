import setuptools

setuptools.setup(
    name='bbc-feeds',
    version='2.1',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='A python package to get news, weather, and sports from BBC',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/bbc-feeds',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'feedparser',
        'click'
    ],
    scripts=['./bbc'],
    python_requires='>=3.6'
)
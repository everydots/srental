from setuptools import setup, find_packages

setup(
    name='srental',
    version='1.0.0',
    author='MingXing Xiao',
    author_email='xiaomixin@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
    install_requires=[
        'flask>=2.2.3',
    ],
)

from setuptools import setup, find_packages

setup(
    name='calcy_final',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0,<4.0',
        'pika>=1.1.0',
        # Add other dependencies
    ],
    entry_points={
        'console_scripts': [
            'manage=calcy_final.manage:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)

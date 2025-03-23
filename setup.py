from setuptools import setup, find_packages

setup(
    name="diceware_password_gen",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "diceware_password_gen=password_gen:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

from setuptools import setup, find_packages

setup(
    name="dt-py",
    version="2022.04.01.01",
    description="Python utilities and services for Digital Twin project",
    author="Kolo-naukowe-IDS-AGH",
    author_email="kamilwozniak@student.agh.edu.pl",
    url="https://github.com/Kolo-naukowe-IDS-AGH/digital-twin-py",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT"
)

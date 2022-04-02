from setuptools import find_packages, setup

REQUIRES = ["requests==2.27.1", "urllib3==1.26.9"]

setup(
    name="dt-py",
    version="2022.04.01.02",
    description="Python utilities and services for Digital Twin project",
    author="Kolo-naukowe-IDS-AGH",
    author_email="kamilwozniak@student.agh.edu.pl",
    url="https://github.com/Kolo-naukowe-IDS-AGH/digital-twin-py",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    install_requires=REQUIRES,
    setup_requires=["pytest-runner==6.0.0"],
    tests_require=REQUIRES,
)

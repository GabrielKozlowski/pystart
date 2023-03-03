from setuptools import setup, find_packages

setup(
    name='finances',
    version='0.0.1',
    description='count finances',
    long_description='count brutto, netto, discounts',
    author='Gabriel Kozłowski',
    author_email='gabrys20krk@gmail.com',
    url='https://nowhere.com',
    packages=find_packages(exclude=['tests'])
)

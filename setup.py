from setuptools import setup

setup(
    name='sample_builder',
    version='1.0',
    author='djlihner',
    author_email='likstern@gmail.com',
    url='https://github.com/djlihner/simple_builder',
    install_requires=['flask', 'pylint']
)

entry_points = {
                   'console_scripts': [
                       'builder = builder.app:run',
                   ]
               },

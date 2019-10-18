import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'historical_validation_tool_australia'
release_package = 'tethysapp-' + app_package
app_class = 'historical_validation_tool_australia.app:HistoricalValidationToolAustralia'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = [
    'pandas',
    'io',
    'requests',
    'plotly',
    'numpy',
    'datetime',
    'hydrostats',
    'scipy',
    'traceback',
    'csv',
]

setup(
    name=release_package,
    version='0.0.1',
    tags='',
    description='',
    long_description='',
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)

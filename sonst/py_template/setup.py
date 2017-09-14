from setuptools import setup, find_packages

setup(
    name='cloud_masking',
    version='0.3',
    description='Combining cloud masks from IdePix Sen2Cor and FMask for S2 and L8',
    author='Justin Kotzebue',
    author_email='juko@dhigroup.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
    [console_scripts]
    cloud_mask=cloud_masking.cli:cli
    """
    )

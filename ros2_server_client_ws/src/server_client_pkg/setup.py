from setuptools import find_packages, setup

package_name = 'server_client_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ilknur',
    maintainer_email='ilknurkoparir262@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_server = server_client_pkg.my_server:main",
            "my_client = server_client_pkg.my_client:main"
        ],
    },
)

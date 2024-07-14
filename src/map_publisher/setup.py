from setuptools import find_packages, setup

package_name = "map_publisher"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Iurii Podkorytov",
    maintainer_email="i.podkorytov@innopolis.university",
    description="Example of topic that publishes nav_msgs/OccupancyGrid",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "talker = map_publisher.publisher_node:main",
        ],
    },
)

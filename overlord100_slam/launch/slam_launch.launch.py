from ament_index_python.packages import get_package_share_directory
import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  # Parameters for launch files
  mapper_params_file = os.path.join(
      get_package_share_directory('overlord100_slam'),
      'config',
      'mapper_params_online_async.yaml'
  )
  # mapper_params_file = LaunchConfiguration('slam_params_file', default=PathJoinSubstitution([FindPackageShare('overlord100_slam'), 'config', 'mapper_params_online_async.yaml']))

  # Launch the laser scan merger
  scan_merger_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([FindPackageShare('ros2_laser_scan_merger'), '/launch', '/merge_2_scan.launch.py']),
  )

  # Launch the slam_toolbox
  slam_toolbox_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([FindPackageShare('slam_toolbox'), '/launch', '/online_async_launch.py']),
    launch_arguments=[
      ('slam_params_file', mapper_params_file)
    ]
  )

  return LaunchDescription([
    scan_merger_launch,
    slam_toolbox_launch,
  ])
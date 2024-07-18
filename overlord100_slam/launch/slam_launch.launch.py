from ament_index_python.packages import get_package_share_directory
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
  rviz=LaunchConfiguration('rviz')
  declare_rviz_cmd = DeclareLaunchArgument(
      'rviz', default_value='False', description='Whether to launch rviz'
  )
  mapper_params_file = os.path.join(
      get_package_share_directory('overlord100_slam'),
      'config',
      'mapper_params_online_async.yaml'
  )

  rviz_config_file = os.path.join(
      get_package_share_directory('overlord100_slam'),
      'rviz',
      'slam.rviz'
  )

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

  # Launch rviz
  start_rviz_cmd = Node(
      condition=IfCondition(rviz),
      package='rviz2',
      executable='rviz2',
      arguments=['-d', rviz_config_file],
      output='screen',
  )


  return LaunchDescription([
    scan_merger_launch,
    slam_toolbox_launch,
    declare_rviz_cmd,
    start_rviz_cmd,
  ])
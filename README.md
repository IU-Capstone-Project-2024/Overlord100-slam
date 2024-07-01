# Overlord100-slam
**Scenario 1: Building a Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_no_controller.launch.py
   ```
2. **Start the Differential Drive Controller:**
   ```bash
   ros2 run overlord100_controller diff_drive_controller
   ```
3. **Run the Keyboard Teleop Node:**
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```
4. **Launch SLAM Toolbox with Online Asynchronous Mapping:**
   ```bash
   ros2 launch slam_toolbox online_async_launch.py slam_params_file:=<path/to/mapper_params_online_async.yaml>
   ```
   **Replace `<path/to/mapper_params_online_async.yaml>` with the actual path to your SLAM configuration file.**
5. **Manually control the robot using the keyboard teleop** to explore the environment and let SLAM Toolbox build a map.
6. **Save the Map:**
   ```bash
   ros2 run nav2_map_server map_saver_cli -f <map_name>
   ```
   **Replace `<map_name>` with your desired map file name.**

**Scenario 2: Navigating on a Built Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_no_controller.launch.py
   ```
2. **Start the Differential Drive Controller:**
   ```bash
   ros2 run overlord100_controller diff_drive_controller
   ```
3. **Launch Navigation2 with the Built Map:**
   ```bash
   ros2 launch nav2_bringup bringup_launch.py params_file:=<path/to/nav2_params.yaml> use_sim_time:=True map:=<path/to/map/.yaml>
   ```
   **Replace `<path/to/nav2_params.yaml>` with the path to your Navigation2 parameters file. Replace `<path/to/map/.yaml>` with the path to the map file you saved in Scenario 1.**
4. **Use a GUI tool (like Rviz) or other navigation tools to visualize the map and send navigation goals to the robot.**

**Scenario 3: Simultaneous SLAM and Navigation**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_no_controller.launch.py
   ```
2. **Start the Differential Drive Controller:**
   ```bash
   ros2 run overlord100_controller diff_drive_controller
   ```
3. **Launch SLAM Toolbox with Online Asynchronous Mapping:**
   ```bash
   ros2 launch slam_toolbox online_async_launch.py slam_params_file:=<path/to/mapper_params_online_async.yaml>
   ```
4. **Launch Navigation2 with the Built Map:**
   ```bash
   ros2 launch nav2_bringup navigation_launch.py params_file:=<path/to/nav2_params.yaml> use_sim_time:=True map:=<path/to/map/.yaml>
   ```
   **Ensure that the Navigation2 configuration and SLAM Toolbox parameters are compatible.**
5. **Use a GUI tool or other navigation tools to visualize the map and send navigation goals to the robot. The robot will simultaneously build the map and navigate.**
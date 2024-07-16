# Overlord100-slam
**Scenario 1: Building a Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_custom_controller.launch.py
   ```
2. **Launch SLAM Toolbox with Online Asynchronous Mapping:**
   ```bash
   ros2 launch ros2_laser_scan_merger merge_2_scan.launch.py
   ```
3. **Launch SLAM Toolbox with Online Asynchronous Mapping:**
   ```bash
   ros2 launch slam_toolbox online_async_launch.py slam_params_file:=<path/to/mapper_params_online_async.yaml>
   ```
4. **Save the Map:**
   ```bash
   ros2 run nav2_map_server map_saver_cli -f <map_name>
   ```

**Scenario 2: Navigating on a Built Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_custom_controller.launch.py
   ```
2. **Launch Navigation2 with the Built Map:**
   ```bash
   ros2 launch nav2_bringup bringup_launch.py params_file:=<path/to/nav2_params.yaml> use_sim_time:=True map:=<path/to/map/.yaml>
   ```

**Scenario 3: Simultaneous SLAM and Navigation**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_custom_controller.launch.py
   ```
2. **Launch SLAM Toolbox with Online Asynchronous Mapping:**
   ```bash
   ros2 launch slam_toolbox online_async_launch.py slam_params_file:=<path/to/mapper_params_online_async.yaml>
   ```
3. **Launch Navigation2:**
   ```bash
   ros2 launch nav2_bringup navigation_launch.py params_file:=<path/to/nav2_params.yaml> use_sim_time:=True map:=<path/to/map/.yaml>
   ```
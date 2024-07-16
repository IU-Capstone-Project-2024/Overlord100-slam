# Overlord100-slam
**Scenario 1: Building a Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_custom_controller.launch.py
   ```
2. **Launch scan merger:**
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
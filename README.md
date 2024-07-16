# Overlord100-slam
**Building a Map**

1. **Launch the URDF Dummy Robot:**
   ```bash
   ros2 launch urdf_dummy sim_custom_controller.launch.py
   ```
2. **Launch scan merger and slam toolbox:**
   ```bash
   ros2 launch overlord100_slam/launch/slam_launch.py
   ```
3. **Save the Map:**
   ```bash
   ros2 run nav2_map_server map_saver_cli -f <map_name>
   ```
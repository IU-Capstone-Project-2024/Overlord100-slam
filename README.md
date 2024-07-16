# Overlord100-slam
**Building a Map**
 **First build the package**
   ```bash
   colcon build --packages-select overlord100_slam --symlink-install
   ```
 **Launch scan merger and slam toolbox:**
   ```bash
   ros2 launch overlord100_slam slam_launch.launch.py
   ```
   
 **Save the Map:**
   ```bash
   ros2 run nav2_map_server map_saver_cli -f <map_name>
   ```
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

  **To launch with rviz**

```bash
   ros2 launch overlord100_slam slam_launch.launch.py rviz:=True
```

 **Save the Map:**

- Using rviz slam_toolbox plugin
- `ros2 run nav2_map_server map_saver_cli -f <map_name> `
- `ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap "name: data: 'map_name'"`

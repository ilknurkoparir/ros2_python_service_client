# STEP 1 : Create Workspace and Package
# Create Workspace
```bash
$ source /opt/ros/humble/setup.bash
$ mkdir ros2_server_client_ws
$ cd ros2_server_client_ws
$ mkdir src
$ ros2 pkg create --build-type ament_python server_client_pkg --dependencies rclpy 
$ cd ~/ros2_server_client_ws
$ colcon build --packages-select server_client_pkg --symlink-install


```
# Create Node
```bash
$ cd ros2_server_client_ws/src/server_client_pkg/server_client_pkg/
$ touch my_server.py
$ chmod +x my_server.py
$ touch my_client.py
$ chmod +x my_client.py

```


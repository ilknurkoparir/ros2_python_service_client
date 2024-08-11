import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ilknur/ros2_server_client_ws/install/server_client_pkg'

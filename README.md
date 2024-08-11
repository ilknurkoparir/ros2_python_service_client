Bu proje, ROS2 üzerinde hazır arayüzlerden biri olan `example_interfaces/srv/AddTwoInts` kullanarak python'da servis ve istemci yapısı oluşturulmuştur.

# 1. Adım  : Çalışma Alanı ve Paket Oluşturma
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
# Node(Düğüm) Oluşturma
```bash
$ cd ros2_server_client_ws/src/server_client_pkg/server_client_pkg/
$ touch my_server.py
$ chmod +x my_server.py
$ touch my_client.py
$ chmod +x my_client.py

```

# STEP 2 : Interfaces
```bash
$ cd ros2 interface show example_interfaces/srv/AddTwoInts

```

`AddTwoInts` servisi, ROS2'nin `example_interfaces` paketinde bulunan ve iki tamsayıyı toplamak için kullanılan önceden tanımlanmış bir servistir. int64 a ve int64 b request temsil ederken int64 sum değeri response temsil etmektedir.
- **Sunucu (Server) Düğümü**: İki tamsayıyı toplayan ve sonucu döndüren bir servis sunmaktadır.
- **İstemci (Client) Düğümü**: Sunucuya iki tamsayı göndererek toplam sonucunu almaktadır.
![Screenshot from 2024-08-10 13-54-03](https://github.com/user-attachments/assets/94214e2a-b516-4bff-b5a4-668d1a97ae0b)

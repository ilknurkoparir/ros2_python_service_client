#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MyClientNode(Node):
    def __init__(self):
        super().__init__(node_name = "My_client_node")

        self.client_ = self.create_client(AddTwoInts,"add_two_ints")
        self.get_logger().info("My_client_node başlatıldı.")


        while not self.client_.wait_for_service(timeout_sec= 1.0):
            self.get_logger().warn("Servisin çalışması bekleniyor.")



        
    def callback_my_client_add_two_ints(self):
        request = AddTwoInts.Request()   
        request.a = 10
        request.b = 40 

        #Burada değerler server'a gönderiliyor 
        return self.client_.call_async(request)


def main(args=None):
    rclpy.init(args=args)


    node = MyClientNode() 
    future = node.callback_my_client_add_two_ints()


    rclpy.spin_until_future_complete(node, future) #İşlem tamamlanana kadar devam etmesini sağlamaktadır.
    response = future.result() #Sonuç bu değişkende tutuluyor.


    node.destroy_node()
    rclpy.shutdown()





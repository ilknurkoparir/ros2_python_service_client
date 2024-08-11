#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MyServerNode(Node):
    def __init__(self):
        super().__init__(node_name = "My_server_node")

        self.client_ = self.create_service(AddTwoInts,"add_two_ints",self.callback_my_server_add_two_ints)
        self.get_logger().info("My_server_node başlatıldı.")



    def callback_my_server_add_two_ints(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info("Toplam : " + str(response.sum))
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MyServerNode()
    rclpy.spin(node)
    rclpy.shutdown()




if __name__ == "__main_":
    main()
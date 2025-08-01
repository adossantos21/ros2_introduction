#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.timer = self.create_timer(0.5, self.publishNumber)
        self.get_logger().info(f"Number publisher node has started")

    def publishNumber(self):
        msg = Int64(data=15)
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

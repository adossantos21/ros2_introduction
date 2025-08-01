#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_ = 0
        self.previous_value = 0
        self.subscriber = self.create_subscription(Int64,"number",self.callback_number,10)
        self.publisher = self.create_publisher(Int64,"number_count",10)

    def callback_number(self, msg: Int64):
        self.get_logger().info(f"{msg.data}")
        if self.previous_value != msg.data:
            self.previous_value = msg.data
            self.counter_ += self.previous_value
            new_msg = Int64(data=self.counter_)
            self.publisher.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

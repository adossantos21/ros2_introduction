#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial # facilitates passing extra arguments to an object you pass in a method or function


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a, b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add Two Ints server...")
        
        # Create the request
        request = AddTwoInts.Request(a=a, b=b)

        # Send the request
        future = self.client_.call_async(request)

        # Register a callback that waits for the response - uncomment one of the following
        #future.add_done_callback(self.callback_call_add_two_ints)
        future.add_done_callback(partial(self.callback_call_add_two_ints, request=request)) # passing request to the callback is optional
    
    def callback_call_add_two_ints(self, future, request=None):
        # Retrieve the response
        response = future.result()
        if request is not None:
            self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        else:
            self.get_logger().info(f"Got response: {response.sum}")


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.call_add_two_ints(2, 7)
    node.call_add_two_ints(3, 7)
    node.call_add_two_ints(4, 9)
    rclpy.spin(node) # Node needs to be spinning so it can wait for the response from the server
    rclpy.shutdown()


if __name__ == "__main__":
    main()

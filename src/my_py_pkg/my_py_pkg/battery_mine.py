#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLedMine
from functools import partial # facilitates passing extra arguments to an object you pass in a method or function


class BatteryClientNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("battery_mine") # MODIFY NAME
        self.intervals_ = [4.0, 6.0]
        self.intervals_idx_ = 0
        self.battery_state = self.create_client(SetLedMine, "set_led")
        self.alternate_timer = self.create_timer(self.intervals_[self.intervals_idx_], self.call_battery_state)
        self.get_logger().info("Battery client has been started.")

    def call_battery_state(self):
        while not self.battery_state.wait_for_service(1.0):
            self.get_logger().warn("Waiting for LED panel server...")
        request = SetLedMine.Request()
        request.led_index = 2
        if self.intervals_[self.intervals_idx_] == 4.0:
            request.state = "on"
        elif self.intervals_[self.intervals_idx_] == 6.0:
            request.state = "off"
        else:
            raise ValueError(f"self.intervals_[self.intervals_idx_] should be one of {{4.0, 6.0}}; instead, it is {self.intervals_[self.intervals_idx_]}")
        
        future = self.battery_state.call_async(request)
        future.add_done_callback(partial(self.callback_battery_state, request=request)) # passing request to the callback is optional
        self.intervals_idx_ = (self.intervals_idx_ + 1) % len(self.intervals_)
        self.alternate_timer.cancel()
        self.alternate_timer = self.create_timer(self.intervals_[self.intervals_idx_], self.call_battery_state)

    def callback_battery_state(self, future, request):
        response = future.result()
        self.get_logger().info(f"Request state {request.state} and led number {request.led_index} yielded response: {response}")

def main(args=None):
    rclpy.init(args=args)
    node = BatteryClientNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

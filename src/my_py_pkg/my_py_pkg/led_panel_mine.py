#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedPanelState
from my_robot_interfaces.srv import SetLedMine

class LedPanelServerNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("led_panel_mine") # MODIFY NAME
        self.declare_parameter("led_panel_", [0, 0, 0])
        self.led_panel_ = self.get_parameter("led_panel_").value
        self.publisher = self.create_publisher(LedPanelState, "led_panel_state", 10)
        self.server = self.create_service(SetLedMine, "set_led", self.callback_led_panel)
        self.led_panel_state_timer = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("LED Panel server and publisher have started.")

    def publish_number(self):
        msg = LedPanelState()
        msg.led_panel = self.led_panel_
        self.publisher.publish(msg)
    
    def callback_led_panel(self, request: SetLedMine.Request, response: SetLedMine.Response):
        if request.state == "on":
            self.led_panel_[request.led_index] = 1
        elif request.state == "off":
            self.led_panel_[request.led_index] = 0
        else:
            raise ValueError(f"request.state should be 'on' or 'off'; got '{request.state}' instead.")
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelServerNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

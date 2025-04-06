import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ArucoListener(Node):
    def __init__(self):
        super().__init__('aruco_listener')
        self.subscription = self.create_subscription(
            String,
            'aruco_data',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        data = msg.data
        markers = data.split("|")  # Format: "ID:x,y|ID:x,y"
        for marker in markers:
            marker_id, coords = marker.split(":")
            x, y = map(float, coords.split(","))
            print(f"Marker {marker_id} berada di: ({x}, {y})")

rclpy.init()
node = ArucoListener()
rclpy.spin(node)
rclpy.shutdown()

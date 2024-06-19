import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid

class MapPublisher(Node):

    def __init__(self):
        super().__init__('map_publisher')
        self.publisher_ = self.create_publisher(OccupancyGrid, '/map', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.publish_map)

    def publish_map(self):
        msg = OccupancyGrid()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"

        msg.info.resolution = 1.0 # The map resolution [m/cell]
        msg.info.width = 10 # Map width [cells]
        msg.info.height = 10 # Map height [cells]
        
        # Origin position
        msg.info.origin.position.x = 0.0
        msg.info.origin.position.y = 0.0
        msg.info.origin.position.z = 0.0
        # Orientation
        msg.info.origin.orientation.w = 1.0 

        # The map data, in row-major order, starting with (0,0).  Occupancy
        # probabilities are in the range [0,100].  Unknown is -1.
        msg.data = [-1] * (msg.info.width * msg.info.height)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing an empty occupancy grid')

def main(args=None):
    rclpy.init(args=args)
    map_publisher = MapPublisher()
    rclpy.spin(map_publisher)

    map_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

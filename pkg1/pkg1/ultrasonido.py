import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random  

class Ultrasonido(Node):

    def __init__(self):
        
        super().__init__('ultra_dist')
        
        
        self.publisher_ = self.create_publisher(String, 'dist', 10)
        
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
       
        numero_aleatorio = random.randint(1, 10)
        
        msg = String()
        
        msg.data = str(numero_aleatorio)
        
        self.publisher_.publish(msg)
        
       
        self.get_logger().info(f'Distancia: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Ultrasonido()

    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass 
    finally:
        minimal_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
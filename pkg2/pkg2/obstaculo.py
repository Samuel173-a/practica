#obstaculo
#obstaculo
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Obstaculo(Node):

    def __init__(self):
        # Mantenemos el nombre que pediste o puedes usar 'sub_dist'
        super().__init__('sub_dist')
        
       
        self.subscription = self.create_subscription(
            String,
            'dist',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        try:
            
            valor_distancia = int(msg.data)
            
            if valor_distancia < 5:
                self.get_logger().warn(f'Alerta: {valor_distancia} ')
            else:
                self.get_logger().info(f'Distancia segura: {valor_distancia}')
                
        except ValueError:
   
            self.get_logger().error(f'Recibí algo que no es un número: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Obstaculo()

    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        minimal_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
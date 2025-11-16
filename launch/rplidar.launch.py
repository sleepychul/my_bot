import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                # ★ by-path → by-id 로 변경
                'serial_port': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',

                # ★ baudrate 추가 (A1이면 보통 115200, A2/A3 계열이면 256000)
                'serial_baudrate': 115200,

                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])

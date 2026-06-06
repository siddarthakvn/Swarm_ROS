from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'rescue_bot',
                '-file',
                '/home/kvn/sar_ws/src/rescue_bot_description/urdf/rescue_bot.urdf',
                '-x', '0',
                '-y', '0',
                '-z', '0.1'
            ],
            output='screen'
        )
    ])
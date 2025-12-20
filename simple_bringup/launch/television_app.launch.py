from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    remap_channel_topic = ("channel_something", "new_channel_something")
    
    television_publisher_node = Node(
        package="simple_py_pkg",
        executable="channel_node",
        name="new_television_node",
        remappings=[
            remap_channel_topic
        ],
        parameters=[
            {"parameter_1_int": 5},
            {"parameter_2_string": "GO"}
        ]
    )
    
    remote_controller_node = Node(
        package="simple_py_pkg",
        executable="remote_controller_node",
        name="new_remote_controller_node",
        remappings=[
            remap_channel_topic
        ]
    )
    
    ld.add_action(television_publisher_node)
    ld.add_action(remote_controller_node)

    return ld
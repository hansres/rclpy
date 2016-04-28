# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time

# this is needed to allow rclpy to be imported from the build folder
sys.path.insert(0, os.getcwd())


def talker():
    import rclpy
    from rclpy.qos import qos_profile_default

    rclpy.init([])

    # TODO(wjwwood) move this import back to the module level when
    # it is possible to import the messages before rclpy.init().
    from std_msgs.msg import String

    node = rclpy.create_node('talker')

    chatter_pub = node.create_publisher(String, 'chatter', qos_profile_default)

    msg = String()

    i = 1
    print('talker: beginning loop')
    while True:
        msg.data = 'Hello World: {0}'.format(i)
        i += 1
        print('talker sending: ' + msg.data)
        chatter_pub.publish(msg)
        time.sleep(1)

if __name__ == '__main__':
    try:
        talker()
    except KeyboardInterrupt:
        print('talker stopped cleanly')
    except BaseException:
        print('exception in talker:', file=sys.stderr)
        raise
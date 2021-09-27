import rospy 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

def main():
    rospy.init_node('set_model_state')

    state_msg = ModelState()
    state_msg.model_name = 'tiago' # 'tiago', 'ground_plane', 'obstacle_name'
    state_msg.pose.position.x = 2.5
    state_msg.pose.position.y = 7.0
    state_msg.pose.position.z = 0
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0.0
    state_msg.pose.orientation.w = 0
    state_msg.twist.linear.x = 0
    state_msg.twist.linear.y = 0
    state_msg.twist.linear.z = 0
    state_msg.twist.angular.x = 0
    state_msg.twist.angular.y = 0
    state_msg.twist.angular.z = 1.0

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state(state_msg)
        print('resp: ', resp)

    except rospy.ServiceException (e):
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

#class Node():
class Master():#Node):

    
    def __init__(name="test")::
        self.name = "%s%d"%(name, math.rand())
        rospy.init_node(name, anonymous=True)
        self.pubSys = rospy.Publisher('system', String, queue_size=10)
        self.subSys = rospy.Subscriber('system', String, handleSys)
        self.pubPr = rospy.Publisher('%s/move'%self.name, String, queue_size=10)
        self.subPr = rospy.Publisher('%s/move'%self.name, String, handle)
        self.battery = 100
        self.charging = {}
        self.full = {}
        self.occupation = {}
        self.master = None
        self.charger = (0,0)

    def handle(data):
        msg = data.data
        words = data.split(' ')
        if words[0] == "attribute":


    def handleSys(data):
        msg = data.data
        words = data.split(' ')
        if  words[0] == "oob":
            self.occupation.remove(data.caller_id)
        elif words[0] == "moved":
            self.occupation.add(pair(data.caller_id,words[1]))
        elif words[0] == "newMaster":
            self.master = words[1]
        else:
            pass

    def move(location):
        # move to location
        #

    def recharge():
        self.pubSys.publish("oob")
        move(self.charger)

    def startMaster():
        

    def setMaster(uri):
        self.master = uri

    def attribute(slot):
        if(!self.full.empty()):
            node = self.full.pop()
        else:
            node = self.charging.pop()
        
        node.publish("attribute %s" % slot)


if __name__ == '__main__':
    try:
        node = Master()

    except rospy.ROSInterruptException:
        pass

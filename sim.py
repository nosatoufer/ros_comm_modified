#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
import socket

from std_msgs.msg import String

node = None

def handleSys(data):
    msg = data.data
    words = msg.split(" ")
    print(rospy.get_caller_id())
    if  words[0] == "oob":
        name = words[1]
        node.rmOccupation(name)
        node.addNode(name)
    elif words[0] == "moved":
        name = words[1]
        loc = words[2]
        node.addOccupation(name, loc)
    elif words[0] == "newMaster":
        uri = words[1]
        node.master = uri
    elif words[0] == "newNode":
        node.addNode(words[1])
    elif words[0] == "attribute" and words[1] == node.name:
        node.move(words[2])
    else:
        pass

def handle(data):
    words = data.data.split(" ")
    print(words)
    if words[0] == "attribute":
        node.move(words[1])

class Master():


    def __init__(self, name="test"):
        self.name = name
        rospy.init_node(name, anonymous=True)
        self.pubSys = rospy.Publisher('coordination', String, queue_size=10)
        self.subSys = rospy.Subscriber('coordination', String, handleSys)
        #self.pubPr = rospy.Publisher('%s/move'%self.name, String, queue_size=10)
        #self.subPr = rospy.Subscriber('%s/move'%self.name, String, handle)
        self.battery = 100
        self.charging = {}
        self.occupation = {}
        self.slots = 3
        self.master = None
        self.charger = (0,0)
        self.pubSys.publish("newNode %s" %(name))

    def addNode(self, node):
        self.charging[node] = 100

    def rmNode(self, node):
        del self.charging[node]

    def addOccupation(self, node, location):
        del self.charging[node]
        self.occupation[node] = location

    def rmOccupation(self, node):
        del self.occupation[node]
        self.charging[node] = 100

    def move(self, location):
        pubSys.publish("moved %s %s" %(self.name, location))

    def recharge(self):
        self.pubSys.publish("oob %s" % self.name)
        move(self.charger)

    def startMaster(self):
        i = 0
        while len(self.occupation) < self.slots - 1 and len(self.charging) > 0 :
            attribute(i)

    def setMaster(self, uri):
        self.master = uri

    def attribute(self, slot):
        if len(self.charging) > 0:
            for i, v in self.charging.items():
                if v > 0:
                    self.pubSys.publish("attribute %s %s" % (i,slot))


if __name__ == '__main__':
    try:
        name = socket.gethostname()
        print(name)
        node = Master(name)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

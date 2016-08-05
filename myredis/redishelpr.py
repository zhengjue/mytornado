#!/bine/env python
# _*_  coding:utf-8 _*_
import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host="127.0.0.1", port=6379)
        self.chan_sub = "fm100"
        self.chan_pub = "fm100"

    def get(self,key):
        return self.__conn.get(key)

    def set(self,key,value):
        self.__conn.set(key,vlaue)

    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


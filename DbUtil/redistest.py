# coding=utf-8
import redis


class redisHelper(object):
    def collection(self, ip, port):
        r = redis.StrictRedis()
        return r


if __name__ == '__main__':
    pc = redisHelper()
    t = pc.collection('127.0.0.1', '6739')
    t.set('1','e')
    t.set('2','rt')
    print (t.get('2'))

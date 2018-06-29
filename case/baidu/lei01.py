# coding:utf-8

class People(object):

    def hand(self):
        print('这是手')

    def foot(self):
        print('这是脚')



if __name__ == '__main__':
    human = People()
    human.hand()
    human.foot()

# coding=utf-8

class Count():
    def __init__(self):
        print("这里是初始化内容")
        self.a=5
        self.b=6

    def add(self):
        d=self.a+self.b
        return d

    def acc(self):
        c=self.a -self.b
        return c

    def cee(self):
        e=self.add()*self.acc()
        return e

# if __name__ =="__main__":
a=Count()
print(a.add())
print(a.acc())
print(a.cee())
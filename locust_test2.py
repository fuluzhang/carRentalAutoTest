'''
任务集合:分层的方式，按模块，子系统来管理
'''
from locust import TaskSet, task, HttpUser, between


# 租车系统
# 系统管理模块

class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")

    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")

    @task
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")

# 基础管理模块
class BasicManage(TaskSet):
    @task(7)
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task(3)
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")

class CarRentalTest(HttpUser):
    wait_time = between(1,3) #任务之间的间隔时间
    # tasks = [BasicManage,SystemManage] # 任务集合，tasks是User中定义的属性，不能写错。
    tasks = {BasicManage:4,SystemManage:1}  # 任务集合，后面数字表示权重，访问基础模块的人会比访问系统模块的人多三倍

    def on_start(self):
        user={"loginname":"admin","pwd":"123456"} #测试前置，登录，在开始运行时每个用户调用一次
        self.client.post("/carRental/login/login.action",data=user)

    def on_stop(self): #测试后置，退出登录，在结束运行时每个用户调用一次
        self.client.post("/carRental/logout/logout.action") #接口错误，执行失败

# locust -f locust_test2.py  --host=http://127.0.0.1:8080
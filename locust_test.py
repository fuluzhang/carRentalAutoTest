'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
为要模拟的用户定义一个类，从HttpUser继承
'''

class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time 是User类定义的一个属性，表示等待时间
    wait_time = between(3,8) #任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def carManage(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllmenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")

# 加压模型
# class StepLoadShape(LoadTestShape):
#  """
#     A step load shape
#     Keyword arguments:
#
#         step_time -- Time between steps
#         step_load -- User increase amount at each step
#         spawn_rate -- Users to stop/start per second at every step
#         time_limit -- Time limit in seconds
#
#     """
#
#     step_time = 30    #两个阶梯之间的时间
#     step_load = 10    #每个阶梯增加的用户数
#     spawn_rate = 10   #用户上线的速率
#     time_limit = 600  #测试的时长
#
#     def tick(self):  # 控制执行时的用户数及速率
#         run_time = self.get_run_time()
#
#         if run_time > self.time_limit:
#             return None
#
#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)

# class DoubleWave(LoadTestShape):
#     """
#     A shape to immitate some specific user behaviour. In this example, midday
#     and evening meal times.
#
#     Settings:
#         min_users -- minimum users
#         peak_one_users -- users in first peak
#         peak_two_users -- users in second peak
#         time_limit -- total length of test
#     """
#
#     min_users = 20
#     peak_one_users = 60
#     peak_two_users = 40
#     time_limit = 600
#
#     def tick(self):
#         run_time = round(self.get_run_time())
#
#         if run_time < self.time_limit:
#             user_count = (
#                 (self.peak_one_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
#                 + (self.peak_two_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
#                 + self.min_users
#             )
#             return (round(user_count), round(user_count))
#         else:
#             return None

class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None

# locust -f locust_test.py  --host=http://127.0.0.1:8080

# locust -f locust_test.py --host=http://127.0.0.1:8089 --web-host=127.0.0.1 --web-port=8088
# locust -f locust_test.py --step-load

# class MyCustomShape(LoadTestShape):
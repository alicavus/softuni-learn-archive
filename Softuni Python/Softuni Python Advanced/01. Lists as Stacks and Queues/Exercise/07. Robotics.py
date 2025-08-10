from collections import deque

class Clock:
    def __init__(self, time: str):
        time_data = time.split(":")
        self.seconds = int(time_data[0]) * 3600
        self.seconds += int(time_data[1]) * 60
        self.seconds += int(time_data[2])
    
    def __repr__(self):
        hours = self.seconds // 3600
        while hours >= 24:
            hours -= 24 
        seconds = self.seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60 
        return f"[{hours:0>2}:{minutes:0>2}:{seconds:0>2}]"
    
    def __str__(self):
        return self.__repr__()
    
    def increment(self):
        self.seconds += 1

class Robot:
    def __init__(self, robot_data: str):
        robot_name, robot_proc_time = robot_data.split("-")
        self.name = robot_name
        self.time = int(robot_proc_time)

        self.product = {"name": "", "time": 0}
    
    def __repr__(self):
        return f'{self.name} - {self.product["name"]}'
    
    def __str__(self):
        return self.__repr__()
    
    def add(self, product: str) -> bool:
        if self.product["time"]:
            return False
        self.product["name"] = product
        self.product["time"] = self.time
        return True
    
    def tick(self):
        if self.product["time"]:
            self.product["time"] -= 1
        if self.product["time"] == 0:
            self.product = {"name": "", "time": 0}
    
    def is_available(self):
        return self.product["time"] == 0


robots = []

robots_infos = input().split(";")

assembly_line = deque()

for robot_info in robots_infos:
    robots.append(Robot(robot_info))

cur_time = Clock(input())

while True:
    cur_product = input()

    if cur_product == "End":
        break

    assembly_line.append(cur_product)

while assembly_line:
    cur_time.increment()


    cur_product = assembly_line.popleft()

    curr_proccessed = False

    for robot_idx in range(len(robots)):
        robots[robot_idx].tick()
        if robots[robot_idx].is_available() and not curr_proccessed:
            if robots[robot_idx].add(cur_product):
                print(robots[robot_idx], cur_time)
                curr_proccessed = True
                
    
    if not curr_proccessed:
        assembly_line.append(cur_product)




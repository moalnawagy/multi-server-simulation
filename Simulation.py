from pythonds.basic import Queue

class Person:
    def __init__(self, experience):
        self.experience = experience
        self.CurrentCustomer = None
        self.TimeRemaining = 0
        self.idleTime = 0

    def ClockTick(self):
        if self.CurrentCustomer != None:
            self.TimeRemaining -= 1
            if self.TimeRemaining <= 0:
                self.CurrentCustomer = None
        else:
            self.idleTime +=1
    
    def Busy(self):
        if self.CurrentCustomer != None:
            return True
        else:
            return False

    def StartNewClient(self, Client):
        self.CurrentCustomer = Client
        self.TimeRemaining = Client.GetServiceTime()
    def GetIdleTime(self):
        return self.idleTime
    
import random

class Customer:
    def __init__(self, Time, ServiceTime):
        self.ArrivalTime = Time
        self.ServiceTime = ServiceTime

    def GetServiceTime(self):
        return self.ServiceTime

    def WaitingTime(self, TimeNow):
        return TimeNow - self.ArrivalTime




arrivalTimes = [0, 2, 6, 10, 12, 14]
serviceTime = [5, 3, 3, 5, 6, 3]

def SimulateMultiServer(WorkingTime):

    Able = Person(2)
    Baker = Person(1)
    WaitingHall = Queue()
    WaitingTIme = []
    counter = 0
    for CurrrentMin in range(WorkingTime):

        if CurrrentMin in arrivalTimes:
            ThePatient = Customer(CurrrentMin, serviceTime[counter])
            counter += 1
            WaitingHall.enqueue(ThePatient)
        
        if (not Able.Busy()) and (not WaitingHall.isEmpty()):
            NextClient = WaitingHall.dequeue()
            waiting = NextClient.WaitingTime(CurrrentMin)
            if waiting>0:
                WaitingTIme.append(waiting)
            Able.StartNewClient(NextClient)
        elif (not Baker.Busy()) and (not WaitingHall.isEmpty()):
            NextClient = WaitingHall.dequeue()
            waiting = NextClient.WaitingTime(CurrrentMin)
            if waiting>0:
                WaitingTIme.append(waiting)
            Baker.StartNewClient(NextClient)

        Able.ClockTick()
        Baker.ClockTick()
    AvgWaitForWhoWaited = sum(WaitingTIme) / len(WaitingTIme)
    AvgWait = sum(WaitingTIme) / len(serviceTime)
    AvgSpendInSystem = (sum(WaitingTIme) + sum(serviceTime)) / len(serviceTime)
    AvgServiceTime = sum(serviceTime) / len(serviceTime)
    timeAvgNumber = sum(WaitingTIme)/ WorkingTime
    Throughput = len(serviceTime) / WorkingTime
    totalBusyTime = ((18-Able.GetIdleTime()) + (18-Baker.GetIdleTime()))/2
    Utilization = totalBusyTime/18
    AbleUtilization = (18-Able.GetIdleTime()) /18
    BakerUtilization = (18-Baker.GetIdleTime()) /18


    print("Average waiting time of those who wait in queue d(n): ",AvgWaitForWhoWaited, "min")
    print("Time-average number in queue q(n): ", timeAvgNumber, "cust")
    print("Total busy time B(t):", totalBusyTime, "min")
    print("System Utilization u(n):", Utilization*100,"%")
    print("Able Utilization u(n):", AbleUtilization*100,"%")
    print("Baker Utilization u(n):", BakerUtilization*100,"%")
    print("Average service time:", AvgServiceTime, "min")
    print("Average Waiting Time", AvgWait, "min")
    print("Average time customer spends in the system:", AvgSpendInSystem, "min")
    print("Throughput: ", Throughput, "cust/min")

def SimulateSingleServer(WorkingTime):

    Able = Person(2)
    WaitingHall = Queue()
    WaitingTIme = []
    counter = 0
    for CurrrentMin in range(WorkingTime):

        if CurrrentMin in arrivalTimes:
            ThePatient = Customer(CurrrentMin, serviceTime[counter])
            counter += 1
            WaitingHall.enqueue(ThePatient)
        
        if (not Able.Busy()) and (not WaitingHall.isEmpty()):
            NextClient = WaitingHall.dequeue()
            waiting = NextClient.WaitingTime(CurrrentMin)
            if waiting>0:
                WaitingTIme.append(waiting)
            Able.StartNewClient(NextClient)
       
        Able.ClockTick()
    AvgWaitForWhoWaited = sum(WaitingTIme) / len(WaitingTIme)
    AvgWait = sum(WaitingTIme) / len(serviceTime)
    AvgSpendInSystem = (sum(WaitingTIme) + sum(serviceTime)) / len(serviceTime)
    AvgServiceTime = sum(serviceTime) / len(serviceTime)
    timeAvgNumber = sum(WaitingTIme)/ WorkingTime
    Throughput = len(serviceTime) / WorkingTime
    totalBusyTime = (18-Able.GetIdleTime()) 
    Utilization = totalBusyTime/18



    print("Average waiting time of those who wait in queue d(n): ",AvgWaitForWhoWaited, "min")
    print("Time-average number in queue q(n): ", timeAvgNumber, "cust")
    print("Total busy time B(t):", totalBusyTime, "min")
    print("System Utilization u(n):", Utilization*100,"%")
    print("Average service time:", AvgServiceTime, "min")
    print("Average Waiting Time", AvgWait, "min")
    print("Average time customer spends in the system:", AvgSpendInSystem, "min")
    print("Throughput: ", Throughput, "cust/min")

    
print("Multi Server Simulation Results")
SimulateMultiServer(18)
print("**************************************")
print("Single Server Simulation Results")

SimulateSingleServer(25)

    
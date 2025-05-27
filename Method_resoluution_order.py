# in a company work is a assigned based on roles of the worker 
      
class Manager:
    def role(self):
        print("Manages the work")
        
class Senior(Manager):
    def role(self):
        print("Supervises workers")
    
class intern(Senior, Manager):
    pass

c1 = intern()
c1.role()


#customer first talks to a Support Agent, then a Team Lead, and finally a Manager if your issue isn’t resolved.
class Manager:
    def customer_service(self):
        print("The manager is the last person a customer talks to")
        
class TeamLeader(Manager):
    def customer_service(self):
        print("Team Leader presents the complaints of the customers to the manager")
        super().customer_service()
        
class SupportAgent(TeamLeader, Manager):
    def customer_service(self):
        print("Agent collects complaints from customer")
        super().customer_service()
        
sup = SupportAgent()
sup.customer_service()

print("\n")
print(SupportAgent.mro())
    

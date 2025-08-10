from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []
    
    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
        return self
    
    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
        return self
    
    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
        return self
    
    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
        return self
    
    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
        return subscription
    
    def get_item(self, collection: list[Subscription | Trainer | ExercisePlan | Equipment | Customer], item_id: int):
        return next((i for i in collection if i.id == item_id), None)
    
    def subscription_info(self, subscription_id: int) -> str:
        subscription = self.get_item(self.subscriptions, subscription_id)

        if subscription:
            customer = self.get_item(self.customers, subscription.customer_id)
            trainer = self.get_item(self.trainers, subscription.trainer_id)
            plan = self.get_item(self.plans, subscription.exercise_id)
            equipment = self.get_item(self.equipment, plan.equipment_id)

            if all(i is not None for i in [customer, trainer, equipment, plan]):
                return "\n".join([subscription.__repr__(), customer.__repr__(), trainer.__repr__(), equipment.__repr__(), plan.__repr__()])
# ------------------------------------------
# Task: Inheritance with MobilePhone, Apple, and Samsung
# ------------------------------------------

# Base class: MobilePhone
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    # Basic functionalities for all mobile phones
    def make_call(self, number):
        print(f"Making a call to {number}...")
    
    def receive_call(self, caller):
        print(f"Receiving a call from {caller}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera and {self.front_camera} front camera.")

    def show_specs(self):
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("------------------------------------------")

# Child class: Apple
class Apple(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=False, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_siri(self):
        print(f"{self.model} is using Siri to assist you.")

    def show_model(self):
        print(f"Apple Model: {self.model}")
        print("------------------------------------------")

# Child class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=True, front_camera="16MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_bixby(self):
        print(f"{self.model} is using Bixby to assist you.")

    def show_model(self):
        print(f"Samsung Model: {self.model}")
        print("------------------------------------------")

# Creating some objects of Apple class with different properties
iphone_12 = Apple(model="iPhone 12", front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB")
iphone_13_pro = Apple(model="iPhone 13 Pro", front_camera="12MP", rear_camera="12MP", ram="6GB", storage="128GB")

# Creating some objects of Samsung class with different properties
galaxy_s21 = Samsung(model="Samsung Galaxy S21", front_camera="16MP", rear_camera="48MP", ram="8GB", storage="128GB")
galaxy_note20 = Samsung(model="Samsung Galaxy Note 20", front_camera="16MP", rear_camera="108MP", ram="12GB", storage="256GB")

# Demonstrating the functionalities
print("------------------------------------------")
iphone_12.show_model()
iphone_12.show_specs()
iphone_12.make_call("123-456-7890")
iphone_12.take_a_picture()
iphone_12.use_siri()

print("------------------------------------------")
iphone_13_pro.show_model()
iphone_13_pro.show_specs()
iphone_13_pro.receive_call("987-654-3210")
iphone_13_pro.take_a_picture()
iphone_13_pro.use_siri()

print("------------------------------------------")
galaxy_s21.show_model()
galaxy_s21.show_specs()
galaxy_s21.make_call("555-1234")
galaxy_s21.take_a_picture()
galaxy_s21.use_bixby()

print("------------------------------------------")
galaxy_note20.show_model()
galaxy_note20.show_specs()
galaxy_note20.receive_call("111-2222")
galaxy_note20.take_a_picture()
galaxy_note20.use_bixby()

print("------------------------------------------")
# ------------------------------------------
# All tasks completed
# ------------------------------------------

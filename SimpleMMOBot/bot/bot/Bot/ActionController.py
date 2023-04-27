from .Initializer import Initializer
from Handlers.TimeHandler import TimeHandler
from Handlers.TextHandler import TextHandler
from Handlers.Logger import Logger
from ActionManagers.LoginManager import LoginManager
from ActionManagers.VerificationManager import VerificationManager
from ActionManagers.StepManager import StepManager
from ActionManagers.MobAttackManager import MobAttackManager
from ActionManagers.MaterialGatheringManager import MaterialGatheringManager
from ActionManagers.FileManager import FileManager

class ActionController:
    def __init__(self):
        self.user = Initializer.initialize_user_class()
        self.discord = Initializer.initialize_discord_class()
        self.chrome_handler = Initializer.initialize_chrome_driver()
        self.element_handler = Initializer.initialize_element_handler(
            self.chrome_handler.driver)
        self.action_decision_maker = Initializer.initialize_action_decision_maker(
            self.element_handler)
        self.logger = Initializer.initialize_logger()
        self.logged_in = False
        self.action_counter = {"Steps": 0,
                       "Mob Attacks": 0,
                       "Gather Materials - Grab": 0,
                       "Gather Materials - Salvage": 0,
                       "Gather Materials - Catch": 0,
                       "Gather Materials - Chop": 0,
                       "Gather Materials - Mine": 0}

    def find_next_action_and_element(self):
        self.action_decision_maker.find_next_action(logged_in=self.logged_in)  
        if self.action_decision_maker.next_action != "None":
                current_action_in_text = TextHandler.get_current_action_in_text(self.action_decision_maker.next_action)
                print(current_action_in_text)
                self.logger.log_info(current_action_in_text)

    def execute_next_action(self, next_action, element):
            TimeHandler.sleep_for_random_time(0.3, 0.6)
            match next_action:
                case "Login":
                    LoginManager.login(chrome_handler=self.chrome_handler, 
                                       element_handler=self.element_handler,
                                       email=self.user.email, 
                                       password=self.user.password
                    )
                    self.logged_in = True
                case "AFK Verification":
                    VerificationManager.inform_about_afk_verification(
                        chrome_handler=self.chrome_handler,
                        discord_model=self.discord
                    )
                case "Step":
                    StepManager.take_steps(take_step_button=element)
                    self.action_counter["Steps"] += 1
                case "Attack Mob":
                    MobAttackManager.attack_mob_until_dead(link_to_mob_attack_page=element,
                                                           chrome_handler=self.chrome_handler,
                                                           element_handler=self.element_handler,
                                                           discord_model=self.discord
                    )
                    self.action_counter["Mob Attacks"] += 1
                case "Gather Materials":
                    MaterialGatheringManager.gather_materials(
                        chrome_handler=self.chrome_handler, 
                        element_handler=self.element_handler, 
                        action=self.action_decision_maker.gathering_action, 
                        link_to_material_gathering_page=element, 
                        discord_model=self.discord
                    )
                    self.action_counter[f"Gather Materials - {self.action_decision_maker.gathering_action}"] += 1


    def take_action_depending_on_current_screen(self):
        user_wants_bot_to_run = True
        while user_wants_bot_to_run:
            self.find_next_action_and_element()
            self.execute_next_action(next_action=self.action_decision_maker.next_action,
                                     element=self.action_decision_maker.element)
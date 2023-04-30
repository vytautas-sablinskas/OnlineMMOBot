from .Initializer import Initializer
from Managers.Files.FileManager import FileManager
from Constants.FilePaths import FilePaths
from Handlers.TimeHandler import TimeHandler
from Handlers.TextHandler import TextHandler
from Handlers.FileHandler import FileHandler
from Managers.Authentication.LoginManager import LoginManager
from Managers.Actions.VerificationManager import VerificationManager
from Managers.Actions.StepManager import StepManager
from Managers.Actions.MobAttackManager import MobAttackManager
from Managers.Actions.MaterialGatheringManager import MaterialGatheringManager

class ActionController:
    def __init__(self):
        self.break_manager = Initializer.initialize_break_manager()
        self.user = Initializer.initialize_user_class()
        self.discord = Initializer.initialize_discord_class()
        self.chrome_handler = Initializer.initialize_chrome_driver()
        self.element_handler = Initializer.initialize_element_handler(
            self.chrome_handler.driver)
        self.decision_maker = Initializer.initialize_decision_maker(
            self.element_handler)
        self.logged_in = False
        self.action_counter = {
            "Steps Taken": 0,
            "Mobs Attacked": 0,
            "Grab": 0,
            "Salvage": 0,
            "Catch": 0,
            "Chop": 0,
            "Mine": 0,
            "AFK Checks": 0,
            "Time Breaks": 0
        }

    def find_next_action_and_element(self):
        self.decision_maker.find_next_action(logged_in=self.logged_in, action_counter=self.action_counter, break_manager=self.break_manager)  
        if self.decision_maker.next_action != "None":
                current_action_in_text = TextHandler.get_current_action_in_text(self.decision_maker.next_action)
                FileManager.log_text(file_path=FilePaths.ACTION_TRACKING_LOGS.value, 
                                     message=current_action_in_text
                )
                FileHandler.write_into_file_with_hashmap(file_path=FilePaths.SESSION_ACTION_SUMMARY.value,
                                            hashmap=self.action_counter)
                print(current_action_in_text)

    def execute_next_action(self, next_action, element):
            TimeHandler.sleep_for_random_time(0.3, 0.6)
            match next_action:
                case "Time Break":
                    self.break_manager.wait_until_break_time_ends()
                case "Login":
                    LoginManager.login(
                        chrome_handler=self.chrome_handler, 
                        element_handler=self.element_handler,
                        email=self.user.email, 
                        password=self.user.password
                    )
                    self.logged_in = True
                case "AFK Verification":
                    VerificationManager.notify_user_about_afk_verification(
                        chrome_handler=self.chrome_handler,
                        element_handler=self.element_handler,
                        discord_model=self.discord
                    )
                case "Step":
                    StepManager.take_steps(take_step_page=element)
                case "Attack Mob":
                    MobAttackManager.fight_mob_until_defeated(
                        mob_attack_page=element,
                        chrome_handler=self.chrome_handler,
                        element_handler=self.element_handler,
                        discord_model=self.discord
                    )
                case "Gather Materials":
                    MaterialGatheringManager.gather_materials(
                        chrome_handler=self.chrome_handler, 
                        element_handler=self.element_handler, 
                        action=self.decision_maker.gathering_action, 
                        link_to_material_gathering_page=element, 
                        discord_model=self.discord
                    )


    def take_action_depending_on_current_screen(self):
        user_wants_bot_to_run = True
        while user_wants_bot_to_run:
            self.find_next_action_and_element()
            self.execute_next_action(next_action=self.decision_maker.next_action,
                                     element=self.decision_maker.element)
from .Initializer import Initializer
from Handlers.TimeHandler import TimeHandler
from ActionManagers.LoginManager import LoginManager
from ActionManagers.VerificationManager import VerificationManager
from ActionManagers.StepManager import StepManager
from ActionManagers.MobAttackManager import MobAttackManager
from ActionManagers.MaterialGatheringManager import MaterialGatheringManager

class ActionController:
    def __init__(self):
        self.user = Initializer.initialize_user_class()
        self.discord = Initializer.initialize_discord_class()
        self.chrome_handler = Initializer.initialize_chrome_driver()
        self.element_handler = Initializer.initialize_element_handler(
            self.chrome_handler.driver)
        self.action_decision_maker = Initializer.initialize_action_decision_maker(
            self.element_handler)

    def take_action_depending_on_current_screen(self):
        logged_in = False
        finished_afk_check = False
        user_wants_bot_to_run = True
        while user_wants_bot_to_run:
            self.action_decision_maker.find_next_action(logged_in=logged_in)
            next_action = self.action_decision_maker.next_action
            if next_action != "None":
                print(next_action)
            element = self.action_decision_maker.element

            TimeHandler.sleep_for_random_time(0.3, 0.6)
            next_action = "Step" if finished_afk_check else next_action
            finished_afk_check = False
            match next_action:
                case "Login":
                    LoginManager.login(chrome_handler=self.chrome_handler, 
                                       element_handler=self.element_handler,
                                       email=self.user.email, 
                                       password=self.user.password
                    )
                    logged_in = True
                case "AFK Verification":
                    VerificationManager.inform_about_afk_verification(
                        discord_model=self.discord
                    )
                    finished_afk_check = True
                case "Step":
                    StepManager.take_steps(take_step_button=element)
                case "Attack Mob":
                    MobAttackManager.attack_mob_until_dead(link_to_mob_attack_page=element,
                                                           chrome_handler=self.chrome_handler,
                                                           element_handler=self.element_handler,
                                                           discord_model=self.discord
                    )
                case "Gather Materials":
                    MaterialGatheringManager.gather_materials(
                        chrome_handler=self.chrome_handler, 
                        element_handler=self.element_handler, 
                        action=self.action_decision_maker.gathering_action, 
                        link_to_material_gathering_page=element, 
                        discord_model=self.discord
                    )

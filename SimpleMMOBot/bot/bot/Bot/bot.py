import selenium.common.exceptions as ex
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import random
import discord_webhook as dc
import os
from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium.webdriver.common.by import By  # locate elements
from selenium.webdriver import ChromeOptions
import subprocess

#globals
action_map = {"Grab": 0, "Salvage": 0, "Catch": 0, "Chop": 0, "Mine": 0, "Step": 0, "Attack": 0, "Battle Arena": 0}
start_time = time.time()
repeat_quests = False
continue_script = False
battle_arena_question_timer = time.time()

def update_status(text):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = f"Bot status: {text}, Last Updated: {current_time}"
    with open("status.txt", "w") as f:
        f.seek(0)
        f.truncate()
        f.write(status)

def time_played():
    elapsed_time = time.time() - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def check_for_link(driver, link_text):
    try:
        attack_element = driver.find_element(By.LINK_TEXT, link_text)
        return attack_element
    except ex.NoSuchElementException:
        pass
    
    return None

def check_by_xpath(driver, locator):
    try:
        element = driver.find_element(By.XPATH, locator)
        return element
    except ex.NoSuchElementException:
        pass
    
    return None

def check_by_id(driver, locator):
    try:
        element = driver.find_element(By.ID, locator)
        return element
    except ex.NoSuchElementException:
        pass
    
    return None

def check_by_css_selector(driver, locator):
    try:
        element = driver.find_element(By.CSS_SELECTOR, locator)
        return element
    except ex.NoSuchElementException:
        pass
    
    return None

def check_for_button(locator):
    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return button
    except ex.TimeoutException:
        return None

def check_for_button_by_id(locator):
    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, locator)))
        return button
    except ex.TimeoutException:
        return None

def click_on_button_by_xpath(driver, locator):
    successful = True
    page_clickable = check_by_xpath(driver, locator)
    if page_clickable and page_clickable.is_displayed():
        try:
            driver.execute_script("arguments[0].click();", page_clickable)
            time.sleep(1)
        except:
            successful = False
    else:
        successful = False
    return successful

def get_last_question_page(list_items):
    last_item = list_items[-1]
    onclick_value = last_item.get_attribute("onclick")
    if onclick_value:
        start_index = onclick_value.find("window.location='") + len("window.location='")
        end_index = onclick_value.find("'", start_index)
        window_location = onclick_value[start_index:end_index]
        page = f"https://web.simple-mmo.com{window_location}"
        return page

    return None

def get_list_of_questions():
    ul_element = check_by_xpath(driver, "//ul[@class='divide-y divide-gray-200 dark:divide-gray-800']")
    if not ul_element:
        print("Not working")
        return

    list_items = ul_element.find_elements(By.TAG_NAME, "li")
    visible_list_items = []
    for item in list_items:
        if item.is_displayed():
            visible_list_items.append(item)

    return visible_list_items

def do_questions():
    update_status("Going to questions page")
    driver.get("https://web.simple-mmo.com/quests/viewall?status=not_completed")
    time.sleep(3)
    
    list_items = get_list_of_questions()
    if not list_items:
        return

    page_to_go = get_last_question_page(list_items)
    if not page_to_go:
        print("Couldn't find page")
        return

    driver.get(page_to_go)
    time.sleep(3)

    dd_element = check_by_xpath(driver, "(//dd[@class='mt-1 text-sm sm:text-3xl font-semibold text-gray-900'])[3]")
    how_many_left_to_do = 0
    if dd_element:
        counts = dd_element.text.split()
        current_count = int(counts[0])
        total_count = int(counts[2])
        how_many_left_to_do = total_count - current_count
   
    quest_points_element = check_by_xpath(driver, "//span[@x-text='$store.quest_points']")
    quest_points = int(quest_points_element.text)
    times_clicked_perform_question = 0
    while how_many_left_to_do > 0 and quest_points > 0:
            update_status(f"Doing Questions. Quest Points Remaining: {quest_points}. Times clicked Perform Quest: {times_clicked_perform_question}")
            click_on_button_by_xpath(driver, "//button[contains(text(), 'Perform Quest')]")
            while True:
                afk_check = check_for_link(driver, "Press here to verify")
                if afk_check:
                    driver.get("https://web.simple-mmo.com/travel")
                    break

                can_interact = check_for_button("//button[contains(text(), 'Perform Quest')]")
                if can_interact.is_enabled():
                    can_interact.click()
                    times_clicked_perform_question += 1
                    how_many_left_to_do -= 1
                    quest_points -= 1
                    break

    if quest_points > 0:
        repeat_quests = True

    driver.get("https://web.simple-mmo.com/travel")
    time.sleep(1)

def attack_mobs(driver, battle_arena):
    if not battle_arena:
        attack = check_for_link(driver, "Attack")
        if not attack:
            return
       
        attack.click()
        time.sleep(1)
        attacks_done = 0
        while True:
            update_status(f"Attacking mob while Travelling, mob was attacked: {attacks_done} times")
            attacked = click_on_button_by_xpath(driver, "//button[contains(text(), 'Attack')]")
            attacks_done += 1
            afk_check = check_for_link(driver, "Press here to verify")
            if afk_check:
                driver.get("https://web.simple-mmo.com/travel")
                break
            end_battle = check_for_link(driver, "End Battle")
            if end_battle and end_battle.is_displayed():
                action_map["Attack"] += 1
                driver.get("https://web.simple-mmo.com/travel")
                break

    if battle_arena:
        mobs_killed = 0
        attacks_done = 0
        while True:
            update_status(f"Attacking mobs in Battle Arena. Mobs killed: {mobs_killed}. Attacks on current mob: {attacks_done}")
            attacked = click_on_button_by_xpath(driver, "//button[contains(text(), 'Attack')]")
            attacks_done += 1
            afk_check = check_for_link(driver, "Press here to verify")
            if afk_check:
                driver.get("https://web.simple-mmo.com/travel")
                break
            if not attacked:
                continue

            generate_another_enemy = check_by_xpath(driver, "//button[contains(text(), 'Quick generate another NPC')]")
            if generate_another_enemy and generate_another_enemy.is_enabled() and generate_another_enemy.is_displayed():
                action_map["Battle Arena"] += 1
                mobs_killed += 1
                attacks_done = 0
                generate_another_enemy.click()
                time.sleep(1)
                continue

            end_battle = check_for_link(driver, "End Battle")
            if end_battle:
                action_map["Battle Arena"] += 1
                driver.get("https://web.simple-mmo.com/travel")
                break

def battle_in_arena(driver):
    driver.get("https://web.simple-mmo.com/battle/arena")
    time.sleep(4)

    energy = check_by_xpath(driver, "//span[contains(@class, 'text-indigo-600 font-semibold')]")
    if energy:
        if int(energy.text) <= 0:
            print("No energy to do battle arena")
            driver.get("https://web.simple-mmo.com/travel")
            return

    went_to_generate_enemy = click_on_button_by_xpath(driver, '//button[contains(@class, "inline-flex") and contains(@class, "items-center") and contains(@class, "rounded-md") and contains(@class, "border") and contains(@class, "border-gray-300") and contains(@class, "bg-white") and contains(@class, "px-3") and contains(@class, "py-2") and contains(@class, "text-sm") and contains(@class, "font-medium") and contains(@class, "leading-4") and contains(@class, "text-gray-700") and contains(@class, "shadow-sm") and contains(@class, "hover:bg-gray-50") and contains(@class, "focus:outline-none") and contains(@class, "focus:ring-2") and contains(@class, "focus:ring-indigo-500") and contains(@class, "focus:ring-offset-2")]')
    if not went_to_generate_enemy:
        print("Generate enemy wasnt clicked")
        driver.get("https://web.simple-mmo.com/travel")
        return

    generated_enemy = click_on_button_by_xpath(driver, '//button[(text())="Generate"]')
    if not generated_enemy:
        print("Couldn't generate enemy")
        driver.get("https://web.simple-mmo.com/travel")
        return

    battle_enemy = click_on_button_by_xpath(driver, '//button[(text())="Battle"]')
    if not battle_enemy:
        print("Couldn't fight enemy")
        driver.get("https://web.simple-mmo.com/travel")
        return

    battle_arena = True
    attack_mobs(driver, battle_arena)

def pause_script_until_continued():
    input_text = ''
    print("Enter !continue in discord channel to continue script")
    send_discord_message("Enter !continue to continue script")
    while True:
        time.sleep(1)
        with open('shared_variable.txt', 'r+') as f:
            input_text = f.read()
            if input_text.lower() == "continue":
                f.seek(0)
                f.truncate()
                f.write("stop")
                print("Stop written")
                break

    print("Continuing with the script...")
    send_discord_message("Continuing with the script...")

def send_discord_message(message):
    webhook_url = 'https://discordapp.com/api/webhooks/1097153473600028672/-4awOctKw8eNFDF-PPMiI7bL6yo5e6d2nxQYXcffXsH9luzYw7BvXX4B7ciN4aDAV5-b'
    webhook = dc.DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

def confirm_not_afk(driver, text):
    confirmation = check_for_link(driver, text)
    if confirmation:
        time_played_since_start = time_played()
        message = "@vytcka#7550 Please do AFK verification! Script is paused till you do it.\nLink: https://web.simple-mmo.com/i-am-not-a-bot?new_page=true \n"
        message += f"Time played: {time_played_since_start}\n"
        for action, count in action_map.items():
            message += f"Action: {action}, Count: {count}\n"
        send_discord_message(message)
        pause_script_until_continued()

def sleep_for_random_time(start_seconds, end_seconds):
    sleep_time = random.uniform(start_seconds, end_seconds)
    time.sleep(sleep_time)

def take_steps(driver):
    try:
        update_status("Taking steps")
        take_step_button_clickable = check_by_xpath(driver, "//button[contains(text(), 'Take a step')]")
        sleep_for_random_time(0.1, 1.6)
        if take_step_button_clickable.is_enabled():
            take_step_button_clickable.click()
            action_map["Step"] += 1
            time.sleep(1)
    except ex.NoSuchElementException:
        time.sleep(1)

def press_gather_button_until_done(action):
    while True:
        afk_check = check_for_link(driver, "Press here to verify")
        if afk_check:
            driver.get("https://web.simple-mmo.com/travel")
            time.sleep(1)
            break
        button = check_for_button_by_id("crafting_button")
        if button:
            action_map[action] += 1
            if "close" in button.text.lower():
                button.click()
                break
            else:
                button.click()

def gather_materials(driver, action):
    try:
        action_button = check_by_xpath(driver, f"//button[contains(text(), '{action}')]")
        if action_button:
            level_too_low = check_by_xpath(driver, "//small[contains(text(), \"Your skill level isn't high enough\")]")
            if(level_too_low):       
                return

            update_status(f"Gathering materials, Action: {action}")
            action_button.click()
            time.sleep(3)
            press_gather_button_until_done(action)
            time.sleep(1)
    except ex.NoSuchElementException:
        pass

def verifyCloudFlareCaptcha(driver):
    while True:
        try:
            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "spinner-icon")))
            if checkbox:
                checkbox.click()
                break
        except ex.TimeoutException:
            print("Timeout")
        

def login(driver, email, password):
    print("Waiting for CloudFlare verification")
    attempts = 0
    while True:
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys(email)
            break
        except ex.TimeoutException:
            pass

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    login_button.click()

    print("Logged in")

    driver.get("https://web.simple-mmo.com/travel")

def read_from_file():
    file_path = os.getcwd() + "\credentials.txt"
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            email = lines[0].strip()
            password = lines[1].strip()
            return email, password

def get_driver(location):
    profile = profiles.Android()
    options = ChromeOptions()
    mydriver = Chrome(profile, options=options, uc_driver=False)
    mydriver.options.add_argument("--headless=new")
    mydriver.options.add_argument("--mute-audio")

    driver = mydriver.start()
    driver.get(location)
    return driver


if __name__ == '__main__':
    update_status("Starting bot")
    subprocess.Popen(['python', './discord_bot.py'])
    driver = get_driver('https://web.simple-mmo.com/login')
    email, password = "vytas.sa1@gmail.com", "Asdf15971"
    login(driver, email, password)
    print("Script will start running now!")
    just_logged_in = True

    while True:
        take_steps(driver)
        confirm_not_afk(driver, "Press here to confirm your existence")
        if repeat_quests:
            do_questions()
            repeat_quests = False

        twenty_five_minutes_has_passed = time.time() - battle_arena_question_timer >= 1500
        if twenty_five_minutes_has_passed or just_logged_in:
            battle_in_arena(driver)
            battle_arena_question_timer = time.time()
            do_questions()
            just_logged_in = False

        wants_to_battle_in_arena = False
        attack_mobs(driver, wants_to_battle_in_arena)
        gather_materials(driver, "Grab")
        gather_materials(driver, "Salvage")
        gather_materials(driver, "Catch")
        gather_materials(driver, "Chop")
        gather_materials(driver, "Mine")
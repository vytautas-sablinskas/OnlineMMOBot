from Managers.Navigation.PageNavigator import PageNavigator
from Managers.Files.FileManager import FileManager
from Constants.FilePaths import FilePaths

class ItemManager:
    def __init__(self):
        self.commonItems = {}
        self.uncommonItems = {}
        self.rareItems = {}
        self.eliteItems = {}
        self.epicItems = {}
        self.legendaryItems = {}
        self.exoticItems = {}
        self.celestialItems = {}

    def add_item_by_rarity(self, item_rarity, item_to_append, chrome_handler, element_handler):
        switcher = {
            "common-item": self.commonItems,
            "uncommon-item": self.uncommonItems,
            "rare-item": self.rareItems,
            "elite-item": self.eliteItems,
            "epic-item": self.epicItems,
            "legendary-item": self.legendaryItems,
            "exotic-item": self.exoticItems,
            "celestial-item": self.celestialItems
        }

        item_dict = switcher.get(item_rarity, None)
        if item_dict is None:
            print("Such item rarity is not in our list!")
            return
        
        item_dict[item_to_append] = item_dict.get(item_to_append, 0) + 1
        FileManager.update_item_count(
            file_path=FilePaths.ITEMS_FOUND_BY_RARITY.value.format(item_rarity),
            item_name=item_to_append,
            new_count=item_dict[item_to_append]
        )
        PageNavigator.go_to_travel_page(chrome_handler, element_handler)
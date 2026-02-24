from BaseClasses import ItemClassification

from .constants import *
from .data_rooms import rooms
from .locations import ROOM_MULTIPLIER

def create_location_id(room_name: str):
    return rooms[room_name][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + get_room_location_count(room_name)

def get_room_location_count(room_name: str) -> int:
    rooms[room_name].setdefault(LOCATION_COUNT_KEY, 0)
    count = rooms[room_name][LOCATION_COUNT_KEY]
    rooms[room_name][LOCATION_COUNT_KEY] = count + 1
    return count

trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_ROOM_COUNT: 45}
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: create_location_id("Workshop"),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: [
                "Burning Glass",
                "Detector Shovel",
                "Dowsing Rod",
                "Electromagnet",
                "Jack Hammer",
                "Lucky Purse",
                "Pick Sound Amplifier",
                "Power Hammer",
            ]
        }
    },
    "Trophy of Drafting": {
        LOCATION_ID_KEY: create_location_id("Mail Room"),
        LOCATION_ROOM_KEY: "Mail Room",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_ITEM_COUNTS: {
                "D Piece": 20,
            }
        }
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: create_location_id("Showroom"),
        LOCATION_ROOM_KEY: "Showroom",
        LOCATION_REQUIREMENTS: {}
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: create_location_id("Room 46"),
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_REQUIREMENTS: {}
    },
    "Bullesye Trophy": {
        LOCATION_ID_KEY: create_location_id("Billiard Room"),
        LOCATION_ROOM_KEY: "Billiard Room",
        LOCATION_REQUIREMENTS: {}
    },
    "A Logical Trophy": {
        LOCATION_ID_KEY: create_location_id("Parlor"),
        LOCATION_ROOM_KEY: "Parlor",
        LOCATION_REQUIREMENTS: {}
    },
    "Trophy 8": {
        LOCATION_ID_KEY: create_location_id("Room 8"),
        LOCATION_ROOM_KEY: "Room 8",
        LOCATION_REQUIREMENTS: {}
    },
    "Explorer's Trophy": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: { LOCATION_REQUIREMENT_TYPE_HAS_ALL_ROOMS: True }
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_REGIONS_ACCESS: [
                "Orinda Aries Sanctum",
                "Fenn Aries Sanctum",
                "Arch Aries Sanctum",
                "Eraja Sanctum",
                "Corarica Sanctum",
                "Mora Jai Sanctum",
                "Verra Sanctum",
                "Nuance Sanctum",
            ]
        }
    },
    "Diploma Trophy": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_REGIONS_ACCESS: [
                "Schoolhouse",
                "Classroom 1",
                "Classroom 2",
                "Classroom 3",
                "Classroom 4",
                "Classroom 5",
                "Classroom 6",
                "Classroom 7",
                "Classroom 8",
                "Classroom Exam",
            ]
        }
    }

    # For if we add new game+ trophies, mostly here for completeness sake
    # "Dare Bird Trophy": {
    #     LOCATION_ID_KEY: create_location_id("Room 46"),
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Cursed Trophy": {
    #     LOCATION_ID_KEY: create_location_id("Room 46"),
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Day One Trophy": {
    #     LOCATION_ID_KEY: create_location_id("Room 46"),
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Trophy of Speed": {
    #     LOCATION_ID_KEY: create_location_id("Room 46"),
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # }
    # "Trophy of Trophies": {
    #     LOCATION_ID_KEY: create_location_id("Trophy Room"),
    #     LOCATION_ROOM_KEY: "Trophy Room",
    #     LOCATION_REQUIREMENTS: {
    #         LOCATION_REQUIREMENT_TYPE_HAS_LOCATIONS_ACCESS: [
    #             "Full House Trophy",
    #             "Trophy of Invention",
    #             "Trophy of Drafting",
    #             "Trophy of Wealth",
    #             "Inheritance Trophy",
    #             "Bullesye Trophy",
    #             "A Logical Trophy",
    #             "Trophy 8",
    #             "Explorer's Trophy",
    #             "Trophy of Sigils",
    #             "Diploma Trophy",
    #             "Dare Bird Trophy",
    #             "Cursed Trophy",
    #             "Day One Trophy",
    #             "Trophy of Speed"
    #         ]
    #     }
    # }
}

safes_and_small_gates = {
    "Boudoir Safe": {
        LOCATION_ID_KEY: create_location_id("Boudoir"),
        LOCATION_ROOM_KEY: "Boudoir",
    },
    "Drafting Studio Safe": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: ["MAGNIFYING GLASS"]}
    },
    "Drawing Room Safe": {
        LOCATION_ID_KEY: create_location_id("Drawing Room"),
        LOCATION_ROOM_KEY: "Drawing Room",
    },
    "Office Safe": {
        LOCATION_ID_KEY: create_location_id("Office"),
        LOCATION_ROOM_KEY: "Office",
    },
    "Study Safe": {
        LOCATION_ID_KEY: create_location_id("Study"),
        LOCATION_ROOM_KEY: "Study",
    },
    "Underpass Gate": {
        LOCATION_ID_KEY: create_location_id("Underpass"),
        LOCATION_ROOM_KEY: "Underpass",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: ["Boiler Room"]}
    },
    "Shelter Safe": {
        LOCATION_ID_KEY: create_location_id("Shelter"),
        LOCATION_ROOM_KEY: "Shelter",
    },
    "Orchard Gate": {
        LOCATION_ID_KEY: create_location_id("Campsite"),
        LOCATION_ROOM_KEY: "Campsite",
    }
}

aries_court_moria_jia_boxes = {
    f"Aries Court Moria Jia Box {n}": {
        LOCATION_ID_KEY: create_location_id("Aries Court"),
        LOCATION_ROOM_KEY: "Aries Court",
    } for n in range(1, 9)
}

moria_jia_boxes = {
    "Master Bedroom Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Master Bedroom"),
        LOCATION_ROOM_KEY: "Master Bedroom",
    },
    "Closed Exhbit Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Closed Exhibit"),
        LOCATION_ROOM_KEY: "Closed Exhibit",
    },
    "Underpass Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Underpass"),
        LOCATION_ROOM_KEY: "Underpass",
    },
    "Tomb Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Tomb"),
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Trading Post Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Trading Post"),
        LOCATION_ROOM_KEY: "Trading Post",
    },
    "Tunnel Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Tunnel"),
        LOCATION_ROOM_KEY: "Tunnel",
    },
    "Solaium Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Solarium"),
        LOCATION_ROOM_KEY: "Solarium",
    },
    "Lost And Found Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Lost And Found"),
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Throne of the Blue Prince Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Throne Room"),
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: [
            "CROWN",
            "ROYAL SCEPTER",
            "CURSED EFFIGY",
        ]}
    },
    "Arch Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Arch Aries Sanctum"),
        LOCATION_ROOM_KEY: "Arch Aries Sanctum",
    },
    "Corarica Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Corarica Sanctum"),
        LOCATION_ROOM_KEY: "Corarica Sanctum",
    },
    "Eraja Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Eraja Sanctum"),
        LOCATION_ROOM_KEY: "Eraja Sanctum",
    },
    "Fenn Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Fenn Aries Sanctum"),
        LOCATION_ROOM_KEY: "Fenn Aries Sanctum",
    },
    "Mora Jai Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Mora Jai Sanctum"),
        LOCATION_ROOM_KEY: "Mora Jai Sanctum",
    },
    "Orinda Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Orinda Aries Sanctum"),
        LOCATION_ROOM_KEY: "Orinda Aries Sanctum",
    },
    "Verra Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Verra Sanctum"),
        LOCATION_ROOM_KEY: "Verra Sanctum",
    },
    "Nuance Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: create_location_id("Nuance Sanctum"),
        LOCATION_ROOM_KEY: "Nuance Sanctum",
    }
} | aries_court_moria_jia_boxes
# not adding atelier boxes, since they are bascially already at the latest goal

drafting_studio_additions = {
    "Dovecote Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "The Kennel Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Clock Tower Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Classroom Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Solarium Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Dormitory Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Vestibule Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Casino Floorplan": {
        LOCATION_ID_KEY: create_location_id("Drafting Studio"),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
}

found_floorplans = {
    "Planetarium Floorplan": {
        LOCATION_ID_KEY: create_location_id("Observatory"),
        LOCATION_ROOM_KEY: "Observatory",
    },
    "Mechanarium Floorplan": {
        LOCATION_ID_KEY: create_location_id("Rotating Gear"),
        LOCATION_ROOM_KEY: "Rotating Gear",
    },
    "Treasure Trove Floorplan": {
        LOCATION_ID_KEY: create_location_id("Underpass"),
        LOCATION_ROOM_KEY: "Underpass",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: ["Boiler Room"]}
    },
    "Throne Room Floorplan": {
        LOCATION_ID_KEY: create_location_id("Orindian Ruins"),
        LOCATION_ROOM_KEY: "Orindian Ruins",
    },
    "Tunnel Floorplan": {
        LOCATION_ID_KEY: create_location_id("Tunnel Area Past Crates"),
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
    },
    "Conservatory Floorplan": {
        LOCATION_ID_KEY: create_location_id("Campsite"),
        LOCATION_ROOM_KEY: "Campsite",
    },
    "Lost And Found Floorplan": {
        LOCATION_ID_KEY: create_location_id("Basement"),
        LOCATION_ROOM_KEY: "Basement",
    },
    "Closed Exhibit Floorplan": {
        LOCATION_ID_KEY: create_location_id("Study"),
        LOCATION_ROOM_KEY: "Study",
    }
}

# Mirror Room Floorplan Duplicates?

floorplans = drafting_studio_additions | found_floorplans

gift_shop_items = {
    "Gift Shop - Mt. Holly Tee": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Lunch Box": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Trunks": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Bird Plushie": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Blue Tents": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_REQUIREMENT_TYPE_COUNT_LOCATIONS_ACCESS: (trophies.keys(), 8)
    },
    "Gift Shop - Cursed Coffers": {
        LOCATION_ID_KEY: create_location_id("Gift Shop"),
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: ["Library"],
    }
}

bookshop_items = {
    "Bookshop - The History of Orindia (1st ed.) ": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - A New Clue": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - The Curse of Black Bridge": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Realm & Rune": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 4": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 5": {
        LOCATION_ID_KEY: create_location_id("Bookshop"),
        LOCATION_ROOM_KEY: "Bookshop",
    },
}

shop_items = gift_shop_items | bookshop_items

upgrade_disks = {
    "Upgrade Disk - Offic": {
        LOCATION_ID_KEY: create_location_id("Office"),
        LOCATION_ROOM_KEY: "Office",
    },
    "Upgrade Disk - Morning Room": {
        LOCATION_ID_KEY: create_location_id("Morning Room"),
        LOCATION_ROOM_KEY: "Morning Room",
    },
    "Upgrade Disk - Her Ladyship's Chambers": {
        LOCATION_ID_KEY: create_location_id("Her Ladyship's Chambers"),
        LOCATION_ROOM_KEY: "Her Ladyship's Chambers",
    },
    "Upgrade Disk - Commissary": {
        LOCATION_ID_KEY: create_location_id("Commissary"),
        LOCATION_ROOM_KEY: "Commissary",
    },
    "Upgrade Disk - Garage": {
        LOCATION_ID_KEY: create_location_id("Garage"),
        LOCATION_ROOM_KEY: "Garage",
    },
    "Upgrade Disk - Great Hall": {
        LOCATION_ID_KEY: create_location_id("Great Hall"),
        LOCATION_ROOM_KEY: "Great Hall",
    },
    "Upgrade Disk - Vault": {
        LOCATION_ID_KEY: create_location_id("Vault"),
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: ["VAULT KEY 304"]
    },
    "Upgrade Disk - Trading Post Dynamite": {
        LOCATION_ID_KEY: create_location_id("Trading Post"),
        LOCATION_ROOM_KEY: "Trading Post",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: ["Burning Glass", "TORCH"]
    },
    "Upgrade Disk - Freezer": {
        LOCATION_ID_KEY: create_location_id("Freezer"),
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: [
            "Furnace",
            "Burning Glass",
            "TORCH",
            "Power Hammer",
        ]
    },
    "Upgrade Disk - Tomb": {
        LOCATION_ID_KEY: create_location_id("Tomb"),
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Upgrade Disk - The Foundation": {
        LOCATION_ID_KEY: create_location_id("The Foundation"),
        LOCATION_ROOM_KEY: "The Foundation",
    },
    "Upgrade Disk - Abandoned Mine": {
        LOCATION_ID_KEY: create_location_id("Abandoned Mine"),
        LOCATION_ROOM_KEY: "Abandoned Mine",
    },
    "Upgrade Disk - Lost And Found": {
        LOCATION_ID_KEY: create_location_id("Lost And Found"),
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Upgrade Disk - Mechanarium": {
        LOCATION_ID_KEY: create_location_id("Mechanarium"),
        LOCATION_ROOM_KEY: "Mechanarium",
    },
    "Upgrade Disk - Archives": {
        LOCATION_ID_KEY: create_location_id("Archives"),
        LOCATION_ROOM_KEY: "Archives",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: ["CABINET KEY 1"] # I think this is the right key?
    },
    "Upgrade Disk - Trading Post Trade": {
        LOCATION_ID_KEY: create_location_id("Trading Post"),
        LOCATION_ROOM_KEY: "Trading Post",
    },
}

vault_keys = {
    "Vault Key 149": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: [
            "Attic", 
            "Rumpus Room", 
            "Security", 
            "Trophy Room", 
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ]
    },
    "Vault Key 233": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: [
            "Office",
            "Sauna",
            "Wine Cellar",
            "Lavatory",
            "Morning Room",
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ]
    },
    "Vault Key 304": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: [
            "Conference Room",
            "Her Ladyship's Chambers",
            "Walk-in Closet",
            "Hovel",
            "Spare Room",
            "Drawing Room",
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ]
    },
    "Vault Key 370": {
        LOCATION_ID_KEY: create_location_id("Entrance Hall"), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY: [
            "Lost And Found",
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ]
    }
}

sanctum_keys = {
    "Sanctum Key - Room 46": {
        LOCATION_ID_KEY: create_location_id("Room 46"),
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Sanctum Key - Vault": {
        LOCATION_ID_KEY: create_location_id("Vault"),
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL: ["VAULT KEY 370"]
    },
    "Sanctum Key - Clock Tower": {
        LOCATION_ID_KEY: create_location_id("Clock Tower"),
        LOCATION_ROOM_KEY: "Clock Tower",
    },
    "Sanctum Key - Reservoir Bottom": {
        LOCATION_ID_KEY: create_location_id("Reservoir Bottom"),
        LOCATION_ROOM_KEY: "Reservoir Bottom",
    },
    "Sanctum Key - Throne Room": {
        LOCATION_ID_KEY: create_location_id("Throne Room"),
        LOCATION_ROOM_KEY: "Throne Room",
    },
    "Sanctum Key - Safehouse": {
        LOCATION_ID_KEY: create_location_id("Safehouse"),
        LOCATION_ROOM_KEY: "Safehouse",
    },
    "Sanctum Key - Music Room": {
        LOCATION_ID_KEY: create_location_id("Music Room"),
        LOCATION_ROOM_KEY: "Music Room",
    },
    "Sanctum Key - Mechanarium": {
        LOCATION_ID_KEY: create_location_id("Mechanarium"),
        LOCATION_ROOM_KEY: "Mechanarium",
    }
}

file_cabinet_keys = {
    "File Cabinet Key - Patio": {
        LOCATION_ID_KEY: create_location_id("Patio"),
        LOCATION_ROOM_KEY: "Patio",
    },
    "File Cabinet Key - Laundry Room": {
        LOCATION_ID_KEY: create_location_id("Laundry Room"),
        LOCATION_ROOM_KEY: "Laundry Room",
    },
    "File Cabinet Key - Tunnel Area Past Crates": {
        LOCATION_ID_KEY: create_location_id("Tunnel Area Past Crates"),
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
    },
}

keys = vault_keys | sanctum_keys | file_cabinet_keys



# TODO-1 add locations for other stuff later.
# "Entrance Hall East Vase": rooms["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 0,
# "Entrance Hall West Vase": rooms["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,

# One-time Allowance Tokens

# Cursed Coffers
# Chapel Offering

# Gas Valves
# Sundial

other_locations = trophies | safes_and_small_gates | moria_jia_boxes | floorplans | shop_items | upgrade_disks | keys
    
from BaseClasses import ItemClassification


from .constants import *

trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: 100_001,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: {LOCATION_REQUIREMENT_TYPE_ROOM_COUNT: 45}
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: 100_002,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_ITEMS: [
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
        LOCATION_ID_KEY: 100_003,
        LOCATION_ROOM_KEY: "Mail Room",
        LOCATION_REQUIREMENTS: {
            LOCATION_REQUIREMENT_TYPE_HAS_ITEM_COUNTS: {
                "D Piece": 20,
            }
        }
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: 100_004,
        LOCATION_ROOM_KEY: "Showroom",
        LOCATION_REQUIREMENTS: {}
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: 100_005,
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_REQUIREMENTS: {}
    },
    "Bullesye Trophy": {
        LOCATION_ID_KEY: 100_006,
        LOCATION_ROOM_KEY: "Billiard Room",
        LOCATION_REQUIREMENTS: {}
    },
    "A Logical Trophy": {
        LOCATION_ID_KEY: 100_007,
        LOCATION_ROOM_KEY: "Parlor",
        LOCATION_REQUIREMENTS: {}
    },
    "Trophy 8": {
        LOCATION_ID_KEY: 100_008,
        LOCATION_ROOM_KEY: "Room 8",
        LOCATION_REQUIREMENTS: {}
    },
    "Explorer's Trophy": {
        LOCATION_ID_KEY: 100_009,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_REQUIREMENTS: { LOCATION_REQUIREMENT_TYPE_HAS_ALL_ROOMS: True }
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: 100_010,
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
        LOCATION_ID_KEY: 100_011,
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

    # For if we add new game trophies, mostly here for completeness sake
    # "Dare Bird Trophy": {
    #     LOCATION_ID_KEY: 100_0xx,
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Cursed Trophy": {
    #     LOCATION_ID_KEY: 100_0xx,
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Day One Trophy": {
    #     LOCATION_ID_KEY: 100_0xx,
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # },
    # "Trophy of Speed": {
    #     LOCATION_ID_KEY: 100_0xx,
    #     LOCATION_ROOM_KEY: "Room 46",
    #     LOCATION_REQUIREMENTS: {}
    # }
    # "Trophy of Trophies": {
    #     LOCATION_ID_KEY: 100_0xx,
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

from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.data_rooms import rooms, core_rooms

class TestNoDraftSanity(BluePrinceTestBase):
    options = {
        "room_draft_sanity": False,
        "goal_type": GoalType.option_room46,
    }

    def test_all_starting_room_items(self) -> None:
        for room in rooms:
            if room in core_rooms:
                continue
            self.assertTrue(self.multiworld.state.has(room, self.player))
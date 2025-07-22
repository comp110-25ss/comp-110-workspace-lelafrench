"""File to define River class."""

from exercises.ex05.fish import Fish
from exercises.ex05.bear import Bear  # do this so we can store Bear and Fish numbers


class River:
    day: int  # which day of the river lifecycle you're modifying
    bears: list[Bear]  # store Bear population
    fish: list[Fish]  # store Fish population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove any Fish with ages older than 3 and Bears older than 5"""
        list_fish: list[Fish] = []  # make this blank so adding Fish, not removing them
        for animal in self.fish:  # iterate thru Fish list
            if animal.age <= 3:
                list_fish.append(
                    animal
                )  # pull ones that are surviving and add to new list
        list_bears: list[Bear] = []
        for animal in self.bears:
            if animal.age >= 5:
                list_bears.append(animal)
        self.fish = list_fish  # match Fish population equivalent to surviving Fish
        self.bears = list_bears
        return None

    def bears_eating(self):
        """Modify river when Bears eat Fish"""
        for animal in self.bears:
            if len(self.fish) >= 5:  # len b/c number of Fish
                self.remove_fish(3)
                animal.eat(3)  # give each Bear that eats 3 fish
        return None

    def check_hunger(self):
        """Remove starving Bears from the river"""
        list_bears: list[Bear] = []
        for animal in self.bears:
            if animal.hunger_score >= 0:  # if they are breaking even or not hungry
                list_bears.append(animal)  # add to new lsit
        self.bears = list_bears
        return None

    def repopulate_fish(self):
        """Repopulate Fish population thanks to reproduction"""
        idx: int = 0
        add_fish: Fish = Fish()
        while idx < len(self.fish):
            if idx % 2 == 0:  # counts every 2 fish (I think)
                self.fish.append(add_fish)
                self.fish.append(add_fish)
                self.fish.append(add_fish)
                self.fish.append(add_fish)  # add 4 new Fish
            idx += 1
        return None

    def repopulate_bears(self):
        """Repopulate Bear population thanks to reproduction"""
        idx: int = 0
        add_bear: Bear = (
            Bear()
        )  # new Bear instance cause I couldn't figure anything else out
        while idx < len(self.bears):
            if idx % 2 == 0:
                self.bears.append(add_bear)
            idx += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(
            f"Fish population: {len(self.fish)}"
        )  # use len b/c otherwise prints a weird list value
        print(
            f"Bear population: {len(self.bears)}"
        )  # len of Bear and Fish lists = num of Bears and Fish
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Run the one_river_week method 7 times"""
        count: int = 0
        while count < 7:  # repeat 7 times
            self.one_river_day
            count += 1
        print(count)

    def remove_fish(self, amount: int) -> None:
        """Remove a given amount of Fish from the river"""
        count: int = 0
        while count < amount:  # iterate thru until reaches amount
            self.fish.pop(0)
            count += 1

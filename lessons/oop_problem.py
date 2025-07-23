"""OOP practice from final review general question #6."""


class TA:
    semester_pay: int
    hours_per_week: int
    title: str

    def __init__(self, title: str):
        self.title = title
        if self.title == "COMP 110 TA":
            self.hours_per_week = 5
            self.semester_pay = 1000
        else:
            self.hours_per_week = 5
            self.semester_pay = 0

    def todo_list(self, todo_list: dict[str, bool]) -> dict[str, bool]:
        return todo_list

    def check_off(self, task: str, todo_list: dict[str, bool]) -> dict[str, bool]:
        if task in todo_list:
            todo_list[task] = True
        return todo_list

    def change_class(self, new_title: str) -> "TA":
        return TA(new_title)


# 6a
bio_ta: TA = TA("Bio 101 TA")

# 6b
comp_ta: TA = bio_ta.change_class("Comp 110 TA")

# 6c
my_tasks: dict[str, bool] = {
    "4 hours of OH": False,
    "1 hour of AH": False,
    "grade quiz question 6.1": False,
}
comp_todo = comp_ta.todo_list(my_tasks)

# 6d
comp_todo = comp_ta.check_off("1 hour of AH", my_tasks)

# 6e
comp_todo = comp_ta.check_off("4 hours of OH", my_tasks)

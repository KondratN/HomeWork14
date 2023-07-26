import datetime


class Project:
    def __init__(self, name, name_programmers):
        self.name = name
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today() + datetime.timedelta(days=7)
        self.name_programmers = name_programmers

    def __str__(self):
        return f"Название проекта: {self.name}\nДата начала: {self.start_date}\nДата окончания: {self.end_date}\n" \
               f"Программисты: {self.name_programmers}"

    def add_programmer(self, programmer):
        if len(self.name_programmers) < 4:
            self.name_programmers.append(programmer)
            print(f"Программист {programmer} добавлен в список программистов")
        else:
            print("Слишком много программистов")

    def del_programmer(self, programmer):
        if programmer in self.name_programmers:
            self.name_programmers.remove(programmer)
            print(f"Программист {programmer} удален из списка программистов")
        else:
            print("Программиста нет в списке")

    def add_end_date(self, date):
        self.end_date = self.end_date + datetime.timedelta(days=date)
        print('Вы продлили дату окончания проекта на', self.end_date)


p1 = Project('Project 1', ['Programmer 1', 'Programmer 2', 'Programmer 3', 'Programmer 4'])
print(p1)

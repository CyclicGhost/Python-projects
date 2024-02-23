class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        
    def consume_vacation(self, vacation_consumed):
        self.vacation_consumed = vacation_consumed
        self.remaining_vacation_days -= vacation_consumed
        
    def get_vacation_details(self):
        return self.remaining_vacation_days
    
 # Сюда добавьте методы consume_vacation и get_vacation_details
# Пример использования класса:
employee = Employee('Роберт', 'Крузо', 'м')
employee2 = Employee('Великий', 'Император', 'м')
employee.consume_vacation(7)
employee2.consume_vacation(28)
print(employee.get_vacation_details())
print(employee2.get_vacation_details())
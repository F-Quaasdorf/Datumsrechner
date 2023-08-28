import re
import datetime


class DatePreparator:
    def __init__(self):
        try:
            self.date_input()
            self.date_create()
            self.date_check()
            self.day_diff_count()
        
        except AttributeError as attr_err:
            print("\t| Fehler bei der Eingabe.\n\t| ERROR:", attr_err)
        
        except ValueError as val_err:
            print("\t| Fehler bei der Eingabe.\n\t| ERROR:", val_err)

    def date_input(self):
        user_input = input("Bitte geben Sie das Datum im Format 'tt.mm.jjjj' ein:\n> ")        
        self.user_date = user_input        
    
    def date_create(self):
        split_date = re.search(r"([0-9]+).([0-9]+).([0-9]+)", self.user_date)
        d = split_date.group(1)
        m = split_date.group(2)
        y = split_date.group(3)
        
        # Creates the Gregorian date via datetime.
        split_date = datetime.date(int(y), int(m), int(d))
        
        self.conv_date = split_date
        self.year = y
        
        return self.conv_date
    
    def date_check(self):
        # Setting the date the Gregorian calendar was implemented.
        greg_reform = datetime.date(1582, 10, 15)
       
        if self.conv_date < greg_reform:
            return True
             
    def weekday(self, given_date):
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
                   "Freitag", "Samstag", "Sonntag"]
        
        day = given_date.weekday()
        print("Wochentag:", days[day])
    
    def day_diff_count(self):
        # The difference between the two calendars is 10 days in the 16th century.
        jul_diff = 10
        
        # For every century the difference between the two calendars increases by 1,
        # unless the century can be divided by 400.
        day_adj = int(self.year[0:2])
        while day_adj > 15:
            if day_adj % 4 == 0:
                day_adj -= 1
            else:
                day_adj -= 1
                jul_diff += 1
                
        # Prepares the days for substraction in the datetime-module.
        jul_day = datetime.timedelta(days=jul_diff)
        self.jul_day = jul_day
        return self.jul_day    

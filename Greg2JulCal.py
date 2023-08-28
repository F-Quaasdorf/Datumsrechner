from DatePrep import DatePreparator


class GregorianToJulianCalendar(DatePreparator):
    def __init__(self):
        DatePreparator.__init__(self)        
        self.greg2jul()
        
        # Checks the date and continues. Returns a warning if the date took place after 1582.
        if DatePreparator.date_check(self) is True:
            print("\t| Achtung! Der gregorianische Kalender wurde am 15. Oktober 1582 eingeführt.\n"
                  "\t| Datumsangaben vor diesem Tag werden nicht umgerechnet.")
        else:
            DatePreparator.weekday(self, DatePreparator.date_create(self))
            DatePreparator.day_diff_count(self)        
    
    def greg2jul(self):
        try:
            # Subtracts the needed amount of days from the given date.
            self.jul_date = self.conv_date - self.jul_day
            
            # Sets the new Julian date up for printing and prints.
            self.jul_date_res = self.jul_date.strftime("%d.%m.%Y")
            print("Im julianischen Kalender:", self.jul_date_res)
            
            return self.jul_date
        
        except OverflowError as ovflow_err:
            print("\t| Ein Fehler ist bei der Berechnung aufgetreten.\n\t| ERROR:", ovflow_err)

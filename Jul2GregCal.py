from DatePrep import DatePreparator


class JulianToGregorianCalendar(DatePreparator):
    def __init__(self):
        DatePreparator.__init__(self)        
        self.greg2jul()
        
        # Checks the date and continues. Returns a warning for dates before 1582. 
        if DatePreparator.date_check(self) is True:
            print("\t| Achtung! Der gregorianische Kalender wurde am 15. Oktober 1582 eingeführt.\n"
                  "\t| Datumsangaben vor diesem Tag werden nicht umgerechnet.")
        else:
            DatePreparator.weekday(self, self.greg_date)
            DatePreparator.day_diff_count(self)
            
    def greg2jul(self):
        try:
            # adds the needed amount of days from the given date.
            self.greg_date = self.conv_date + self.jul_day
            
            # Sets the new Gregorian date up for printing and prints.
            self.greg_date_res = self.greg_date.strftime("%d.%m.%Y")
            print("Im gregorianischen Kalender:", self.greg_date_res)
            
            return self.greg_date
        
        except OverflowError as ovflow_err:
            print("\t| Ein Fehler ist bei der Berechnung aufgetreten.\n\t| ERROR:", ovflow_err)

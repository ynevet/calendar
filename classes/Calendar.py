from classes.CustomExceptions import *


class Calendar:
    """ A callender of events, has an entry for every event,
        which is a mapping from event name to Date o bject"""

    def __init__(self):
        self.events = {}

    def add_event(self, name, date):
        """ Add a new entry to the callender"""
        self.events[name] = date

    def is_event(self, date):
        """ Check if the given date appears in the callender"""
        return date in self.events.values()

    def get_date(self, name):
        """ Return the date of the given event name"""
        if name not in self.events:
            raise CalendarException("Event does not exits")
        else:
            return self.events[name]

    def get_all_events_in_month(self, month):
        """ Return a dictionary with all the events in the given month
        month is the number of the month """
        return {k: str(v) for k, v in self.events.items() if v.month == month}
        # return filter(lambda k,v: (v.month == month and k==k), self.events.items())
        return filter(lambda v: v.month == month, self.events.values())

        # month_events = {}
        # for name in self.events.keys():
        #    if (self.events[name].month == month):
        #        month_events[name] = self.events[name]

        # return month_events

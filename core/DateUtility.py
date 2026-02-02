from datetime import datetime, timedelta, timezone

import pytz
from pytz import timezone


class DateUtility:

    def set_date_slash(self, day):
        """Date with format: 01/01/2019"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            return use_date.strftime('%d/%m/%Y')
        except TypeError:
            pass

    def set_date_slash_short_year_without_zero(self, day):
        """Date with format: 1/1/19"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            this_date = use_date.strftime('%#m/%#d/%Y')
            return this_date[:-4] + this_date[-2:]
        except TypeError:
            pass

    def set_date_hypen(self, day):
        """Date with format: 01-01-2019"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            return use_date.strftime('%Y-%m-%d')
        except TypeError:
            pass

    def set_date_slash_short_year(self, day):
        """Date with format: 01/01/19"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            this_date = use_date.strftime('%#m/%#d/%Y')
            return this_date[:-4] + this_date[-2:]
        except TypeError:
            pass

    def set_date_short_year(self, day):
        """Date with format: 190828"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            this_date = use_date.strftime('%Y%m%d')
            return this_date[-6:]
        except TypeError:
            pass

    def set_past_date_slash_short_year(self, day):
        """Past Date with format: 01/01/19"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today - timedelta(days=set_date)
            this_date = use_date.strftime('%#m/%#d/%Y')
            return this_date[:-4] + this_date[-2:]
        except TypeError:
            pass

    def set_date_slash_worded(self, day):
        """Past Date with format: Tuesday, January 01, 2019"""
        try:
            set_date = int(day)
            today = datetime.today().date()
            use_date = today + timedelta(days=set_date)
            return use_date.strftime('%A, %B %#d, %Y')
        except TypeError:
            pass

    def set_date_slash_short_year_from_date_string(self, system_date, day):
        """Date with format: 1/1/19"""
        try:
            set_day = int(day)
            clean_date = system_date.replace('/', ' ').replace('19', '2019')
            convert_to_date = datetime.strptime(clean_date, '%m %d %Y').date()
            set_date = convert_to_date + timedelta(days=set_day)
            this_date = set_date.strftime('%#m/%#d/%Y')
            return this_date[:-4] + this_date[-2:]
        except TypeError:
            pass

    def get_current_utc_date_time(self):
        """Date with format: January 1, 2024, 1:11"""
        utc_date_time_now = datetime.now(pytz.utc)
        return utc_date_time_now.strftime('%B %d, %Y, %I:%M').replace(' 0', ' ')

    def get_current_melbourne_date(self):
        """Date with format: 20240112"""
        AEST = pytz.timezone('Australia/Sydney')
        use_date = datetime.now(AEST)
        this_date = use_date.strftime('%d%m%Y')
        return this_date

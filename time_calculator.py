def add_time(start, duration, weekdaystart=''):
    time_start = start.split()[0]
    AM_or_PM_start = start.split()[1]
    AM_or_PM = AM_or_PM_start

    # getting hour and minutes from start time

    hours_start = int(time_start.split(':')[0])
    minutes_start = time_start.split(':')[1]

    # getting hour and minutes from duration

    hours_duration = int(duration.split(':')[0])
    minutes_duration = duration.split(':')[1]

    # Calculate new time
    new_minutes = int(minutes_start) + int(minutes_duration)

    # Hours to add for new time
    hours_add = 0

    # Days to skip

    n = 0

    n_am_it=0
    # Days of the week

    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Calculate new minutes

    if new_minutes >= 60:
        hours_duration += 1
        new_minutes -= 60
        if hours_start==11:
            n_am_it+=1
    if len(str(new_minutes)) < 2:
        new_minutes = '0' + str(new_minutes)

        # Calculate how many 'n days later'

    if hours_duration >= 24:
        n = hours_duration // 24
        hours_add = hours_duration - n * 24
        new_hour = int(hours_start) + hours_add
        n_ampm = (hours_duration // 12)+n_am_it
        if new_hour > 24:
            new_hour -= 24
            n += 1
        if 12 < new_hour <= 24:
            if new_hour == 24 : n += 1 ;
            new_hour -= 12
            n_ampm+=1
        if n_ampm % 2 == 0:
            pass
        if n_ampm % 2 == 1:
            if AM_or_PM_start == 'AM':
                AM_or_PM = 'PM'
            if AM_or_PM_start == 'PM':
                AM_or_PM = 'AM'
                n+=1

    if hours_duration < 24:
        n_ampm = (hours_duration // 12)+n_am_it
        hours_add = int(hours_duration)
        new_hour = int(hours_start) + hours_add

        if new_hour >= 24:
            new_hour -= 24
            n += 1
        if new_hour > 12 and new_hour < 24:
            if new_hour == 24: n += 1;
            new_hour -= 12
            if (n_ampm!=1): n_ampm+= 1;
        if n_ampm % 2 == 0:
            pass
        if n_ampm % 2 == 1:
            if AM_or_PM_start == 'AM':
                AM_or_PM = 'PM'
            if AM_or_PM_start == 'PM':
                AM_or_PM = 'AM'
                n += 1

    new_true_hour = str(new_hour) + ':' + str(new_minutes)

    if len(weekdaystart) > 1:
        weekdaystart = weekdaystart.lower()
        for day in week:
            if weekdaystart == day:
                days_later = n
                if days_later > len(week):
                    i = 0
                    while days_later > len(week):
                        days_later -= len(week)
                        i += 1
                    days_later += i
                    if (days_later) > len(week):
                        days_later -= len(week)
                    new_day = week[days_later - 1]

                else:
                    index=week.index(weekdaystart)
                    new_day = week[index+days_later]

        if n == 0:
            new_time = ('%s %s, %s' % (new_true_hour, AM_or_PM, new_day.capitalize()))

        if n == 1:
            new_time = ('%s %s, %s (next day)' % (new_true_hour, AM_or_PM, new_day.capitalize()))

        if n > 1:
            new_time = ('%s %s, %s (%s days later)' % (new_true_hour, AM_or_PM, new_day.capitalize(), n))

    else:
        if n == 0:
            new_time = ('%s %s' % (new_true_hour, AM_or_PM))

        if n == 1:
            new_time = ('%s %s (next day)' % (new_true_hour, AM_or_PM))

        if n > 1:
            new_time = ('%s %s (%s days later)' % (new_true_hour, AM_or_PM, n))

    return new_time
        


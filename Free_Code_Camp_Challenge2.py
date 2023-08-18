def add_time(start, duration, starting_day=None):
    def parse_start(time):
        hour, minute, period = time[:-3].split(':') + [time[-2:]]
        return int(hour), int(minute), period

    def parse_duration(time):
        hour, minute = map(int, time.split(':'))
        return hour, minute

    start_hour, start_minute, start_period = parse_start(start)
    duration_hour, duration_minute = parse_duration(duration)

    if start_period == 'PM':
        start_hour += 12

    tot_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    new_hour = new_hour = (start_hour + duration_hour + ((start_minute + duration_minute) // 60)) % 12
    new_minute = tot_minutes % 60
    new_period = new_period = 'AM' if ((start_hour + duration_hour + ((start_minute + duration_minute) // 60)) % 24) < 12 else 'PM'



    if new_hour == 0:
        new_hour = 12

    num_days_later = tot_minutes // (24 * 60)

    if starting_day:
        starting_day = starting_day.capitalize()
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        starting_index = days_of_week.index(starting_day)
        new_index = (starting_index + num_days_later) % 7
        new_day = days_of_week[new_index]
        new_time_str = f'{new_hour}:{str(new_minute).zfill(2)} {new_period}'
        if num_days_later == 1:
            new_time_str += f', {new_day} (next day)'
        elif num_days_later > 1:
            new_time_str += f', {new_day} ({num_days_later} days later)'
        else:
            new_time_str += f', {new_day}'
    else:
        new_time_str = f'{new_hour}:{str(new_minute).zfill(2)} {new_period}'
        if num_days_later == 1:
            new_time_str += ' (next day)'
        elif num_days_later > 1:
            new_time_str += f' ({num_days_later} days later)'

    new_time = new_time_str
    print(new_time)
    return new_time

def calculate_exit_day(entry_date, valid_days):
    from datetime import datetime, timedelta

    # Parse the entry date
    entry_date = datetime.strptime(entry_date, "%Y-%m-%d")
    
    # Calculate the last exit day
    last_exit_day = entry_date + timedelta(days=valid_days)
    
    return last_exit_day.strftime("%Y-%m-%d")
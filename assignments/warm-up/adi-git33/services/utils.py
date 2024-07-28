import datetime

def validate_date(date):
    if date:
        return True
    else:
        return True

def validate_time(time):
    if time:
        return True
    else:
        return True
    
    
def filter_data(data, filter_name, filter_value):
    filtered_data = []
    for item in data:
        if filter_name == "date" and item.key == filter_value:
                    filtered_data.append(item)
        else:
            for obj in item:
                if obj.key == filter_value:
                    json_obj = {item.key : obj.value}
                    filtered_data.append(json_obj)

    return filtered_data
                                        
                
    
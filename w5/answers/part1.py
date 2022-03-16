import datetime

names_ages = []

def date_to_age(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    now = datetime.datetime.now()
    diff = now - dt
    return diff.days // 365

def get_names_ages(min_age):
    if min_age is None:
        return names_ages

    # Practice this
    return list(filter(lambda record: record['age'] >= int(min_age), names_ages))

def add_name_age(name, dob):
    names_ages.append({
        'name': name,
        'age': date_to_age(dob)
    })

def edit_name_age(name, dob):
    for name_age in names_ages:
        if name_age['name'] == name:
            name_age['age'] = date_to_age(dob)
            return

def clear_names_ages():
    #Global Var!
    names_ages.clear()
    return {}
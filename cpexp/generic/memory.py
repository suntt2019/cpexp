temp_id = 0


def new_temp():
    global temp_id
    temp_id += 1
    return f't{temp_id}'

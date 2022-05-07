temp_id = 0
label_id = 100


def new_temp():
    global temp_id
    temp_id += 1
    return f'temp#{temp_id}'


def new_label():
    global label_id
    label_id += 1
    return f'label#{label_id}'

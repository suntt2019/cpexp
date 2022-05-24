def bits_to_data_size(bits: int):
    if bits > 64:
        raise Exception(f'Unsupported word length {bits}')
    elif bits <= 0:
        raise Exception(f'Invalid non-positive bits {bits}')
    elif bits <= 8:
        data_size = 'b'
    elif bits <= 16:
        data_size = 'w'
    elif bits <= 32:
        data_size = 'd'
    else:  # bits <= 64
        data_size = 'q'
    return data_size
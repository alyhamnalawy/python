def set_bit(value, position):
    value =value| 1 << position 
    return value
def clr_bit(value, position):
    value =value& (~(1 << position))
    return value
def get_bit(value, position):
    value = value &(1 << position)
def toggle_bit(value, position):
    value = value ^ (1 << position)
    return value
number=5
print(set_bit(number,1))
print(clr_bit(number,2))
print(get_bit(number,2))
print(toggle_bit(number,2))



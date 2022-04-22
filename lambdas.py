def need_space(m):
    return m.text.count(' ') != 0

def tea_drink(c):
    return c.data.split(' ')[0] == 't?drink'

def tea_decline(c):
    return c.data.split(' ')[0] == 't?decline'

def tea_spill(c):
    return c.data.split(' ')[0] == 't?spill'

def meal_eat(c):
    return c.data.split(' ')[0] == 'm?eat'

def meal_decline(c):
    return c.data.split(' ')[0] == 'm?decline'

def meal_trash(c):
    return c.data.split(' ')[0] == 'm?trash'
def water_column_height(tower_height, tank_height):
    h = tower_height+((3*tank_height)/4)
    return h

def pressure_gain_from_water_height(height):
    density = 998.2
    acceleration = 9.80665
    p = (density*acceleration*height)/1000
    return p

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
        d = 998.2
        p2 = (-1 * (friction_factor * pipe_length * (fluid_velocity ** 2) * d)) / (2000 * pipe_diameter)
        return p2
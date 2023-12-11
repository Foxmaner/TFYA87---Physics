from body import Body

def create_sun():
    sun_pos = (0, 0)
    sun_v = (0, 0)
    sun_mass = 1.9885*(10**30)
    sun_radius = 30
    sun_color = (255, 255, 0)
    sun = Body(sun_pos, sun_v, sun_mass, sun_radius, sun_color)
    return sun

def create_earth():
    earth_pos = (1.496*(10**8)*1000, 0)
    earth_v = (0, 107200 * 0.277777778)
    earth_mass = 5.972168*(10**24)
    earth_radius = 10
    earth_color = (0, 0, 255)
    earth = Body(earth_pos, earth_v, earth_mass, earth_radius, earth_color)
    return earth

def create_moon():
    moon_pos = (1.496*(10**8)*1000 + 384400 * 1000 + (10**10), 0)
    moon_v = (0, 107200 * 0.277777778 + 1023)
    moon_mass = 7.34767309 * (10**22)
    moon_radius = 3
    moon_color = (200, 200, 200)
    moon = Body(moon_pos, moon_v, moon_mass, moon_radius, moon_color)
    return moon

def create_jupiter(jupiter_close, jupiter_heavier):
    if jupiter_close:
            jupiter_pos = (778000000*500, 0)
    else:
        jupiter_pos = (778000000*1000, 0)
    jupiter_v = (0, 47051 * 0.277777778)
    if jupiter_heavier:
        jupiter_mass = (1898.13 * 10 ** 25)
    else:
        jupiter_mass = (1898.13 * 10**24)
    jupiter_radius = 15
    jupiter_color = (151, 134, 94)
    jupiter = Body(jupiter_pos, jupiter_v, jupiter_mass, jupiter_radius, jupiter_color)
    return jupiter
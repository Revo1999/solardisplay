# WMO codes generated by Chat-GPT

weather_icons = {
    0: "🌪️",     # Cloud development not observed or not observable
    1: "🌪️",     # Cloud generally dissolving or becoming less developed
    2: "☁️",     # State of sky on the whole unchanged
    3: "🌥️",     # Clouds generally forming or developing
    4: "🌫️",     # Visibility reduced by smoke
    5: "🌫️",     # Haze
    6: "🌫️",     # Widespread dust in suspension
    7: "🌫️",     # Dust or sand raised by wind
    8: "🌫️",     # Well-developed dust or sand whirl(s)
    9: "🌫️",     # Duststorm or sandstorm
    10: "🌫️",    # Mist
    11: "🌫️",    # Patches of shallow fog or ice fog
    12: "🌫️",    # More or less continuous shallow fog or ice fog
    13: "🌩️",    # Lightning visible, no thunder heard
    14: "🌧️",    # Precipitation not reaching ground
    15: "🌧️",    # Precipitation reaching ground, distant
    16: "🌧️",    # Precipitation reaching ground, near
    17: "⛈️",    # Thunderstorm, no precipitation
    18: "🌬️",    # Squalls
    19: "🌪️",    # Funnel clouds
    20: "🌧️",    # Drizzle (not freezing) or snow grains
    21: "🌧️",    # Rain (not freezing)
    22: "🌨️",    # Snow
    23: "🌧️",    # Rain and snow or ice pellets
    24: "🌧️",    # Freezing drizzle or rain
    25: "🌧️",    # Showers of rain
    26: "🌨️",    # Showers of snow
    27: "🌨️",    # Showers of hail
    28: "🌫️",    # Fog or ice fog
    29: "⛈️",    # Thunderstorm (with or without precipitation)
    30: "🌫️",    # Slight or moderate duststorm or sandstorm (decreased)
    31: "🌫️",    # Slight or moderate duststorm or sandstorm (no change)
    32: "🌫️",    # Slight or moderate duststorm or sandstorm (increased)
    33: "🌫️",    # Severe duststorm or sandstorm (decreased)
    34: "🌫️",    # Severe duststorm or sandstorm (no change)
    35: "🌫️",    # Severe duststorm or sandstorm (increased)
    36: "🌨️",    # Slight/moderate drifting snow
    37: "🌨️",    # Heavy drifting snow
    38: "🌨️",    # Slight/moderate blowing snow
    39: "🌨️",    # Heavy blowing snow
    40: "🌫️",    # Fog or ice fog at a distance
    41: "🌫️",    # Fog or ice fog in patches
    42: "🌫️",    # Fog/ice fog, sky visible, thinner
    43: "🌫️",    # Fog/ice fog, sky invisible, thinner
    44: "🌫️",    # Fog or ice fog, sky visible, no change
    45: "🌫️",    # Fog or ice fog, sky invisible, no change
    46: "🌫️",    # Fog or ice fog, sky visible, thicker
    47: "🌫️",    # Fog or ice fog, sky invisible, thicker
    48: "🌫️",    # Fog depositing rime, sky visible
    49: "🌫️",    # Fog depositing rime, sky invisible
    50: "🌧️",    # Drizzle, intermittent, slight
    51: "🌧️",    # Drizzle, continuous, slight
    52: "🌧️",    # Drizzle, intermittent, moderate
    53: "🌧️",    # Drizzle, continuous, moderate
    54: "🌧️",    # Drizzle, intermittent, heavy
    55: "🌧️",    # Drizzle, continuous, heavy
    56: "🌧️",    # Freezing drizzle, slight
    57: "🌧️",    # Freezing drizzle, moderate or heavy
    58: "🌧️",    # Rain and drizzle, slight
    59: "🌧️",    # Rain and drizzle, moderate or heavy
    60: "🌨️",    # Rain, intermittent, slight
    61: "🌨️",    # Rain, continuous, slight
    62: "🌨️",    # Rain, intermittent, moderate
    63: "🌨️",    # Rain, continuous, moderate
    64: "🌨️",    # Rain, intermittent, heavy
    65: "🌨️",    # Rain, continuous, heavy
    66: "🌨️",    # Freezing rain, slight
    67: "🌨️",    # Freezing rain, moderate or heavy
    68: "🌨️",    # Rain or drizzle and snow, slight
    69: "🌨️",    # Rain or drizzle and snow, moderate or heavy
    70: "🌨️",    # Intermittent fall of snowflakes, slight
    71: "🌨️",    # Continuous fall of snowflakes, slight
    72: "🌨️",    # Intermittent fall of snowflakes, moderate
    73: "🌨️",    # Continuous fall of snowflakes, moderate
    74: "🌨️",    # Intermittent fall of snowflakes, heavy
    75: "🌨️",    # Continuous fall of snowflakes, heavy
    76: "❄️",    # Diamond dust (with or without fog)
    77: "❄️",    # Snow grains (with or without fog)
    78: "❄️",    # Isolated star-like snow crystals (with or without fog)
    79: "🌨️",    # Ice pellets
    80: "🌧️",    # Rain shower(s), slight
    81: "🌧️",    # Rain shower(s), moderate or heavy
    82: "⛈️",    # Rain shower(s), violent
    83: "🌨️",    # Shower(s) of rain and snow, slight
    84: "🌨️",    # Shower(s) of rain and snow, moderate or heavy
    85: "🌨️",    # Snow shower(s), slight
    86: "🌨️",    # Snow shower(s), moderate or heavy
    87: "🌨️",    # Shower(s) of snow pellets or small hail, slight
    88: "🌨️",    # Shower(s) of snow pellets or small hail, moderate or heavy
    89: "🌨️",    # Shower(s) of hail, slight
    90: "🌨️",    # Shower(s) of hail, moderate or heavy
    91: "⛈️",    # Slight rain with thunderstorm
    92: "⛈️",    # Moderate or heavy rain with thunderstorm
    93: "⛈️",    # Slight snow or rain and snow with thunderstorm
    94: "⛈️",    # Moderate or heavy snow or rain and snow with thunderstorm
    95: "⛈️",    # Thunderstorm, slight or moderate, without hail
    96: "⛈️",    # Thunderstorm, slight or moderate, with hail
    97: "⛈️",    # Thunderstorm, heavy, without hail
    98: "⛈️",    # Thunderstorm combined with dust/sandstorm
    99: "⛈️"     # Heavy thunderstorm with hail
}

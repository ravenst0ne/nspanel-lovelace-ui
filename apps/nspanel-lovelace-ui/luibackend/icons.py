from icon_mapping import get_icon_id

weather_mapping = {
    'clear-night': 'weather-night',
    'cloudy': 'weather-cloudy',
    'exceptional': 'alert-circle-outline',
    'fog': 'weather-fog',
    'hail': 'weather-hail',
    'lightning': 'weather-lightning',
    'lightning-rainy': 'weather-lightning-rainy',
    'partlycloudy': 'weather-partly-cloudy',
    'pouring': 'weather-pouring',
    'rainy': 'weather-rainy',
    'snowy': 'weather-snowy',
    'snowy-rainy': 'weather-snowy-rainy',
    'sunny': 'weather-sunny',
    'windy': 'weather-windy',
    'windy-variant': 'weather-windy-variant'
}

sensor_mapping_on = {
    "door": "door-open",
}

sensor_mapping_off = {
    "door": "door-closed",
}

sensor_mapping = {
    "temperature": "thermometer",
    "power": "flash"    
}


def map_to_mdi_name(ha_type, state=None, device_class=None):
    if ha_type == "weather":
        return weather_mapping[state] if state in weather_mapping else "alert-circle-outline"
    if ha_type == "button":
        return "gesture-tap-button"
    if ha_type == "scene":
        return "palette"
    if ha_type == "script":
        return "script-text"
    if ha_type == "switch":
        return "light-switch"
    if ha_type == "number":
        return "ray-vertex"
    if ha_type == "light":
        return "lightbulb"
    if ha_type == "fan":
        return "fan"
    if ha_type == "input_boolean":
        return "check-circle-outline" if state == "on" else "close-circle-outline"
    if ha_type == "cover":
        if device_class == "awning" or device_class == "blind" or device_class == "curtain":
            return "blinds-open" if state == "open" else "blinds"
        elif device_class == "door":
            return "door-open" if state == "open" else "door-closed" 
        elif device_class == "garage":
            return "garage-open" if state == "open" else "garage"
        elif device_class == "gate":
            return "gate-open" if state == "open" else "gate"
        elif device_class == "shade" or device_class == "shutter":
            return "window-shutter-open" if state == "open" else "window-shutter"
        else:
        # This should run for None, window or damper
            return "window-open" if state == "open" else "window-closed"
    if ha_type == "lock":
        return "lock-open" if state == "unlocked" else "lock"

    elif ha_type == "sensor":
        if state == "on":
            return sensor_mapping_on[device_class] if device_class in sensor_mapping_on else "alert-circle-outline"
        elif state == "off":
            return sensor_mapping_off[device_class] if device_class in sensor_mapping_off else "alert-circle-outline"
        else:
            return sensor_mapping[device_class] if device_class in sensor_mapping else "alert-circle-outline"

    return "alert-circle-outline"

def get_icon_id_ha(ha_name, state=None, device_class=None, overwrite=None):
    if overwrite is not None:
        return get_icon_id(overwrite)
    return get_icon_id(map_to_mdi_name(ha_name, state, device_class))

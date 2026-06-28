test_settings = {
    'theme': 'light',
    'notifications': 'on',
    'language': 'english',
    'autosave': 'off'
}

def add_setting(test_settings, new_setting):
    key, value = new_setting[0].lower(), new_setting[1].lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

add_setting({'theme': 'light'}, ('THEME', 'dark'))    
add_setting({'theme': 'light'}, ('volume', 'high'))
    

def update_setting(test_settings, new_setting):
    new_key, new_value = new_setting
    new_key, new_value = new_setting[0].lower(), new_setting[1].lower()

    if new_key in test_settings:
        test_settings[new_key] = new_value
        return f"Setting '{new_key}' updated to '{new_value}' successfully!"
    else:
        return f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings, key):
    key = key.lower()

    if key not in test_settings:
        return f"Setting not found!"
    else:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"

def view_settings(test_settings):

    if not test_settings:
        return "No settings available."
    else:
        output = ["Current Settings:" + "\n"]
        for key, value in test_settings.items():
            output.append(f"{key.capitalize()}: {value}")
        return "\n".join(output) + "\n"

add_setting(test_settings, ('timer', 'off'))
print(view_settings(test_settings))
import app_controller

window = app_controller.windows_controller()



window.cmd_color("e")
window.clear_cmd()

going = True
while going:
    command = input('Enter the name of software to open: ')
    if 'setting' in command:
        window.open_settings()
    elif 'control panel' in command:
        window.open_cpanel()
    elif 'cmd' in command:
        window.open_cmd()
    elif 'full' in command:
        window.fullscreen()
    else:
        print(f'No software is present with a name of " {command} ".')

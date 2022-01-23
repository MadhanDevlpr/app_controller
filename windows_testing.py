from app_controller import windows_controller

window = windows_controller.device()

# testing codes are removed after working.

window.run_command('git add .')
window.run_command('git commit -m "update"')
window.run_command('git pull')
window.run_command('git push origin main')
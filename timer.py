import json
import time

# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.

FILE = "timer.json"
SAVE_INTERVAL = 3

def save_timer_state(total_seconds, file_path):
    timer_time = {'timer_state': total_seconds}
    with open(file_path, 'w') as wfile:
        json.dump(timer_time, wfile)

def load_timer_state(file_path):
    try:
        with open(file_path, 'r') as rfile:
            state = json.load(rfile)
            timer_state = state.get('timer_state', 0)
    except FileNotFoundError:
        return 0
    
    return timer_state

def start_timer():
    timer_previous = load_timer_state(FILE)
    timer_elapsed = 0

    while True:
        try:
            time.sleep(0.5)
            timer_elapsed += 0.5
            timer_time = timer_previous + timer_elapsed
            print(f"Timer: {timer_time} sec")
            if timer_elapsed % SAVE_INTERVAL == 0:
                save_timer_state(timer_time, FILE)
                print("Timer saved")
        except KeyboardInterrupt:
            print(f"Timer stopped")
            save_timer_state(timer_time, FILE)
            break

start_timer()
time.sleep(2)
start_timer()
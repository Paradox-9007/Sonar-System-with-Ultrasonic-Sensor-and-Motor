import serial
import tkinter as tk
import math
import time

# Install required library: pip install pyserial
# Adjust the serial port (check Arduino IDE → Tools → Port)

serialPort = 'COM3'  # 👈 change if needed
ser = serial.Serial(serialPort, 9600, timeout=0.1)
last_angle = 0
last_distance = 100
last_update_time = time.time()

TIMEOUT = 0.2
MAX_DISTANCE = 200

# --- WINDOW ---
root = tk.Tk()
root.title("Close Range Sonar")
root.configure(bg="black")

top_frame = tk.Frame(root, bg="black")
top_frame.pack()

bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack()

canvas = tk.Canvas(top_frame, width=600, height=400, bg="black", highlightthickness=0)
canvas.pack()

chart = tk.Canvas(bottom_frame, width=600, height=150, bg="black", highlightthickness=0)
chart.pack()

log_box = tk.Text(bottom_frame, height=5, width=70, bg="black", fg="lime")
log_box.pack()

# --- RANGE CONTROL ---
range_var = tk.IntVar(value=100)

slider = tk.Scale(root, from_=20, to=200,
                  orient="horizontal",
                  label="Detection Range (cm)",
                  variable=range_var,
                  bg="black", fg="lime",
                  width=15, sliderlength=10, length=400)
slider.pack()

# --- DATA ---
points = {}
distances = []
max_chart = 60

# --- COLOR GRADIENT ---
def get_color(distance, max_range):
    ratio = distance / max_range

    red = int(255 * (1 - ratio))
    green = int(255 * ratio)

    return f'#{red:02x}{green:02x}00'

# --- Sonar DRAW ---
def draw_sonar(angle, distance):
    canvas.delete("all")

    cx, cy = 300, 350
    max_range = range_var.get()

    scale = 300 / max_range

    # grid arcs
    for r in range(1, 6):
        radius = r * (300 / 5)
        canvas.create_arc(cx-radius, cy-radius, cx+radius, cy+radius,
                          start=0, extent=180,
                          outline="#003300")

    # radial lines
    for a in range(0, 181, 30):
        x = cx + 300 * math.cos(math.radians(a))
        y = cy - 300 * math.sin(math.radians(a))
        canvas.create_line(cx, cy, x, y, fill="#002200")

    # sweep line
    x = cx + 300 * math.cos(math.radians(angle))
    y = cy - 300 * math.sin(math.radians(angle))
    canvas.create_line(cx, cy, x, y, fill="lime", width=2)

    # update map (only valid range)
    if distance <= max_range:
        points[int(angle)] = distance

    # draw points
    for a, d in points.items():
        if d > max_range:
            continue

        rad = math.radians(a)
        px = cx + d * scale * math.cos(rad)
        py = cy - d * scale * math.sin(rad)

        color = get_color(d, max_range)
        canvas.create_oval(px-3, py-3, px+3, py+3, fill=color, outline="")

# --- CHART ---
def draw_chart(distance):
    distances.append(distance)

    if len(distances) > max_chart:
        distances.pop(0)

    chart.delete("all")

    for i in range(1, len(distances)):
        x1 = (i-1) * 10
        y1 = 150 - min(distances[i-1], 150)

        x2 = i * 10
        y2 = 150 - min(distances[i], 150)

        chart.create_line(x1, y1, x2, y2, fill="lime", width=2)

# --- LOG (LAST 10 ONLY) ---
def update_log(angle, distance):
    log_box.insert("end", f"{int(angle)}° | {int(distance)} cm\n")
    log_box.see("end")

    if int(log_box.index('end-1c').split('.')[0]) > 10:
        log_box.delete("1.0", "2.0")

# --- MAIN LOOP (FIXED) ---
def update():
    global last_angle, last_distance, last_update_time

    try:
        if ser.in_waiting:
            data = ser.readline().decode(errors='ignore').strip()

            if "," in data:
                parts = data.split(",")

                if len(parts) == 2:
                    angle = float(parts[0])
                    distance = float(parts[1])

                    # filter bad values
                    if distance <= 0 or distance > MAX_DISTANCE:
                        distance = MAX_DISTANCE

                    last_angle = angle
                    last_distance = distance
                    last_update_time = time.time()

    except:
        pass

    # --- HANDLE SENSOR FREEZE ---
    if time.time() - last_update_time > TIMEOUT:
        distance = MAX_DISTANCE
    else:
        distance = last_distance

    # ALWAYS update UI
    draw_sonar(last_angle, distance)
    draw_chart(distance)
    update_log(last_angle, distance)

    root.after(50, update)

# --- START ---
update()
root.mainloop()
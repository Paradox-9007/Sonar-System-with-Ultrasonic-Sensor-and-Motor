# Sonar System with Ultrasonic Sensor and Motor

A simple sonar visualization project using a **NodeMCU**, **HC-SR04P ultrasonic sensor**, and **SG90 servo motor**.  
The ultrasonic sensor rotates across a 180° area while sending distance data to a Python visualization interface.

This project combines:

- Embedded Systems
- Arduino / C++
- Python Visualization
- Serial Communication
- Ultrasonic Distance Sensing

---

# Features

- 180° scanning using SG90 servo motor
- Real-time ultrasonic distance detection
- Python visualization
- Serial communication between NodeMCU and Python
- Low-cost hardware implementation

---

# Hardware Components

| Component | Quantity |
|---|---|
| NodeMCU ESP8266 | 1 |
| HC-SR04P Ultrasonic Sensor | 1 |
| SG90 Micro Servo Motor | 1 |
| Breadboard | 1 |
| USB Cable | 1 |
| Male-Female Jumper Wires | 8 |
| Male-Male Jumper Wires | 3 |
| Cardboard Pieces | 2 |
| Paper Clips | 2 |

---

# Wiring Diagram
<img width="536" height="352" alt="image" src="https://github.com/user-attachments/assets/6a5026ab-a9a1-41d0-b7dc-6d25ee0a9434" />


## Ultrasonic Sensor → NodeMCU

| HC-SR04P Pin | NodeMCU Pin |
|---|---|
| VCC | 3.3V |
| GND | GND |
| TRIG | D5 |
| ECHO | D6 |

---

## Servo Motor → NodeMCU

| SG90 Wire | NodeMCU Pin |
|---|---|
| Orange (Signal) | D7 |
| Red (Power) | Vin (5V) |
| Brown (Ground) | GND |

> ⚠️ The SG90 servo motor requires 4.8V–6V.  
> Using 3.3V may not provide enough power for stable operation.

---

# Hardware Assembly

## Step 1 — Setup NodeMCU

Attach the NodeMCU to the breadboard.

---

## Step 2 — Connect Ultrasonic Sensor

Wire the HC-SR04P sensor according to the table above.

---

## Step 3 — Build Sensor Mount
<img width="1245" height="695" alt="image" src="https://github.com/user-attachments/assets/3417f484-8fb1-4d37-8237-bcd6542a50b7" />

Using cardboard and paper clips:

- Attach cardboard to the servo horn
- Secure using paper clips

<img width="1247" height="700" alt="image" src="https://github.com/user-attachments/assets/e39ae5d3-858a-4e39-aadf-22aeb4de5292" />
<img width="1246" height="698" alt="image" src="https://github.com/user-attachments/assets/51c9fc2b-9941-4f69-aca2-afc2ca4f97bc" />


- Mount the ultrasonic sensor on the front side
- Ensure:
  - Servo wires point downward
  - Sensor wires point upward

This creates the rotating scanning platform.

---
# Software Setup

## 1. Arduino IDE Setup

Open the `.ino` file inside Arduino IDE.

Example:

```text
File → Open → sketch_apr15a.ino
```

Do not upload yet.

---

## 2. Python Setup

Open the `sonar_ui.py` file using:

- VS Code
- PyCharm
- or any Python IDE

---

## 3. Install Python Dependencies

Install `pyserial`:

```bash
pip install pyserial
```

---

## 4. Configure Serial Port

Inside the Python file, change the serial port to match your NodeMCU port.

Example:

```python
serialPort = "COM3"
```

You can check the port number inside:

```text
Arduino IDE → Tools → Port
```

---

# Running the Project

## Step 1 — Upload Arduino Code

Before uploading:

- Make sure the servo area is clear
- Ensure all wiring connections are correct

Upload the `sketch_apr15a.ino` file to the NodeMCU.

The servo motor should begin rotating and scanning a 180° area.

---

## Step 2 — Close Serial Monitor

Before running Python visualization:

- Close Arduino Serial Monitor

Otherwise the serial port may become busy.

---

## Step 3 — Run Python Visualization
<img width="1477" height="1108" alt="img-2" src="https://github.com/user-attachments/assets/53a8fe4e-2547-44b3-9b3e-4f1a42d137ee" />

Run the Python script:

```bash
python sonar.py
```

The sonar visualization window should appear and begin displaying distance scans in real time.

---

# Safety Notice

⚠️ Important Safety Information

The servo motor starts rotating immediately after the Arduino code is uploaded.

Incorrect wiring or hardware issues may cause:

- Uncontrolled spinning
- Hardware damage
- Injury from moving components

If this happens:

1. Disconnect the USB cable immediately
2. Power off the NodeMCU
3. Recheck all wiring connections

Keep:

- fingers
- hair
- loose wires

away from the rotating mechanism.

# Technologies Used

- Arduino / C++
- Python
- PySerial
- NodeMCU ESP8266
- HC-SR04P Ultrasonic Sensor
- SG90 Servo Motor

---

# Learning Outcomes


This project helped demonstrate:

- Embedded systems integration
- Serial communication between hardware and software
- Real-time visualization techniques
- Sensor-based distance measurement
- Basic robotics and motion control

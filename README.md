# Webots Simulation with Teleop Key (ROS2)

Simulasi robot menggunakan Webots yang dikontrol melalui keyboard menggunakan ROS2 (`teleop_twist_keyboard`). Cocok digunakan dengan **internal Webots controller** untuk integrasi yang lebih sederhana.

---

## 🗂️ Struktur Direktori

```
my_webots_project/
├── worlds/
│   └── my_world.wbt
├── controllers/
│   └── ros2_teleop_controller/
│       └── ros2_teleop_controller.py
```

---

## 🚀 Setup ROS2 & Teleop Keyboard

### 📌 Jika Belum Punya ROS2 Workspace

```bash
cd ~/ros2_ws/src
git clone https://github.com/ros2/teleop_twist_keyboard.git
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

### ▶️ Menjalankan Teleop Keyboard

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## ⚙️ Menjalankan Webots + ROS2

### 1. Source Environment
```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

### 2. Jalankan Webots
```bash
webots ~/Path-Planning-Swarm-Robot-Simulation-in-Webots/worlds/your_world.wbt
```

> ❗ Pastikan file `.wbt` kamu dan nama controller sudah sesuai.

---

## 🧠 Tentang Controller Internal (`ros2_teleop_controller.py`)

Script ini digunakan di Webots controller dan berfungsi menerima perintah dari ROS2 (`/cmd_vel`) lalu menggerakkan motor berdasarkan input `linear.x` dan `angular.z`.

### Cuplikan Kode (Singkat):

```python
self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

def cmd_vel_callback(self, msg):
    self.linear_velocity = msg.linear.x
    self.angular_velocity = msg.angular.z
```

Motor kanan dan kiri akan disesuaikan dengan perhitungan differential drive.

---

## 🎮 Kontrol Keyboard (via `teleop_twist_keyboard`)

```
Moving around:
   u    i    o
   j    k    l
   m    ,    .

Hold Shift → Holonomic Mode (strafing):
   U    I    O
   J    K    L
   M    <    >

Special Keys:
t/b : up/down (z-axis)
q/z : increase/decrease all speeds
w/x : increase/decrease linear speed
e/c : increase/decrease angular speed
```

---

## 🔍 Debug & Monitoring

### Cek apakah topik `/cmd_vel` aktif
```bash
ros2 topic list
ros2 topic echo /cmd_vel
```

---

## 🐍 Error Umum: `ModuleNotFoundError: No module named 'rclpy'`

Jika muncul error seperti ini saat menjalankan Webots:

```
ModuleNotFoundError: No module named 'rclpy'
```

💡 Artinya interpreter Python yang digunakan Webots belum mengenali ROS2 environment.

### ✅ Solusi:

Pastikan sebelum menjalankan Webots, kamu sudah menjalankan:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
webots ~/Path-Planning-Swarm-Robot-Simulation-in-Webots/worlds/your_world.wbt
```

---

## 📌 Catatan Tambahan

Jika kamu menggunakan **controller eksternal**, maka integrasi akan lebih kompleks karena harus menggunakan Webots-ROS bridge atau supervisor script. Gunakan controller internal untuk kemudahan integrasi.

---

## 📫 Kontak

Jika ada pertanyaan atau ingin kontribusi, silakan buka Issue atau Pull Request di repo ini!

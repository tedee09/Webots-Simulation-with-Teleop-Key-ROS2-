import cv2
import numpy as np

# Pilih dictionary ArUco (bisa 4x4, 5x5, 6x6, dst.)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

# Ubah ID marker (coba ID dari 0 sampai 49 untuk DICT_4X4_50)
for marker_id in range(5):  # Generate 5 marker dengan ID berbeda
    marker_size = 200  # Ukuran dalam piksel
    marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    # Simpan gambar marker
    filename = f"marker_{marker_id}.png"
    cv2.imwrite(filename, marker_image)
    print(f"Marker {marker_id} disimpan sebagai {filename}")

print("Selesai! Semua marker telah dibuat.")

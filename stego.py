import cv2
import os

image_path = r"C:\Users\pshou\OneDrive\Desktop\AICTE\Stenography-main\mypic.jpg"

if not os.path.isfile(image_path):
    print(f"Error: File not found -> {image_path}")
    exit()

img = cv2.imread(image_path)

if img is None:
    print("Error: Failed to read the image.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter password: ")

d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

n, m, z = 0, 0, 0
height, width, channels = img.shape

if len(msg) > height or len(msg) > width:
    print("Error: Message too long for this image.")
    exit()

for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

    if n >= height or m >= width:
        print("Warning: Message truncated due to image size.")
        break

cv2.imwrite("Encryptedmsg.jpg", img)
print("Encrypted image saved as: Encryptedmsg.jpg")

decrypted_message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for _ in range(len(msg)):
        decrypted_message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

        if n >= height or m >= width:
            break

    print("Decrypted message:", decrypted_message)
else:
    print("Not a valid key. Decryption failed.")

from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)
    encrypted_img_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_img_array)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img_array = np.array(encrypted_img)
    decrypted_img_array = np.bitwise_xor(encrypted_img_array, key)
    decrypted_img = Image.fromarray(decrypted_img_array)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    encryption_key = 12345  # This can be any integer value (same for both encryption and decryption)
    encrypt_image("your_image.png", encryption_key)
    decrypt_image("encrypted_image.png", encryption_key)

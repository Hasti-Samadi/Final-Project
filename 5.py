import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

# تابع خواندن تصویر و تبدیل به آرایه دو بعدی
def read_image(file_path):
    image = imread(file_path)
    if image.ndim == 3:
        image = rgb2gray(image)
    return image

# تابع کانولوشن
def apply_convolution(image, kernel):
    return convolve(image, kernel)

# تابع پردازش تصویر
def process_image(file_path):
    image = read_image(file_path)
    
    # فیلترهای سوبل
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    
    # اعمال فیلتر سوبل در جهت x و y
    edge_x = apply_convolution(image, sobel_x)
    edge_y = apply_convolution(image, sobel_y)
    
    # ترکیب نتایج دو فیلتر
    result = np.hypot(edge_x, edge_y)
    
    # نرمال‌سازی تصویر خروجی برای تبدیل به اعداد صحیح 8 بیتی
    result_normalized = (result - result.min()) / (result.max() - result.min())
    result_uint8 = (result_normalized * 255).astype(np.uint8)
    
    # ذخیره تصویر تشخیص لبه به عنوان فایل تصویری جدید
    imsave('sobel_edge_detected_image.png', result_uint8)
    
    # ذخیره تصویر تشخیص لبه در فایل متنی
    np.savetxt('sobel_edge_detected_image.txt', result)
    
    return image, result_uint8

# تابع برای انتخاب فایل
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        original, processed = process_image(file_path)
        display_images(original, processed)

# تابع برای نمایش تصاویر
def display_images(original, processed):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(processed, cmap='gray')
    axes[1].set_title('Edge Detected Image')
    axes[1].axis('off')
    plt.show()

# ساخت رابط کاربری
def create_gui():
    root = Tk()
    root.title("Edge Detection using Sobel Filter")
    
    Label(root, text="Select an image file for edge detection:").pack(pady=10)
    Button(root, text="Browse", command=select_file).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import convolve
from skimage.io import imread, imsave
from skimage.color import rgb2gray

# تابع خواندن تصویر و تبدیل به آرایه دو بعدی
def read_image(file_path):
    image = imread(file_path)
    if image.ndim == 3:
        image = rgb2gray(image)
    return image

# تابع کانولوشن
def apply_convolution(image, kernel):
    return convolve(image, kernel)

# تابع اصلی
def main():
    # نام فایل تصویری که باید در پوشه جاری قرار گیرد
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, 'image.png')
    
    # خواندن تصویر از فایل
    image = read_image(image_path)
    
    # فیلتر تشخیص لبه
    edge_detection_kernel = np.array([[-1, -1, -1],
                                      [-1,  8, -1],
                                      [-1, -1, -1]])
    
    # اعمال کانولوشن
    result = apply_convolution(image, edge_detection_kernel)
    
    # نرمال‌سازی تصویر خروجی برای تبدیل به اعداد صحیح 8 بیتی
    result_normalized = (result - result.min()) / (result.max() - result.min())
    result_uint8 = (result_normalized * 255).astype(np.uint8)
    
    # ذخیره تصویر تشخیص لبه به عنوان فایل تصویری جدید
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_output_path = os.path.join(current_directory, 'edge_detected_image.png')
    imsave(image_output_path, result_uint8)
    
    # ذخیره تصویر تشخیص لبه در فایل متنی
    current_directory = os.path.dirname(os.path.abspath(__file__))
    text_output_path = os.path.join(current_directory, 'edge_detected_image.txt')
    np.savetxt(text_output_path, result)
    
    # نمایش تصاویر
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title('Edge Detected Image')
    plt.show()

if __name__ == "__main__":
    main()

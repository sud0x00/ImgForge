from PIL import Image
import os

folder_path = os.path.join(os.getcwd(), 'images')
pdf_file_name = 'pdf_name.pdf'


images = []
for image_file in os.listdir(folder_path):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        images.append(Image.open(os.path.join(folder_path, image_file)))

images[0].save(pdf_file_name, save_all=True, append_images=images[1:])

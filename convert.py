from PIL import Image
import os
import shutil

def convert_and_reduce_image_size(image_dir, output_dir, max_width=800, max_height=800, quality=85):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(image_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.heif', '.heic', '.ico', '.cur', '.tif', '.jfif', '.jpe', '.jif', '.jfi', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.jxr', '.hdp', '.wdp')):
            try:
                img_path = os.path.join(image_dir, filename)
                img = Image.open(img_path)

                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Check if the image is already smaller than the specified dimensions
                if img.width <= max_width and img.height <= max_height:
                    print(f"Image '{filename}' is already smaller than specified dimensions, copying.")
                    shutil.copy(img_path, output_dir)
                    continue

                # Reduce size if necessary
                img.thumbnail((max_width, max_height), Image.LANCZOS)

                # Save my directoryy
                output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')
                img.save(output_path, quality=quality)
                print(f"Converted and reduced: {filename} -> {os.path.basename(output_path)}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    image_dir = 'downloaded_images'
    output_dir = 'processed_images'
    convert_and_reduce_image_size(image_dir, output_dir)

import os
import cv2


class ImageAnalyzer:

    def analyze_image(self, image_path):

        image = cv2.imread(image_path)

        height, width = image.shape[:2]

        channels = image.shape[2] if len(image.shape) == 3 else 1

        extension = os.path.splitext(image_path)[1]

        file_size = round(os.path.getsize(image_path) / 1024, 2)

        details = {
            "Image Name": os.path.basename(image_path),
            "Width": width,
            "Height": height,
            "Resolution": f"{width} x {height}",
            "Channels": channels,
            "Format": extension,
            "File Size (KB)": file_size
        }

        return details
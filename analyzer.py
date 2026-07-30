import os
import cv2


class ImageAnalyzer:

    def analyze_image(self, image_path):

        try:
            # Check if file exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"File not found: {image_path}")

            # Read image
            image = cv2.imread(image_path)

            if image is None:
                raise ValueError("Unable to read the image. The file may be corrupted or unsupported.")

            # Extract image details
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

        except FileNotFoundError as e:
            print(f"File Error: {e}")
            return None

        except ValueError as e:
            print(f"Image Error: {e}")
            return None

        except PermissionError as e:
            print(f"Permission Error: {e}")
            return None

        except Exception as e:
            print(f"Unexpected Error: {e}")
            return None
import os
import cv2


class ImageValidator:

    def __init__(self):
        self.valid_extensions = [".jpg", ".jpeg", ".png"]

    def validate_image(self, image_path):
        try:
            # Check file exists
            if not os.path.exists(image_path):
                return False, "File does not exist."

            # Check extension
            extension = os.path.splitext(image_path)[1].lower()

            if extension not in self.valid_extensions:
                return False, "Unsupported file format."

            # Read image
            image = cv2.imread(image_path)

            if image is None:
                return False, "Image is corrupted."

            return True, "Image is valid."

        except Exception as e:
            return False, str(e)
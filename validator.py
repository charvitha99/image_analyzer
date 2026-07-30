import os
import cv2


class ImageValidator:

    def __init__(self):
        self.valid_extensions = [".jpg", ".jpeg", ".png"]

    def validate_image(self, image_path):

        try:
            # Check if file exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"File not found: {image_path}")

            # Check file extension
            extension = os.path.splitext(image_path)[1].lower()

            if extension not in self.valid_extensions:
                raise ValueError("Unsupported file format.")

            # Read image
            image = cv2.imread(image_path)

            if image is None:
                raise ValueError("Image is corrupted or cannot be opened.")

            return True, "Image is valid."

        except FileNotFoundError as e:
            return False, f"File Error: {e}"

        except ValueError as e:
            return False, f"Validation Error: {e}"

        except PermissionError as e:
            return False, f"Permission Error: {e}"

        except Exception as e:
            return False, f"Unexpected Error: {e}"
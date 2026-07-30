import os
import cv2
import matplotlib.pyplot as plt


class ImageProcessor:

    def process_image(self, image_path, output_folder):

        try:
            # Check if image file exists
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"File not found: {image_path}")

            # Read image
            image = cv2.imread(image_path)

            if image is None:
                raise ValueError("Image cannot be processed. It may be corrupted or in an unsupported format.")

            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize image
            resized = cv2.resize(gray, (300, 300))

            # Edge Detection
            edges = cv2.Canny(resized, 100, 200)

            image_name = os.path.basename(image_path)

            # Save processed image
            output_path = os.path.join(output_folder, image_name)
            cv2.imwrite(output_path, edges)

            # Generate Histogram
            histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

            histogram_name = os.path.splitext(image_name)[0] + "_histogram.png"
            histogram_path = os.path.join(output_folder, histogram_name)

            plt.figure(figsize=(6, 4))
            plt.plot(histogram)
            plt.title("Image Histogram")
            plt.xlabel("Pixel Intensity")
            plt.ylabel("Number of Pixels")
            plt.savefig(histogram_path)
            plt.close()

            return output_path

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
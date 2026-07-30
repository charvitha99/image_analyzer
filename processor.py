import os
import cv2
import matplotlib.pyplot as plt


class ImageProcessor:

    def process_image(self, image_path, output_folder):

        try:

            image = cv2.imread(image_path)

            if image is None:
                raise Exception("Image cannot be processed.")

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

            # ---------- Histogram Generation ----------
            histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

            histogram_name = image_name.split(".")[0] + "_histogram.png"
            histogram_path = os.path.join(output_folder, histogram_name)

            plt.figure(figsize=(6,4))
            plt.plot(histogram)
            plt.title("Image Histogram")
            plt.xlabel("Pixel Intensity")
            plt.ylabel("Number of Pixels")
            plt.savefig(histogram_path)
            plt.close()
            # ------------------------------------------

            return output_path

        except Exception as e:
            print("Processor Error:", e)
            return None
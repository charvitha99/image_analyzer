import os

from validator import ImageValidator
from analyzer import ImageAnalyzer
from processor import ImageProcessor
from report import ReportGenerator
from logger import logger


def main():

    image_folder = "images"
    output_folder = "outputs"
    report_folder = "reports"

    try:
        # Check if images folder exists
        if not os.path.exists(image_folder):
            raise FileNotFoundError(f"'{image_folder}' folder not found.")

        # Create required folders
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(report_folder, exist_ok=True)

        validator = ImageValidator()
        analyzer = ImageAnalyzer()
        processor = ImageProcessor()
        reporter = ReportGenerator()

        logger.info("Image Analyzer Project Started")

        for category in os.listdir(image_folder):

            category_path = os.path.join(image_folder, category)

            if not os.path.isdir(category_path):
                continue

            print(f"\nProcessing Category: {category}")
            logger.info(f"Processing Category: {category}")

            for image_name in os.listdir(category_path):

                image_path = os.path.join(category_path, image_name)

                # Validate Image
                valid, message = validator.validate_image(image_path)

                if not valid:
                    print(f"{image_name}: {message}")
                    logger.warning(f"{image_name}: {message}")
                    continue

                # Analyze Image
                details = analyzer.analyze_image(image_path)

                if details is None:
                    print(f"Skipping {image_name} due to analysis error.")
                    logger.error(f"Analysis failed for {image_name}")
                    continue

                # Process Image
                output_path = processor.process_image(
                    image_path,
                    output_folder
                )

                if output_path is None:
                    print(f"Skipping {image_name} due to processing error.")
                    logger.error(f"Processing failed for {image_name}")
                    continue

                # Generate Report
                report_path = reporter.generate_report(
                    details,
                    report_folder
                )

                if report_path is None:
                    print(f"Skipping {image_name} due to report generation error.")
                    logger.error(f"Report generation failed for {image_name}")
                    continue

                print(f"Processed: {image_name}")
                print(f"Saved Image : {output_path}")
                print(f"Saved Report: {report_path}")

                logger.info(f"Processed: {image_name}")
                logger.info(f"Saved Image: {output_path}")
                logger.info(f"Saved Report: {report_path}")

        print("\nAll images processed successfully.")
        logger.info("All images processed successfully.")

    except FileNotFoundError as e:
        print(f"File Error: {e}")
        logger.error(f"File Error: {e}")

    except PermissionError as e:
        print(f"Permission Error: {e}")
        logger.error(f"Permission Error: {e}")

    except OSError as e:
        print(f"Operating System Error: {e}")
        logger.error(f"Operating System Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")
        logger.error(f"Unexpected Error: {e}")

    finally:
        logger.info("Image Analyzer Project Finished")


if __name__ == "__main__":
    main()
import os


class ReportGenerator:

    def generate_report(self, details, report_folder):

        report_name = details["Image Name"].split(".")[0] + ".txt"

        report_path = os.path.join(report_folder, report_name)

        with open(report_path, "w") as file:

            file.write("========== IMAGE ANALYSIS REPORT ==========\n\n")

            for key, value in details.items():
                file.write(f"{key}: {value}\n")

        return report_path
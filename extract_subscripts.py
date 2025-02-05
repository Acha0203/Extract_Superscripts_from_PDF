import pymupdf  # PyMuPDF
import sys
import os

def extract_subscripts(pdf_path, threshold):
    subscripts = []

    # Open the PDF file
    with pymupdf.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            blocks = page.get_text("dict")["blocks"]  # Get text blocks

            for block in blocks:
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        # Get font size and Y coordinate of the text
                        font_size = span["size"]
                        origin_y = span["origin"][1]  # Y coordinate of the text

                        # Specify the font size threshold and the position of the text
                        if font_size <= threshold and origin_y - font_size / 2 > 0:
                            subscripts.append({
                                "text": span["text"],
                                "page": page_num,
                                "size": font_size,
                                "position": span["origin"]
                            })

    return subscripts

input_file_name = ""

while input_file_name == "":
    print("Enter the file name of the PDF from which you want to extract subscript texts in the format 'XXX.pdf': ")
    sys.stdout.flush()
    input_file_name = str(sys.stdin.readline()).strip()
    if not os.path.exists(input_file_name):
        print(f"The file {input_file_name} does not exist. Please check the file name.")
        input_file_name = ""

print(f"This program will extract subscript texts from {input_file_name}.")

default_threshold = 8.5

print(f"Enter the threshold value of the font size for extracting subscript texts. The default value is {default_threshold}: ")
sys.stdout.flush()
threshold_input = sys.stdin.readline().strip()

if threshold_input == "":
    threshold = default_threshold
else:
    threshold = float(threshold_input)

default_output_file_name = "subscripts.txt"

print(f"Enter the file name to save the extracted subscript texts in the format 'XXX.txt'. The default file name is {default_output_file_name}: ")
sys.stdout.flush()
output_file_name = str(sys.stdin.readline()).strip()

if output_file_name == "":
    output_file_name = default_output_file_name

subscripts = extract_subscripts(input_file_name, threshold)

# Save the extracted subscript texts to a text file
with open(output_file_name, "w", encoding="utf-8") as f:
    if subscripts:
        for item in subscripts:
            f.write(f"Page {item['page']}: {item['text']} (Font Size: {item['size']}, Position: {item['position']})\n")
    else:
        f.write("No subscripts were found. \n")

print(f"The extracted subscript texts have been saved in {output_file_name}.")

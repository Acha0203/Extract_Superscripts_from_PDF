# Python Program to Extract Subscripts from a PDF file

## Description

You can extract subscript texts from a PDF file by using this Python program.

## Usage

1. In your project root directory, create a Python virtual environment ('pymupdf-venv' in the following commands is your virtual environment name).

- Windows:

```shell
py -m venv pymupdf-venv
.\pymupdf-venv\Scripts\activate
python -m pip install --upgrade pip
```

- Linux or MacOS:

```shell
python -m venv pymupdf-venv
. pymupdf-venv/bin/activate
python -m pip install --upgrade pip
```

1. Install PyMuPDF with the following command:

```shell
pip install --upgrade pymupdf
```

3. Run this program with the following command:

```shell
python extract_subscripts.py
```

4. Follow the on-screen instructions.
5. You can exit your virtual environment with the following command:

```shell
deactivate
```

## Tips

- Due to the nature of this program, text in graphs and figures may be extracted incorrectly. Please ignore such texts by referring to the page number.
- To successfully extract subscript texts, first set the font size of the subscript you want to extract to around 8.5, extract it once, and check the result. If the subscripts are not extracted, specify the value larger than '8.5' for the font size and try extracting again.
- If a lot of non-subscript texts are extracted along with subscripts, check the font size of the subscript texts by referring your output file. Within the same file, subscripts are often the same size, so specify a slightly larger size as the font size of the subscript you want to extract, and then try extracting again.

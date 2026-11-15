# PDF to Images

A lightweight Python utility to convert PDF documents into images using [PyMuPDF](https://pymupdf.readthedocs.io/).

## Features

- Convert each PDF page into a separate image.
- Customize image resolution (DPI).
- Choose the output format (PNG, JPG, JPEG, TIFF, BMP).
- Customize output filenames.
- Specify the output directory.
- Accept PDF file paths, binary content, and file-like objects.
- Process pages individually to limit memory consumption.
- No external dependencies except PyMuPDF.

## Requirements

- Python 3.9+
- PyMuPDF

## Installation

Clone the repository:

    git clone https://github.com/Dark-Knife/pdf-to-images.git
    cd pdf-to-images

Install the dependency:

    pip install pymupdf

Alternatively:

    pip install -r requirements.txt

## Usage

Import the function:

    from pdf_to_images import pdf_to_images

### Basic conversion

    images = pdf_to_images("document.pdf")

By default:
- Output format: PNG
- Resolution: 300 DPI
- Output directory: current directory
- Output filename: original PDF filename

### Custom DPI and format

    images = pdf_to_images(
        pdf="document.pdf",
        extension="jpg",
        dpi=600
    )

### Custom output directory and filename

    images = pdf_to_images(
        pdf="document.pdf",
        output_dir="./images",
        output_name="invoice",
        extension="png",
        dpi=300
    )

### Using a file object

    with open("document.pdf", "rb") as file:
        images = pdf_to_images(
            pdf=file,
            output_name="export",
            extension="png",
            dpi=200
        )

### Using binary content

    with open("document.pdf", "rb") as file:
        pdf_content = file.read()

    images = pdf_to_images(
        pdf=pdf_content,
        output_name="export",
        extension="tiff",
        dpi=300
    )

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| pdf | str, Path, bytes, file | Required | Input PDF |
| output_dir | str, Path | "." | Output directory |
| output_name | str | None | Output filename prefix |
| extension | str | "png" | Image format |
| dpi | int | 300 | Image resolution |

## Supported formats

- PNG
- JPG / JPEG
- TIFF
- BMP

## Output

Each PDF page is saved as a separate image.

For example, converting document.pdf generates:

    document_page1.png
    document_page2.png
    document_page3.png

The function returns a list of pathlib.Path objects pointing to the generated images.

## License

This project is licensed under the MIT License.

Note: PyMuPDF is distributed under AGPL-3.0 or a commercial license. Its licensing terms apply independently of this project's license.

See the PyMuPDF licensing information:
https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright

from pathlib import Path
import pymupdf


def pdf_to_images(
    pdf,
    output_dir=".",
    output_name=None,
    extension="png",
    dpi=300
):
    """
    Convert each page of a PDF into an image.

    Parameters
    ----------
    pdf : str, Path, bytes or file-like object
        Input PDF file or binary content.
    output_dir : str or Path
        Output directory.
    output_name : str, optional
        Output filename prefix. Defaults to the PDF filename.
    extension : str
        Image format: png, jpg, jpeg, tif, tiff or bmp.
    dpi : int
        Image resolution. Default is 300.

    Returns
    -------
    list[Path]
        Paths to the generated images.
    """

    extension = extension.lower().lstrip(".")
    formats = {"png", "jpg", "jpeg", "tif", "tiff", "bmp"}

    if extension not in formats:
        raise ValueError(f"Unsupported extension: {extension}")

    if dpi <= 0:
        raise ValueError("DPI must be positive.")

    # Open PDF
    if isinstance(pdf, (str, Path)):
        pdf = Path(pdf)
        doc = pymupdf.open(pdf)
        name = output_name or pdf.stem
    else:
        if hasattr(pdf, "getvalue"):
            pdf = pdf.getvalue()
        elif hasattr(pdf, "read"):
            pdf = pdf.read()

        doc = pymupdf.open(stream=pdf, filetype="pdf")
        name = output_name or "document"

    # Prepare output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    name = Path(name).stem
    zoom = dpi / 72

    images = []

    try:
        # Convert each page
        for i, page in enumerate(doc, start=1):
            pix = page.get_pixmap(
                matrix=pymupdf.Matrix(zoom, zoom),
                alpha=False
            )

            path = output_dir / f"{name}_page{i}.{extension}"
            pix.save(str(path))
            images.append(path)

    finally:
        doc.close()

    return images

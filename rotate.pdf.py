from PyPDF2 import PdfFileReader, PdfFileWriter
import warnings

# Ignore specific warnings
warnings.filterwarnings("ignore", message="Xref table not zero-indexed. ID numbers for objects will be corrected.")

def rotate_pages(pdf_path, output_path, rotations):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)

    for i, rotation in enumerate(rotations):
        try:
            page = pdf_reader.getPage(i)
            if rotation == 'clockwise':
                page.rotateClockwise(90)
            elif rotation == 'counterclockwise':
                page.rotateCounterClockwise(90)
            # No rotation for 'none'
            pdf_writer.addPage(page)
        except IndexError:
            print(f"Page {i} does not exist in the document.")
            break

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    input_path = 'sample_land.pdf'
    output_path = 'rotate_pages.pdf'
    # Define rotations for each page: 'clockwise', 'counterclockwise', or 'none'
    rotations = ['clockwise', 'counterclockwise', 'none']
    rotate_pages(input_path, output_path, rotations)

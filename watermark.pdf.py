from PyPDF2 import PdfFileWriter, PdfFileReader
import warnings

# Ignore specific warnings about xref table
warnings.filterwarnings("ignore", message="Xref table not zero-indexed. ID numbers for objects will be corrected.")

def create_watermark(input_pdf, output, watermark):
    try:
        # Read the watermark PDF
        watermark_obj = PdfFileReader(watermark)
        watermark_page = watermark_obj.getPage(0)

        # Read the input PDF
        pdf_reader = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()

        # Apply watermark to all pages
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.mergePage(watermark_page)  # Merge watermark page with the current page
            pdf_writer.addPage(page)

        # Write the output PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)
        print(f"Watermarked PDF saved as '{output}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_watermark(
        input_pdf='merged.pdf',
        output='watermarked_notebook.pdf',
        watermark='watermark.pdf')

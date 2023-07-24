import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter

def add_image_to_pdf(input_pdf_path, output_pdf_path, image_path, position=(100, 300), size=(100, 100)):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    c.drawImage(image_path, position[0], position[1], size[0], size[1])
    c.save()

    packet.seek(0)

    with open(input_pdf_path, "rb") as filehandle:
        existing_pdf = PdfReader(filehandle)
        new_pdf = PdfReader(packet)
        writer = PdfWriter()

        for page in existing_pdf.pages:
            page.merge_page(new_pdf.pages[0])
            writer.add_page(page)

        with open(output_pdf_path, "wb") as outputStream:
            writer.write(outputStream)


position = (100, 100)
size = (100, 100)
add_image_to_pdf('LAYOUT_DIARIO_DEMANDA_v12.pdf', 'pdf_teste.pdf', 'jvtd.jpg', position=position, size=size)
from django.views.generic import View
from django.http import FileResponse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import PyPDF2
import io
import zipfile

class SplitPDFView(View):
    def post(self, request):
        pdf_file = request.FILES['pdf_file']  # Asegúrate de que el archivo se envíe con este nombre

        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # Create a temporary in-memory file for the zip archive
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            for page_num in range(num_pages):
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])

                # Create a temporary in-memory file for each split PDF
                page_buffer = io.BytesIO()
                pdf_writer.write(page_buffer)
                page_buffer.seek(0)

                # Add the split PDF to the zip archive
                zip_file.writestr(f'page_{page_num + 1}.pdf', page_buffer.read())

        # Set the content type and disposition for the zip file
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="split_pdfs.zip"'

        return response

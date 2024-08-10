from django.views.generic import View
from django.http import FileResponse

import PyPDF2
import os

class MergePDFView(View):
    def post(self, request):
        pdf_files = request.FILES.getlist('pdf_files')  # Obtén una lista de archivos PDF

        pdf_writer = PyPDF2.PdfWriter()

        for pdf_file in pdf_files:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Add all pages from the current file
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        # Crea el archivo PDF combinado
        output_filename = 'merged_pdf.pdf'
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        # Retorna el archivo PDF combinado
        response = FileResponse(open(output_filename, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{output_filename}"'

        # Limpieza del archivo temporal
        os.remove(output_filename)

        return response

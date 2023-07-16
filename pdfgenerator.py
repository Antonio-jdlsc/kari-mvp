from reportlab.pdfgen import canvas


class PDFGenerator:
    def generate_report(self, data):
        # Implementa la lógica para generar el informe en PDF
        pdf_name = f'report_{data["customer_id"]}.pdf'
        pdf = canvas.Canvas(pdf_name)

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, 800, "Informe de Ventas")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 750, f"Cliente: {data['customer_name']}")
        pdf.drawString(50, 720, f"Total de Ventas: {data['total_sales']}")

        pdf.save()

        return pdf_name



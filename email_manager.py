from gmail import GmailClient
from pdfgenerator import PDFGenerator

def send_email_with_attachments(recipient, subject, body, attachments=None):
    gmail_client = GmailClient()
    gmail_client.send_email(recipient, subject, body, attachments)

def send_report_email(recipient, data):
    # Generar el informe en PDF utilizando la clase PDFGenerator
    pdf_generator = PDFGenerator()
    pdf_file = pdf_generator.generate_report(data)

    # Adjuntar el archivo PDF al correo electrónico
    attachments = [pdf_file]

    # Enviar el correo electrónico con el informe adjunto
    subject = 'Informe de ventas'
    body = 'Adjunto encontrarás el informe de ventas. ¡Gracias!'
    send_email_with_attachments(recipient, subject, body, attachments)

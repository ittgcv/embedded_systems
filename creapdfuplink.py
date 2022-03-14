import anvil.server

anvil.server.connect("XSZ7HYCEBQPJDPXLRJEJUNC2-7KYZ3TJAUYOFBT3H")
import anvil.pdf
import anvil.media
from anvil.pdf import PDFRenderer
pdf = anvil.pdf.PDFRenderer(scale=0.75, page_size='Letter').render_form("ReportForm")

anvil.media.write_to_file(pdf, "report.pdf")

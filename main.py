from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(27,678,"Prete, Austin C.")
can.drawString(27,654,"05/11/1997")
address = 650
can.drawString(410,address,"drchrono")
can.drawString(410,address-15,"1001 N Rengstorff Ave.")
can.drawString(410,address-30,"Mountain View, CA 94043")
can.setFont("Helvetica", 7)

date_column = 75
manu_column = 116
admin_column = 220
site_column = 290
vis_column = 262

manu_placeholder = "Merck"
lot_placeholder = "100320"
date_placeholder = "06/15/2015"
admin_placeholder = "06/15/2015"
site_placeholder = "LD"
vis_placeholder = "03/13/2008"

hepB_1 = 549
can.drawString(date_column,hepB_1,date_placeholder)
can.drawString(manu_column,hepB_1+8,manu_placeholder)
can.drawString(manu_column,hepB_1-6,lot_placeholder)
can.drawString(admin_column,hepB_1, admin_placeholder)
can.drawString(site_column,hepB_1+7,site_placeholder)
can.drawString(vis_column,hepB_1-6,vis_placeholder)


hepB_2 = hepB_1-27
can.drawString(date_column,hepB_2,date_placeholder)
can.drawString(manu_column,hepB_2+8, manu_placeholder)
can.drawString(manu_column,hepB_2-6, lot_placeholder)
can.drawString(admin_column,hepB_2, admin_placeholder)
can.drawString(site_column,hepB_2+7,site_placeholder)
can.drawString(vis_column,hepB_2-6,vis_placeholder)

hepB_3 = hepB_2-27
can.drawString(date_column,hepB_3,date_placeholder)
can.drawString(manu_column,hepB_3+8, manu_placeholder)
can.drawString(manu_column,hepB_3-6, lot_placeholder)
can.drawString(admin_column,hepB_3, admin_placeholder)
can.drawString(site_column,hepB_3+7,site_placeholder)
can.drawString(vis_column,hepB_3-6,vis_placeholder)

hepB_4 = hepB_3-27
can.drawString(date_column,hepB_4,date_placeholder)
can.drawString(manu_column,hepB_4+8, manu_placeholder)
can.drawString(manu_column,hepB_4-6, lot_placeholder)
can.drawString(admin_column,hepB_4, admin_placeholder)
can.drawString(site_column,hepB_4+7,site_placeholder)
can.drawString(vis_column,hepB_4-6,vis_placeholder)

rota1 = hepB_4-27
can.drawString(date_column,rota1,date_placeholder)
can.drawString(manu_column,rota1+8,manu_placeholder)
can.drawString(manu_column,rota1-6,lot_placeholder)
can.drawString(admin_column,rota1, admin_placeholder)
can.drawString(site_column,rota1+7,site_placeholder)
can.drawString(vis_column,rota1-6,vis_placeholder)

rota2 = rota1-27
can.drawString(date_column,rota2,date_placeholder)
can.drawString(manu_column,rota2+8,manu_placeholder)
can.drawString(manu_column,rota2-6,lot_placeholder)
can.drawString(admin_column,rota2, admin_placeholder)
can.drawString(site_column,rota2+7,site_placeholder)
can.drawString(vis_column,rota2-6,vis_placeholder)

rota3 = rota2-27
can.drawString(date_column,rota3,date_placeholder)
can.drawString(manu_column,rota3+8,manu_placeholder)
can.drawString(manu_column,rota3-6,lot_placeholder)
can.drawString(admin_column,rota3, admin_placeholder)
can.drawString(site_column,rota3+7,site_placeholder)
can.drawString(vis_column,rota3-6,vis_placeholder)

dtap1 = rota3-27
can.drawString(date_column,dtap1,date_placeholder)
can.drawString(manu_column,dtap1+8,manu_placeholder)
can.drawString(manu_column,dtap1-6,lot_placeholder)
can.drawString(admin_column,dtap1, admin_placeholder)
can.drawString(site_column,dtap1+7,site_placeholder)
can.drawString(vis_column,dtap1-6,vis_placeholder)

dtap2 = dtap1-27
can.drawString(date_column,dtap2,date_placeholder)
can.drawString(manu_column,dtap2+8,manu_placeholder)
can.drawString(manu_column,dtap2-6,lot_placeholder)
can.drawString(admin_column,dtap2, admin_placeholder)
can.drawString(site_column,dtap2+7,site_placeholder)
can.drawString(vis_column,dtap2-6,vis_placeholder)

dtap3 = dtap2-27
can.drawString(date_column,dtap3,date_placeholder)
can.drawString(manu_column,dtap3+8,manu_placeholder)
can.drawString(manu_column,dtap3-6,lot_placeholder)
can.drawString(admin_column,dtap3, admin_placeholder)
can.drawString(site_column,dtap3+7,site_placeholder)
can.drawString(vis_column,dtap3-6,vis_placeholder)

dtap4 = dtap3-27
can.drawString(date_column,dtap4,date_placeholder)
can.drawString(manu_column,dtap4+8,manu_placeholder)
can.drawString(manu_column,dtap4-6,lot_placeholder)
can.drawString(admin_column,dtap4, admin_placeholder)
can.drawString(site_column,dtap4+7,site_placeholder)
can.drawString(vis_column,dtap4-6,vis_placeholder)

dtap5 = dtap4-27
can.drawString(date_column,dtap5,date_placeholder)
can.drawString(manu_column,dtap5+8,manu_placeholder)
can.drawString(manu_column,dtap5-6,lot_placeholder)
can.drawString(admin_column,dtap5, admin_placeholder)
can.drawString(site_column,dtap5+7,site_placeholder)
can.drawString(vis_column,dtap5-6,vis_placeholder)


hib1 = dtap5-27
can.drawString(date_column,hib1,date_placeholder)
can.drawString(manu_column,hib1+8,manu_placeholder)
can.drawString(manu_column,hib1-6,lot_placeholder)
can.drawString(admin_column,hib1, admin_placeholder)
can.drawString(site_column,hib1+7,site_placeholder)
can.drawString(vis_column,hib1-6,vis_placeholder)

hib2 = hib1-27
can.drawString(date_column,hib2,date_placeholder)
can.drawString(manu_column,hib2+8,manu_placeholder)
can.drawString(manu_column,hib2-6,lot_placeholder)
can.drawString(admin_column,hib2, admin_placeholder)
can.drawString(site_column,hib2+7,site_placeholder)
can.drawString(vis_column,hib2-6,vis_placeholder)

hib3 = hib2-27
can.drawString(date_column,hib3,date_placeholder)
can.drawString(manu_column,hib3+8,manu_placeholder)
can.drawString(manu_column,hib3-6,lot_placeholder)
can.drawString(admin_column,hib3, admin_placeholder)
can.drawString(site_column,hib3+7,site_placeholder)
can.drawString(vis_column,hib3-6,vis_placeholder)

hib4 = hib3-27
can.drawString(date_column,hib4,date_placeholder)
can.drawString(manu_column,hib4+8,manu_placeholder)
can.drawString(manu_column,hib4-6,lot_placeholder)
can.drawString(admin_column,hib4, admin_placeholder)
can.drawString(site_column,hib4+7,site_placeholder)
can.drawString(vis_column,hib4-6,vis_placeholder)

date_column += 286
manu_column += 285
admin_column += 285
site_column += 285
vis_column += 285

pc1 = hepB_1
can.drawString(date_column,pc1,date_placeholder)
can.drawString(manu_column,pc1+8,manu_placeholder)
can.drawString(manu_column,pc1-6,lot_placeholder)
can.drawString(admin_column,pc1, admin_placeholder)
can.drawString(site_column,pc1+7,site_placeholder)
can.drawString(vis_column,pc1-6,vis_placeholder)

pc2 = pc1-27
can.drawString(date_column,pc2,date_placeholder)
can.drawString(manu_column,pc2+8,manu_placeholder)
can.drawString(manu_column,pc2-6,lot_placeholder)
can.drawString(admin_column,pc2, admin_placeholder)
can.drawString(site_column,pc2+7,site_placeholder)
can.drawString(vis_column,pc2-6,vis_placeholder)

pc3 = pc2-27
can.drawString(date_column,pc3,date_placeholder)
can.drawString(manu_column,pc3+8,manu_placeholder)
can.drawString(manu_column,pc3-6,lot_placeholder)
can.drawString(admin_column,pc3, admin_placeholder)
can.drawString(site_column,pc3+7,site_placeholder)
can.drawString(vis_column,pc3-6,vis_placeholder)

pc4 = pc3-27
can.drawString(date_column,pc4,date_placeholder)
can.drawString(manu_column,pc4+8,manu_placeholder)
can.drawString(manu_column,pc4-6,lot_placeholder)
can.drawString(admin_column,pc4, admin_placeholder)
can.drawString(site_column,pc4+7,site_placeholder)
can.drawString(vis_column,pc4-6,vis_placeholder)

ipv1 = pc4-27
can.drawString(date_column,ipv1,date_placeholder)
can.drawString(manu_column,ipv1+8,manu_placeholder)
can.drawString(manu_column,ipv1-6,lot_placeholder)
can.drawString(admin_column,ipv1, admin_placeholder)
can.drawString(site_column,ipv1+7,site_placeholder)
can.drawString(vis_column,ipv1-6,vis_placeholder)

ipv2 = ipv1-27
can.drawString(date_column,ipv2,date_placeholder)
can.drawString(manu_column,ipv2+8,manu_placeholder)
can.drawString(manu_column,ipv2-6,lot_placeholder)
can.drawString(admin_column,ipv2, admin_placeholder)
can.drawString(site_column,ipv2+7,site_placeholder)
can.drawString(vis_column,ipv2-6,vis_placeholder)

ipv3 = ipv2-27
can.drawString(date_column,ipv3,date_placeholder)
can.drawString(manu_column,ipv3+8,manu_placeholder)
can.drawString(manu_column,ipv3-6,lot_placeholder)
can.drawString(admin_column,ipv3, admin_placeholder)
can.drawString(site_column,ipv3+7,site_placeholder)
can.drawString(vis_column,ipv3-6,vis_placeholder)

ipv4 = ipv3-27
can.drawString(date_column,ipv4,date_placeholder)
can.drawString(manu_column,ipv4+8,manu_placeholder)
can.drawString(manu_column,ipv4-6,lot_placeholder)
can.drawString(admin_column,ipv4, admin_placeholder)
can.drawString(site_column,ipv4+7,site_placeholder)
can.drawString(vis_column,ipv4-6,vis_placeholder)

mmr1 = ipv4-27
can.drawString(date_column,mmr1,date_placeholder)
can.drawString(manu_column,mmr1+8,manu_placeholder)
can.drawString(manu_column,mmr1-6,lot_placeholder)
can.drawString(admin_column,mmr1,admin_placeholder)
can.drawString(site_column,mmr1+7,site_placeholder)
can.drawString(vis_column,mmr1-6,vis_placeholder)


mmr2 = mmr1-27
can.drawString(date_column,mmr2,date_placeholder)
can.drawString(manu_column,mmr2+8,manu_placeholder)
can.drawString(manu_column,mmr2-6,lot_placeholder)
can.drawString(admin_column,mmr2,admin_placeholder)
can.drawString(site_column,mmr2+7,site_placeholder)
can.drawString(vis_column,mmr2-6,vis_placeholder)

var1 = mmr2-27
can.drawString(date_column,var1,date_placeholder)
can.drawString(manu_column,var1+8,manu_placeholder)
can.drawString(manu_column,var1-6,lot_placeholder)
can.drawString(admin_column,var1,admin_placeholder)
can.drawString(site_column,var1+7,site_placeholder)
can.drawString(vis_column,var1-6,vis_placeholder)

var2 = var1-27
can.drawString(date_column,var2,date_placeholder)
can.drawString(manu_column,var2+8,manu_placeholder)
can.drawString(manu_column,var2-6,lot_placeholder)
can.drawString(admin_column,var2,admin_placeholder)
can.drawString(site_column,var2+7,site_placeholder)
can.drawString(vis_column,var2-6,vis_placeholder)

hepA1 = var2-27
can.drawString(date_column,hepA1,date_placeholder)
can.drawString(manu_column,hepA1+8,manu_placeholder)
can.drawString(manu_column,hepA1-6,lot_placeholder)
can.drawString(admin_column,hepA1,admin_placeholder)
can.drawString(site_column,hepA1+7,site_placeholder)
can.drawString(vis_column,hepA1-6,vis_placeholder)

hepA2 = hepA1-27
can.drawString(date_column,hepA2,date_placeholder)
can.drawString(manu_column,hepA2+8,manu_placeholder)
can.drawString(manu_column,hepA2-6,lot_placeholder)
can.drawString(admin_column,hepA2,admin_placeholder)
can.drawString(site_column,hepA2+7,site_placeholder)
can.drawString(vis_column,hepA2-6,vis_placeholder)

can.showPage()

date_column = 74
manu_column = 113
admin_column = 217
site_column = 290
vis_column = 262

can.setFont("Helvetica", 7)

flu1=672
can.drawString(date_column,flu1,date_placeholder)
can.drawString(manu_column,flu1+8,manu_placeholder)
can.drawString(manu_column,flu1-6,lot_placeholder)
can.drawString(admin_column,flu1, admin_placeholder)
can.drawString(site_column,flu1+7,site_placeholder)
can.drawString(vis_column,flu1-6,vis_placeholder)

flu2=flu1-27
can.drawString(date_column,flu2,date_placeholder)
can.drawString(manu_column,flu2+8,manu_placeholder)
can.drawString(manu_column,flu2-6,lot_placeholder)
can.drawString(admin_column,flu2, admin_placeholder)
can.drawString(site_column,flu2+7,site_placeholder)
can.drawString(vis_column,flu2-6,vis_placeholder)


can.save()


#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("sample.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page2 = existing_pdf.getPage(1)
page.mergePage(new_pdf.getPage(0))
page2.mergePage(new_pdf.getPage(1))
output.addPage(page)
output.addPage(page2)
# finally, write "output" to a real file
outputStream = file("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
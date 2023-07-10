import veryfi
import pandas as pd
from ast import literal_eval

client_id= "vrfURyLUDpZ2UzVcfxht8OPrDcrE88BKea6jxYS"
client_secret ="FFAMYPcjhJvxzcSo3AJhzFTuSaIeIjbePZIgTuOkduc8tKSLEzFbnGdZTW3uyJIP96WaB8168wcBnZj1P6y9AeT2GDMpBbuJlrJ4ykegmk4LuTxcj1xfo8Ark1koHtMg"
username = "nirbodhmamun"
api_key ="254a5a7342b5c8a0c0400a64db432bf5"

client = veryfi.Client(client_id,client_secret,username,api_key)

categories = ["Grocery","datapack","internate pack", "Tax Chalan", "chalan", "invoice", "Job Supplies and Materials","product"]

json_result = client.process_document("/Users/shahriar/OfficeWorks/PDF_Extractor_new/pdf/invoice.pdf",categories)

print(json_result)
print("main invoice",json_result["line_items"])
print(type(json_result["line_items"]))
# data = pd.read_json(json_result["ocr_text"])
#
# data.to_excel("/Users/shahriar/OfficeWorks/PDF_Extractor_new/pdf/invoice.xlxs",index=False)
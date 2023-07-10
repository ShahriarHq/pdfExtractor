from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import json
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


template = read_templates("Template/")
print(template)

result = extract_data('pdf/invoice.pdf', templates=template)
print(result)

with open("Shopoth.json", "w") as outfile:
    json.dump(result, outfile, indent=4, cls=DateTimeEncoder)

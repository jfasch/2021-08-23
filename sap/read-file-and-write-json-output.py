import sys
import sap
import json

my_records_for_json = []

for r in sap.read_sap_file(sys.argv[1]):
    rec = {
        'material': r.material,
        'werk': r.werk,
        'lort': r.lort,
        'b': r.b,
        'charge': r.charge,
        's': r.s,
        'sonderbestandsnummer': r.sonderbestandsnummer,
        'materialkurztext': r.materialkurztext,
        'typ': r.typ,
        'lagerplatz': r.lagerplatz,
        'verfueg_bestand': r.verfueg_bestand,
        'bme': r.bme,
        'we_datum': str(r.we_datum),
    }
    my_records_for_json.append(rec)

print(json.dumps(my_records_for_json))

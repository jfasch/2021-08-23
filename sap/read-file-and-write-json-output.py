import sys
import sap
import json

my_records_for_json = []

for r in sap.read_sap_file(sys.argv[1]):
    # argh. read_sap_file() produces record with datetime.datetime
    # objects (we_datum), but json cannot handle those. convert them
    # back to strings where they came from originally.
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

# create a string in JSON format, and print it out
json_text = json.dumps(my_records_for_json)
print(json_text)

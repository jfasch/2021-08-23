import sys
import pprint

from . import sap


records = sap.read_sap_file(sys.argv[1])
for r in records:
    #pprint.pprint(r, indent=4)
    print(
        'Material:', r.material, '\n',
        'Werk:', r.werk, '\n',
        'LOrt:', r.lort, '\n',
        'B:', r.b, '\n',
        'Charge:', r.charge, '\n',
        'S:', r.s, '\n',
        'Sonderbestandsnummer:', r.sonderbestandsnummer, '\n',
        'Materialkurztext:', r.materialkurztext, '\n',
        'Typ:', r.typ, '\n',
        'Lagerplatz:', r.lagerplatz, '\n',
        'Verfüg.Bestand:', r.verfueg_bestand, '\n',
        'BME:', r.bme, '\n',
        'WE-Datum:', r.we_datum, '\n',
    )

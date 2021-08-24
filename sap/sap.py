'''
This module contains central functionality to read bloody SAP files
'''

from collections import namedtuple
from datetime import datetime


Record = namedtuple('Record', [
    'material',
    'werk',
    'lort',
    'b',
    'charge',
    's',
    'sonderbestandsnummer',
    'materialkurztext',
    'typ',
    'lagerplatz',
    'verfueg_bestand',
    'bme',
    'we_datum',
])

def read_sap_file(filename):
    data = []
    f = open(filename)
    for line in f:
        fields = line.split('|')

        record = Record(
            material=int(fields[1].strip()),
            werk=fields[2].strip(),
            lort=fields[3].strip(),
            b=fields[4].strip() or None,
            charge=fields[5].strip() or None,
            s=fields[6].strip() or None,
            sonderbestandsnummer=fields[7].strip() or None,
            materialkurztext=fields[8].strip(),
            typ=fields[9].strip(),
            lagerplatz=fields[10].strip(),
            verfueg_bestand=fields[11].strip(),
            bme=fields[12].strip(),
            we_datum=datetime.strptime(fields[13].strip(), '%d.%m.%Y')
        )
        
        data.append(record)

    return data

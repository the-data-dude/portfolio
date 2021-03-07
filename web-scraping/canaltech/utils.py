from datetime import datetime

def to_datetime(stringdt, stringhour):

    monthdict = {
        'JANEIRO' : '01',
        'FEVEREIRO' : '02',
        'MARÇO' : '03',
        'ABRIL' : '04',
        'MAIO' : '05',
        'JUNHO' : '06',
        'JULHO' : '07',
        'AGOSTO' : '08',
        'SETEMBRO': '09',
        'OUTUBRO' : '10',
        'NOVEMBRO' : '11',
        'DEZEMBRO' : '12'
    }

    day, month, year = stringdt.split(" ")
    
    month = monthdict[month.upper()]

    newdt = datetime.strptime(year + '-' + month + "-" + day + " " + stringhour, '%Y-%m-%d %H:%M')

    return newdt

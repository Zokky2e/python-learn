import csv
from SolarPanel import SolarPanel

def importPanels(location) -> list[SolarPanel]:
    solar_panels = []
    with open(location, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            solar_panel = SolarPanel(
                row['Serialnummer'],
                float(row['PMPP']), 
                float(row['UOC']), 
                float(row['ISC']), 
                float(row['UMPP']), 
                float(row['IMPP']), 
                float(row['FF']), 
                row['Palettennummer']
            )
            solar_panels.append(solar_panel)

    return solar_panels


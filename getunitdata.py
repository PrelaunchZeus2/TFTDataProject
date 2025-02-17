import json, csv

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def scrape_units(data):
    units = []
    for i in range(0,8):
        for champ in data['setData'][i]['champions']:
            api_name = champ.get('apiName', 'Unknown')
            unit_name = api_name.split('_')[1]
            set_number = api_name.split('_')[0][3:] if api_name.startswith('TFT') else 'Unknown'
            unit = {
                'name': unit_name,
                'set': set_number,
                'cost': champ.get('cost', 'Unknown'),
                'role': champ.get('role', 'Unknown'),
            
                'traits': champ.get('traits', [])
            }
            units.append(unit)
    return units

def save_to_csv(units, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'set', 'cost', 'role', 'traits']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for unit in units:
            writer.writerow({
                'name': unit['name'],
                'set': unit['set'],
                'cost': unit['cost'],
                'role': unit['role'],
                'traits': ', '.join(unit['traits'])
            })

def main():
    json_file_path = 'units_en_us.json'
    csv_file_path = 'units.csv'
    data = load_json(json_file_path)
    units = scrape_units(data)
    save_to_csv(units, csv_file_path)

if __name__ == "__main__":
    main()
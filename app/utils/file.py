import csv, json
import pandas as pd

class FileUtils():
    def __init__(self):
        pass

    async def open_csv_file(self, path):
        rows = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                processed_row = await self.process_row(row)
                rows.append(processed_row)
        return rows

    async def open_text_file(self, path):
        with open(path, 'r') as f:
            return f.read()

    async def open_json_file(self, path):
        with open(path) as json_file:
            json_data = json.load(json_file)
            return json_data

    async def process_row(self, row):
        # Perform some processing on each row asynchronously
        return row

    def convert_libraries_csv_to_json(self):
        df = pd.read_csv('app/schemas/libraries.csv')
        libraries_json = df.to_json(orient='records')
        return libraries_json

    async def get_libraries_csv(self):
        libraries_csv = await self.open_csv_file('app/schemas/libraries.csv')
        return libraries_csv

    async def get_libraries_json(self):
        libraries_json = await self.open_json_file('app/schemas/libraries.json')
        return libraries_json

    # https://stackoverflow.com/questions/10574520/extract-json-from-text
    async def get_json_from_paragraph(self, paragraph):
        right_indices = [i for i, c in enumerate(paragraph) if c == '}']
        i = 0
        while i < len(paragraph) - 1:
            if paragraph[i] == '{':
                for j in right_indices:
                    if i < j:
                        try:
                            result = json.loads(paragraph[i: j + 1])
                            i = j + 1
                            break
                        except json.decoder.JSONDecodeError:
                            pass
            i += 1
        return result

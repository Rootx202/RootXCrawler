"""Support for exporting the results."""
import csv
import json
import os
import sqlite3
import html


def exporter(directory, method, datasets):
    """Export the results."""
    if method.lower() == 'json':
        # Convert json_dict to a JSON styled string
        json_string = json.dumps(datasets, indent=4)
        savefile = open('{}/exported.json'.format(directory), 'w+')
        savefile.write(json_string)
        savefile.close()

    if method.lower() == 'csv':
        with open('{}/exported.csv'.format(directory), 'w+') as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for key, values in datasets.items():
                if values is None:
                    csv_writer.writerow([key])
                else:
                    csv_writer.writerow([key] + values)
        csvfile.close()

    if method.lower() == 'html':
        html_path = os.path.join(directory, 'exported.html')
        with open(html_path, 'w+', encoding='utf-8') as outfile:
            outfile.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
            outfile.write('<meta charset="utf-8">\n<title>RootXCrawler Report</title>\n')
            outfile.write('<style>body{font-family:Arial,sans-serif;background:#f9f9f9;color:#222;}')
            outfile.write('table{border-collapse:collapse;width:100%;margin-bottom:1.5rem;}')
            outfile.write('th,td{border:1px solid #ddd;padding:0.5rem;text-align:left;}')
            outfile.write('th{background:#333;color:#fff;}</style>\n</head>\n<body>\n')
            outfile.write('<h1>RootXCrawler Report</h1>\n')
            for key, values in datasets.items():
                outfile.write('<h2>%s (%s)</h2>\n' % (html.escape(key.capitalize()), len(values)))
                outfile.write('<table>\n<tr><th>Result</th></tr>\n')
                for value in values:
                    outfile.write('<tr><td>%s</td></tr>\n' % html.escape(str(value)))
                outfile.write('</table>\n')
            outfile.write('</body>\n</html>')

    if method.lower() == 'sqlite':
        db_path = os.path.join(directory, 'exported.db')
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        for key, values in datasets.items():
            table_name = 'dataset_%s' % key.replace('-', '_')
            cursor.execute('CREATE TABLE IF NOT EXISTS %s (value TEXT)' % table_name)
            cursor.executemany(
                'INSERT INTO %s (value) VALUES (?)' % table_name,
                [(str(value),) for value in values]
            )
        connection.commit()
        connection.close()

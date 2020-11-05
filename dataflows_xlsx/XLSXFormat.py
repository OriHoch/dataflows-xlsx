import os
import openpyxl
import datetime
from dataflows.processors.dumpers.file_formats import CSVFormat


class XLSXWriter(object):

    def __init__(self, file, headers, schema, titles=None):
        self.file = file
        self.headers = headers
        self.schema = schema
        self.schema_fields = {f.name: f for f in self.schema.fields}
        self.workbook = openpyxl.Workbook()
        self.workbook.active.append(titles or self.headers)

    def writerow(self, row):
        cells = []
        for field_name in self.headers:
            value = row[field_name]
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, list):
                value = ', '.join(map(str, value))
            else:
                try:
                    field_type = self.schema_fields[field_name].type
                    if field_type == 'integer':
                        value = int(value)
                    elif field_type == 'number':
                        value = float(value)
                except:
                    pass
            cells.append(value)
        self.workbook.active.append(cells)

    def finalize_file(self):
        self.workbook.save(self.file.name)


class XLSXFormat(CSVFormat):

    def __init__(self, file, schema, use_titles=False, **kwargs):
        headers = [f.name for f in schema.fields]
        if use_titles:
            titles = [f.descriptor.get('title', f.name) for f in schema.fields]
            xlsx_writer = XLSXWriter(file, headers, schema, titles)
        else:
            xlsx_writer = XLSXWriter(file, headers, schema)
        super(CSVFormat, self).__init__(xlsx_writer, schema)

    @classmethod
    def prepare_resource(cls, resource):
        descriptor = resource.descriptor
        basename, _ = os.path.splitext(descriptor['path'])
        descriptor['path'] = basename + '.xlsx'
        descriptor['format'] = 'xlsx'
        super(CSVFormat, cls).prepare_resource(resource)

    def finalize_file(self):
        self.writer.finalize_file()

import os
from datapackage import Resource
from dataflows.processors.dumpers.file_formats import CSVFormat, JSONFormat
from dataflows.processors.dumpers.to_path import PathDumper as dataflows_PathDumper, FileDumper
from .XLSXFormat import XLSXFormat


class PathDumper(dataflows_PathDumper):

    def process_datapackage(self, datapackage):
        datapackage = super(FileDumper, self).process_datapackage(datapackage)

        self.file_formatters = {}

        # Make sure all resources are proper CSVs
        resource: Resource = None
        for i, resource in enumerate(datapackage.resources):
            if self.force_format:
                file_format = self.forced_format
            else:
                _, file_format = os.path.splitext(resource.source)
                file_format = file_format[1:]
            file_formatter = {
                'csv': CSVFormat,
                'json': JSONFormat,
                'xlsx': XLSXFormat,
            }.get(file_format)
            if file_format is not None:
                if file_format == 'xlsx':
                    self.resource_hash = None
                self.file_formatters[resource.name] = file_formatter
                self.file_formatters[resource.name].prepare_resource(resource)
                resource.commit()
                datapackage.descriptor['resources'][i] = resource.descriptor

        return datapackage

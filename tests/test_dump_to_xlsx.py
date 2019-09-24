import os
from dataflows import Flow
from dataflows_xlsx import dump_to_path


def get_data():
    for i in range(10):
        yield {'i': i, 'foo': 'bar{}'.format(i)}


Flow(
    [{'i': i, 'foo': 'bar{}'.format(i)} for i in range(10)],
    dump_to_path('tests/data/test_dump_to_xlsx', format='xlsx')
).process()


assert os.path.isfile('tests/data/test_dump_to_xlsx/res_1.xlsx')
assert os.path.isfile('tests/data/test_dump_to_xlsx/datapackage.json')
assert os.path.getsize('tests/data/test_dump_to_xlsx/datapackage.json') > 200
assert os.path.getsize('tests/data/test_dump_to_xlsx/res_1.xlsx') > 2000

print('OK')

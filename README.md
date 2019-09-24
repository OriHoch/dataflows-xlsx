# dataflows-xlsx

Dataflows support for xlsx files

## Install

`python3 -m pip install -e git+https://github.com/OriHoch/dataflows-xlsx.git@master#egg=dataflows-xlsx`

## Writing xlsx files

Import the dump_to_path processor from dataflows_xlsx:

`from dataflows_xlsx import dump_to_path`

Use it with `format='xlsx'` argument to save xlsx files

`dump_to_path('out-path', format='xlsx')`

Full example:

```
from dataflows import Flow
from dataflows_xlsx import dump_to_path

Flow(
    [{'i': i, 'foo': 'bar{}'.format(i)} for i in range(10)],
    dump_to_path('tests/data/test_dump_to_xlsx', format='xlsx')
).process()
```

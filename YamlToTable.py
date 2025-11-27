#!/usr/bin/env python

import yaml, sys, re

FN_TEMPLATE = "content/tables/LogTableWeek{n}.md"

def main():
    fn = sys.argv[1]
    weekn = re.findall(r'\d+', fn)[0]
    fnOut = FN_TEMPLATE.replace('{n}', weekn)
    with open(fn, 'r') as f:
        table = yaml.safe_load(f.read())['table']

    final = createTable(table)
    print(final)

def createTable(table: dict) -> str:
    headers: list = table['headers']
    rows: list = table['rows']

    tableStr: str = ''

    tableStr += '|'
    for head in headers:
        tableStr += head + '|'
    tableStr += '\n'

    tableStr += '|'
    for n in range(len(headers)):
        tableStr += ' --- ' + '|'
    tableStr += '\n'

    for row in rows:
        tableStr += '|'
        for col in row:
            tableStr += col.replace('\n', '<br/>') + '|'
        tableStr += '\n'
    tableStr += '\n'
    return tableStr

def publishTable(final: str, fnOut: str):
    with open(fnOut, 'w') as f:
        f.write(final)

if __name__ == '__main__':
    main()

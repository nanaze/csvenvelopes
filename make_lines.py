import sys

def _SplitLine(line):
  line = line.strip()
  parts = line.split('\t')

  while len(parts) < 6:
    parts.append('')

  return parts

    
def _AppendIfNotEmpty(lines, field):
  field = field.strip()
  if field:
    lines.append(field)

def main():
  for line in sys.stdin:
    parts = _SplitLine(line)

    out_lines = []
    _AppendIfNotEmpty(out_lines, parts[0])
    _AppendIfNotEmpty(out_lines, parts[1])
    _AppendIfNotEmpty(out_lines, parts[2])    

    city, state, zip_code = parts[3:6]
    city_line = '%s, %s %s' % (city, state, zip_code)
    out_lines.append(city_line)

    out_line = '\t'.join(out_lines)
    print out_line

if __name__ == '__main__':
  main()

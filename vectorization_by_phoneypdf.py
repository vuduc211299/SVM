def vectorization_phoneypdf(path):
  listVectors = []
  with open(path) as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
      if "--eof--" in lines[i]:
        v = []
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        i += 1
        v.append((lines[i].split(' ')[0], lines[i].split(' ')[2].replace('\n','')))
        # v = sorted(v, key=lambda x: x[0])
        listVectors.append(v)
      i += 1
    
    result = []
    # result_name = []
    for v in listVectors:
      v = sorted(v, key=lambda x: x[0])
      value = []
      name = []
      for x in v:
        value.append(x[1])
        name.append(x[0])

      result.append(value)
      # result_name.append(name)

    return result;

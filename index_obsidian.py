file_name = raw_input('File name: ')
file = open(file_name,'r')
Lines = file.readlines()
file.close()
file = open(file_name,'w')
file.write('---\n#### index\n')
for line in Lines:
  if(line.startswith('![[')):
    line = '##### ' + line[3:] 
    if(']]' in line):
      line = line[0:len(line)-3]
    file.write(line + '\n')
file.close()
  
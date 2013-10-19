#url
def listing(request, sub):
  import os
  from django.shortcuts import render
  cxt = { }
  if sub == '':
    cxt['dir_name'] = '/var/log'
    cxt['dir_content'] = os.listdir('/var/log')
  else:
    cxt['dir_name'] = '/var/log' + '/' + str(sub)
    cxt['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  return render(request, 'listing.html', cxt)

  
#подпапки
def listing(request, sub):
  import os
  from django.shortcuts import render
  cxt = { }
  dir_name = '/var/log' + '/' + str(sub)
  cxt['dir_name'] = dir_name
  cxt['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  cxt['dir'] = []
  cxt['f'] = []
  for f in cxt['dir_content']:
    fullname = os.path.join(dir_name, f)
    if os.path.isdir(fullname):
      cxt['dir'].append(f)
    else:
      cxt['f'].append(f)
  return render(request, '../t/listing.html', cxt)


#таблицы
def listing(request, sub):
  import os
  import time
  from django.shortcuts import render
  cxt = { }
  dir_name = '/var/log' + '/' + str(sub)
  cxt['dir_name'] = dir_name
  cxt['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  cxt['tbl_content'] = []
  for f in cxt['dir_content']:
    row = []
    fullname = os.path.join(dir_name, f)
    sz = os.path.getsize(fullname)
    stat = os.stat(fullname)
    t = time.localtime(stat.st_mtime)
    ct = str(t[2])+'/'+str(t[1])+'/'+str(t[0])+' '+str(t[3])+':'+str(t[4])+':'+str(t[5])
    row.append(f)
    row.append(sz)
    row.append(ct)
    cxt['tbl_content'].append(row)
  return render(request, 'listing.html', cxt)


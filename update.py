import re, json, datetime, urllib.request
URL='https://www.teslafi.com/firmware.php?detail=2026.20.300'
FW='2026.20.300'
req=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0 FirmwareJailWatch/1.0'})
html=urllib.request.urlopen(req,timeout=30).read().decode('utf-8','ignore')
text=re.sub(r'<script.*?</script>|<style.*?</style>',' ',html,flags=re.S|re.I)
text=re.sub(r'<[^>]+>',' ',text); text=re.sub(r'&nbsp;',' ',text); text=re.sub(r'\s+',' ',text)
# Current total: first All row after Current Installs
m=re.search(r'Current Installs.*?All\s+(\d+)\s+0\s+0\s+0\s+0\s+0\s+(\d+)',text,re.I)
if not m: raise RuntimeError('Could not parse Current Installs')
current=int(m.group(1))
models={}
for model in ['Model S','Model X','Model 3','Model Y','Cybertruck']:
    mm=re.search(re.escape(model)+r'\s+(\d+)\s+0\s+0\s+0\s+0\s+0\s+\d+',text,re.I)
    if mm and int(mm.group(1)): models[model]=int(mm.group(1))
# Parse Next Version Installed section only
next_versions={}
sec=re.search(r'Next Version Installed(.*?)Current Installs',text,re.S|re.I)
if sec:
    for v,n in re.findall(r'(20\d\d\.\d+(?:\.\d+){0,2})[^0-9]+(\d+)\s+\d+%',sec.group(1)):
        next_versions[v]=int(n)
freed=sum(next_versions.values())
out={'firmware':FW,'source':URL,'current_installs':current,'total_freed':freed,'next_versions':next_versions,'models':models,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'Updated automatically from TeslaFi.'}
open('data.json','w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

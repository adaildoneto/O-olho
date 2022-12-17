import json

def thunder():
  postt = open('thunder.json')
  thunder = json.loads(postt.read())

  return thunder


def thundera():
  postt = open('thundera.json')
  thundera = json.loads(postt.read())

  return thundera

def log():
  postl = open('log.json')
  logi = json.loads(postl.read())

  return logi

def pdate():
  log1 = log()
  pdate = log1[-1]
  return pdate
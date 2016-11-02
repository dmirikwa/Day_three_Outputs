def find_missing(a,b):
  if(isinstance(a,list) and isinstance(b,list)):
    if(len(a)==len(b)):
      return 0
    else:
      if(len(b)>len(a)):
        for i in b:
          if(i not in a):
            return i
          else:
            continue
      else:
        for i in a:
          if(i not in b):
            return i
          else:
            continue
  else:
    raise ValueError
    

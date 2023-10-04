while(True):
  string = input()
  key = 0
  ps = []
  stack = []

  if string == '.':
      break
    
  for _ in string:
    if _ == '('or _ == '['or _ == ')'or _ == ']':
      ps.append(_)
      
  for _ in ps:
    if _ == '(' or _ == '[':
      stack.append(_)

    elif stack:
      if _ == ')' and stack[-1] == '(':
        stack.pop()
      elif _ == ']' and stack[-1] == '[':
        stack.pop()
      else:
        print("no")
        key = 1
        break
    else:
      print("no")
      key = 1
      break
  if stack and key ==0:
    key = 1
    print("no")
  if key == 0:
    print("yes")
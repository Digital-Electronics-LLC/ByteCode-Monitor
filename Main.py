print("ByteCodeMon 1.0")
print("Translate Python to Bytecode")
print("Type 'q' to quit")
import dis
while True:
  x = input(">")
  if x == "q":
    break
  else:
    dis.dis(x)

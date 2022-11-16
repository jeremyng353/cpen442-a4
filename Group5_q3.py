''' NOTE: This file will edit the existing Group5.program1.exe file, 
    once the script finishes running, you can run that exe file with your new password'''

''' README: To run this file try something like:
    OPTION1: py Group5_q3.py
    OPTION2: py Group5_q3.py --new_password "YOUR_PASSWORD_GOES_HERE"

    Current password is password
'''

import hashlib
import argparse
import binascii

def hash(password):
    #source: sam_a4_home.py
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def change_password(password):
    hashed_new_password = hash(password)
    print("hash of the new password = " + str(hashed_new_password))

    # Offset where current password's has is stored
    my_hex_offset = "01d3e3"

    # convert the hex offset to int, source: https://blog.finxter.com/how-to-convert-hex-string-to-integer-in-python/
    my_int_offset = int(my_hex_offset, base=16)
    print("Offset for stored hash = " + str(my_int_offset))

    # source : https://www.tutorialsteacher.com/python/python-read-write-file#:~:text=The%20open()%20function%20opens,in%20binary%20format%20for%20writing.
    # open the binary file with read and write permission
    f=open("Group5.program2.exe","r+b")

    # change the offset of the file to where hash is stored
    f.seek(my_int_offset)
    i=0

    # change the 20 byte long hash to the new password's hash
    read_bytes = f.read(20)
    hex_read_bytes = binascii.hexlify(read_bytes)
    print("bytes read " + str(hex_read_bytes))
    n = f.tell()
    print("Offset is now at: " + str(n))

    print("Changing offset back to where hash starts")
    f.seek(my_int_offset)
    n = f.tell()
    print("Offset is now at: " + str(n))


    # source: https://www.folkstalk.com/2022/10/python-hex-to-bytes-string-with-code-examples.html
    byte_array = bytearray.fromhex(hashed_new_password)
    #write the new hash to the offset
    write_bytes = f.write(byte_array)
    print("write_bytes = "+str(write_bytes))
    n = f.tell()
    print("Offset is now at: " + str(n))

    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Program to change the application password for Group5.program2.exe file.')
    parser.add_argument("--new_password", help="Changes the password.")
    args = parser.parse_args()
    new_password = args.new_password
    print("New password entered = " + str(new_password))
    while new_password is None:
        new_password = input("Password cannot be null, please enter your new password: ")
    
    #source: https://stackabuse.com/python-check-if-string-contains-substring/
    while (' ') in new_password:
        new_password = input("Password cannot contain space, please enter your new password: ")
    change_password(new_password)

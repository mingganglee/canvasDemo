import sqlite3

def converToBinaryData(filename):
    # Conver digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    
    return
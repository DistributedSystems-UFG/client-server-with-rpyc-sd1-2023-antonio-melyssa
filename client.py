import rpyc
from constRPYC import * #-
conn = rpyc.connect(SERVER, PORT) # Connect to the server

def command_help():
  print("Available commands:")
  print("-help : print this help")
  print("-append : append a value to the list")
  print("-value : return the list")
  print("-search : search a value in the list")
  print("-order : order the list")
  print("-biggest :  return the biggest value in the list")
  print("-mean : return the mean of the list")
  print("-lowest : return the lowest value in the list")
  print("-exit")

def command_append():
  data = input("Type a value to append: ")
  print(conn.root.exposed_append(data))

def command_value():
  print(conn.root.exposed_value())

def command_search():
  data = input("Type a value to search:")
  print(conn.root.exposed_search(data))

def command_order():
  print(conn.root.exposed_order())

def command_biggest():
  print(conn.root.exposed_biggest())

def command_mean():
  print(conn.root.exposed_mean())

def command_smaller():
  print(conn.root.exposed_smaller())

def command_exit():
  print("Exiting...")
  exit()


class Client:
  

  def exec_command(command):
    if command == 'help':
        command_help()
    elif command == 'exit':
        command_exit()
    elif command == 'append':
        command_append()
    elif command == 'value':
        command_value()
    elif command == 'search': 
        command_search()
    elif command == 'order':
        command_order()
    else:
        print("Unknown command. Type 'help' for a list of available commands.")

  while True:
      i = input("Type a command: ")
      print("Command typed: " + i)
      exec_command(i)
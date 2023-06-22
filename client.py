import rpyc
from constRPYC import * #-




class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server

  def command_help():
      print("Available commands:")
      print("-help")
      print("-append")
      print("-value")
      print("-search")
      print("-order")
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

  def command_exit():
      print("Exiting...")
      exit()

  def exec_command(command):
    if command == 'help':
        self.command_help()
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
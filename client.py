import rpyc
from constRPYC import * #-




class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server

  def exec_command(command):
    if command == '-help':
        command_help()
    elif command == '-exit':
        command_exit()
    else:
        print("Comando desconhecido. Digite 'ajuda' para obter uma lista de comandos disponíveis.")

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

  while True:
      command = input("Type a command: ")
      exec_command(command)
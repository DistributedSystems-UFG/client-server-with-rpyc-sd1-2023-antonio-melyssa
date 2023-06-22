import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [int(data)]
    return self.value

  def exposed_value(self):
    return self.value
  
  def exposed_search(self, data):
    return data in self.value

  def exposed_order(self):
    self.value.sort()
    return self.value

  def exposed_biggest(self):
    return max(self.value)
  
  def exposed_mean(self):
    return sum(self.value)/len(self.value)
  
  def exposed_lowest(self):
    return min(self.value)



if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()


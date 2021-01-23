import requests
from requests.exceptions import HTTPError, URLRequired
import textwrap



class Launches:
  """
  The Launches class uses the response from the r/SpaceX API to create a collection of launch data for me to use later, mainly to output to stdout
  """
  def __init__(self, rocketSerial=0, missionName="", droneShip="", payload="", missionDescription=""):
    if missionName == "":
      self.__missionName = "NOT FOUND"
    else:
      self.__missionName = missionName
    
    if rocketSerial == 0:
      self.__rocketSerial = "NOT FOUND"
    else:
      self.__rocketSerial = rocketSerial
    
    if droneShip == "":
      self.__droneShip = "NOT FOUND"
    else:
      self.__droneShip = droneShip
    
    if payload == "":
      self.__payload = "NOT FOUND"
    else:
      self.__payload = payload

    if missionDescription == "":
      self.__missionDescription = "NOT FOUND"
    else:
      self.__missionDescription = missionDescription
    
    
  def __str__(self):
    """
    Prints infos stored in the Launches class or a class instance to stdout
    """
    wrappedMissionDescription = textwrap.wrap(self.__missionDescription)
    print("Launch Info".center(80))
    print()
    print(f"Mission Name: {self.__missionName}")
    print()
    print(f"Payload: {self.__payload}")
    print()
    print(f"Booster Serial #: {self.__rocketSerial}")
    print()
    print(f"Landing Zone Name: {self.__droneShip}")
    print()
    print("Mission Description:", end="\n");
    for each in wrappedMissionDescription: print(f"{each}")
    print()
    print(f"Webcast Link: {self.__webcastLink}")
    return ""


  def updateValues(self, payload, rocketSerial, jsonResponse):
    """
    A stub method of sorts to allow me to call one method in order to update everything about a new Launches instance
    """
    self.updatePayload(id=payload)
    self.updateRocketSerial(id=rocketSerial)
    self.updateDroneshipName(jsonResponse)
    self.updateMissionDescription(jsonResponse)
    self.updateLivestreamLink(jsonResponse)

  # Ok so I realize this can be a bit confusing and why I did things in a seemingly weird way is not necessarily explained by just reading the code. I can't call the updater methods in __init__ because they would throw a not found error. So I have to call them later on, in this case updateValues() is called from createLaunchObject() in order to run the three updater methods so that __str__() has proper values to display to the user

  def updatePayload(self, id):
    """
    Queries the API for payload info and updates the private payload name var in the class instance
    """
    id = str(id)
    url = str("http://api.spacexdata.com/v4/payloads/" + id)
    try:
      response = requests.get(url)
      response.raise_for_status()
      jsonResponse = response.json()
      payload = jsonResponse["name"]
      self.__payload = payload
      return 
    except HTTPError as http_err:
      print(f"HTTP error occured: {http_err}")
      return
    except Exception as err:
      print(f"Other error occured: {err}")
      return

  def updateRocketSerial(self, id):
    """
    Queries API for infos and then updates the private var in the class instance
    """
    serial = str(id)
    url = str("http://api.spacexdata.com/v4/cores/" + serial)
    try:
      response = requests.get(url)
      response.raise_for_status()
      jsonResponse = response.json()
      rocketSerial = str(jsonResponse["serial"])
      reuseCount = str(jsonResponse["reuse_count"])
      self.__rocketSerial = str(rocketSerial + "." + reuseCount)
      return
    except HTTPError as http_err:
      print(f"HTTP error occured: {http_err}")
      return
    except Exception as err:
      print(f"Other error occured: {err}")
      return

  def updateDroneshipName(self, jsonResponse):
    """
    Queries API for droneship info and then updates the class instance 
    """
    shipID = str(jsonResponse["cores"][0]["landpad"])
    url = str("http://api.spacexdata.com/v4/landpads/" + shipID)
    try:
      response = requests.get(url)
      response.raise_for_status()
      jsonResponse = response.json()
      shipName = str(jsonResponse["full_name"])
      self.__droneShip = str(shipName)
      return
    except HTTPError as http_err:
      print(f"HTTP error occured: {http_err}")
      return
    except Exception as err:
      print(f"Other error occured: {err}")
      return

  def updateLivestreamLink(self, jsonResponse):
    """
    Queries API for droneship info and then updates the class instance 
    """
    livestreamLink = str(jsonResponse["links"]["webcast"])
    self.__webcastLink = livestreamLink

  def updateMissionDescription(self, jsonResponse):
    """
    docstring
    """
    missionDescription = jsonResponse["details"]
    self.__missionDescription = missionDescription
    


def requestNextLaunch():
  """
  API caller for the JSON on the next launch so that it can be used elsewhere
  """
  try:
    response = requests.get("http://api.spacexdata.com/v4/launches/next")
    response.raise_for_status()
    jsonResponse = response.json()
    return jsonResponse
  except HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
  except Exception as err:
    print(f"Other error occured: {err}")
    
def requestArbitraryLaunch(id):
  """
  API caller to request JSON for a launch specified by the user
  """
  launchID = str(id)
  url = str("http://api.spacexdata.com/v4/launches/"+ launchID)
  try:
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
    return jsonResponse
  except HTTPError as http_err:
    print(f"HTTP error occured: {http_err}")
  except Exception as err:
    print(f"Other error occured: {err}")

def requestLatestLaunch():
    """
    API caller to get JSON for the last launch 
    """
    try:
      response = requests.get("http://api.spacexdata.com/v4/launches/latest")
      response.raise_for_status()
      jsonResponse = response.json()
      return jsonResponse
    except HTTPError as http_err:
      print(f"HTTP error occured: {http_err}")
    except Exception as err:
      print(f"Other error occured: {err}")

def createLaunchObject(jsonResponse):
  """
  Method to create an instance of the Launches class, and then call updateValues() to populate the instance
  """
  name = jsonResponse["name"]
  payloadID = jsonResponse["payloads"]
  payloadIDString = payloadID[0]
  coreID = jsonResponse["cores"][0]["core"]
  launch = Launches(rocketSerial=0, missionName=name, droneShip="", payload="")
  launch.updateValues(payloadIDString, rocketSerial=coreID, jsonResponse=jsonResponse)
  return launch

  

  # if requestedLaunch.status_code == 200:
  #   return requestedLaunch
  # else:
  #   return


def main():
  """
  It's a tester. If it wasn't present, Dr. Lewis would feel a random chill down his spine every time I ran my program.
  """
  jsonResponse = requestNextLaunch()
  launch = createLaunchObject(jsonResponse)
  if type(launch) == None:
    print("You've fked it")
  else:
    launch.__str__()




if __name__ == "__main__":
    main()
from scripts import requestsDriver

def displayMenu():
  """
  Display a menu with the latest five launches as determined by API calls
  """
  userInput = "2"
  while userInput != "5":
    print("".center(80,"="))
    print("Select a Launch...".center(80, " "))
    print("".center(80,"="))
    print()
    print("1) Next launch") # Add a function call to get the name and display it in the parentheses
    print("2) Latest launch")
    print("3) Request a Specific Launch")
    print("4) Notable Launches")
    print("5) Exit")
    print()
    userInput = input("Please select an option: ")

    if userInput == "1":
      print("Accessing info for the next SpaceX launch....")
      jsonResponse = requestsDriver.requestNextLaunch()
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")
    elif userInput == "2":
      print("Accessing info for the latest SpaceX launch....")
      jsonResponse = requestsDriver.requestLatestLaunch()
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")
    elif userInput == "3":
      id = input("Please provide a launch ID as specified by the API: ")
      print("Accessing info for specified SpaceX launch....")
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press Enter to continue...")
    elif userInput == "4":
      notableLaunchesMenu()
      input("Press Enter to continue...")
    elif userInput == "5":
      break
    else:
      print("\033[1;31m" + "Please input a valid menu option." + "\033[0m")

def notableLaunchesMenu():
  """
  docstring
  """
  userInput = "2"
  while userInput != "4":
    print("".center(80, "="))
    print("Notable Launches".center(80, " "))
    print("".center(80, "="))
    print()
    print("1) Crew-1")
    print("2) Demo-2")
    print("3) NROL-108")
    print("4) Return to Main Menu")
    print()
    userInput = input("Please select an option: ")

    if userInput == "1":
      id = "5eb87d4dffd86e000604b38e"
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")

    elif userInput == "2":
      id = "5eb87d46ffd86e000604b388"
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")

    elif userInput == "3":
      id = "5f8399fb818d8b59f5740d43"
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")
    elif userInput == "4":
      break
    else:
      print("\033[1;31m" + "Please input a valid menu option." + "\033[0m")


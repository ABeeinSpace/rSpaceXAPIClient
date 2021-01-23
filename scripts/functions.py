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
    elif userInput == "5":
      break
    elif userInput == "6":
      superSecretEasterEgg()
    else:
      print("\033[1;31m" + "Please input a valid menu option." + "\033[0m")

def superSecretEasterEgg():
  """
  An easter egg. SSSSSSHHHHH its a SEEEEEECRET
  """
  print("".center(80,"="))
  print("Credits".center(80))
  print("".center(80,"="))
  print()
  print(f"I have to credit a number of people with making this little piece of software possible.\nDr. Jason Lewis, professor at Florida Southern College. I've learned to like writing Python code, even if I thought your class would turn me against Python for good. \nThe users of the SpaceX subreddit. I would not have an API to query if not for their hard work. \nAs always with a programming project, Stack Exchange proved really helpful for figuring out the requests module.\nAnd finally, Python documentation writers. You people are awesome.")
  input("Press enter to continue...")


def notableLaunchesMenu():
  """
  Menu to display a few interesting launches as determined by yours truly. 
  """
  userInput = "2"
  while userInput != "6":
    print("".center(80, "="))
    print("Notable Launches".center(80, " "))
    print("".center(80, "="))
    print()
    # I saw Crew-1 with my girlfriend, and it was the first operational launch of SpaceX's Crew Dragon capsule
    print("1) Crew-1")
    # Demo-2 was the first Crew Dragon mission on which there were people. 
    print("2) Demo-2")
    # LZ-1 landing
    print("3) NROL-108")
    print("4) Arabsat 6A")
    print("5) Falcon Heavy Test Flight")
    print("6) Return to Main Menu")
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
      id = "5eb87d2dffd86e000604b376"
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")
    elif userInput == "5":
      id = "5eb87d13ffd86e000604b360"
      jsonResponse = requestsDriver.requestArbitraryLaunch(id)
      launch = requestsDriver.createLaunchObject(jsonResponse)
      print(launch)
      input("Press enter to continue... ")
    elif userInput == "6":
      break
    else:
      print("\033[1;31m" + "Please input a valid menu option." + "\033[0m")


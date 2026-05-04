from solution import Statistics

s = Statistics("test_data.txt")

print("Players:", s.get("/players"))
print("Games:", s.get("/games"))
print("Total games:", s.get("/total"))

print("Points games:", s.get("/total/points"))
print("Places games:", s.get("/total/places"))
print("Winner games:", s.get("/total/winner"))

print("Joosep games played:", s.get("/player/joosep/amount"))
print("Joosep wins:", s.get("/player/joosep/won"))
print("Joosep favourite game:", s.get("/player/joosep/favourite"))

print("Chess games played:", s.get("/game/chess/amount"))
print("Chess most wins:", s.get("/game/chess/most-wins"))
print("Chess record holder:", s.get("/game/chess/record-holder"))
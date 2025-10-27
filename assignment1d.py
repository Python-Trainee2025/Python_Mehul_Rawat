contacts = {
    "Mehul": "9800498541",
    "Samir": "9804344382",
    "Hari":  "9254745890",
    "Om":    "9847897645"
}


name = input("Enter the name to search: ")


if name in contacts:
    print("Phone number of", name, "is:", contacts[name])
else:
    print("Sorry, contact not found.")

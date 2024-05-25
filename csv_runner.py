import csv

name = input("What is your name? ")
house = input("What is your house? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","house"])
    writer.writerow({"name":name,"house":house})
# Basic-Physics-Calculator
# Built by Asaiah Yabut
# This project was made to practice basic coding and to revise physics


def final_velocity():
    print("\n-- Final Velocity --")
    print("Formual: v = u + at")
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s2): "))
    t = float(input("Enter time (s): "))
    v = u + a * t
    print("Final Velocity =" , V, "m/s")

def displacement():
    print("\n-- Displacement --")
    print("Formula: s = ut + 0.5 x a x t squared")
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s2): "))
    t = float(input("Enter time (s): "))

def force():
    print("\n-- Force --")
    print("Formula: F = ma")
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    KE = 0.5 * m * v ** 2
    print("Kinetic Energy =", KE, "Joules")

def potential_energy():
    print("\n-- Gravitational Potential Energy --")
    print("Formula: GPE = mgh")
    m = float(input("Enter mass (kg): "))
    g = float(input("Enter gravitational potential acceleration (m/s2), usually 9.81: "))
    h = float(input("Enter height (m): "))
    GPE = m * g * h
    print("Potential Energy =", GPE, "Joules")

# Main Menu
# I learned how to use loops to keep the program running

print("Welcome to my Physics Calculator")
print("I built this to learn the fundamentals of coding and to aid in my revision of physics"

while True:
    print("\nWhat do you want to calculate?")
    print("1. Final Velocity")
    print("2. Displacement")
    print("3. Force")
    print("4. Kinetic Energy")
    print("5. Gravitational Potential Energy")
    print("6. Quit")

    choice = input("\nEnter a number: ")

    if choice = "1":
        final_velocity()
    elif choice = "2":
        displacement()
    elif choice = "3":
        force()
    elif choice = "4":
        kinetic_energy()
    elif choice = "5":
        potential_energy()
    elif choice = "6":
        print("Goodbye")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 6")




def user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_unit = input("Enter the unit of height (meters/m or feet/ft): ").lower()
        
        if height_unit == "meters" or height_unit == "m":
            height = float(input("Enter your height in meters: "))
        elif height_unit == "feet" or height_unit == "ft":
            feet = float(input("Enter your height in feet: "))
            inches = float(input("Enter the remaining inches: "))
            # Convert feet and inches to meters
            height = (feet * 0.3048) + (inches * 0.0254)
        else:
            print("Invalid height unit. Please enter either 'meters' or 'feet'.")
            return 0, 0

        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return 0,0

def calculate_bmi(weight, height):
    if weight == 0 or height ==0 :
        return 0

    # BMI formula
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi == 0:
        return "Invalid input is given ."

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")

    weight, height = user_input()

    while weight ==0 or height ==0 or weight <= 0 or height <= 0:
        print("Please enter positive numbers for weight and height .")
        weight, height = user_input()

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print('\n----------------------------------')
    print(f"\tYour BMI Result ")
    print('----------------------------------')

    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()

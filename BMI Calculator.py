#------------------------------------------Question-------------------------------------------
# Write a single Python function that calculates a BMI score and also classifies that score by assigning a text string from the table below.  Your bmi() function should take in height and weight as float parameters.  
# Your function should return four items: height (float), weight (float), BMI score (rounded float to one decimal place), and BMI classification (string).

# Please use the classification system below, which is commonly used for adults in the United States:

# Classification

# BMI Range

# Underweight - less than 18.5 

# Healthy - 18.5 to just under 25.0

# Overweight - 25.0 to just under 30.0

# Obese - 30.0 and above

 

# Requirements

# Your code should:

# Ask the user to input a height (meters or inches), convert it into a float.
# Ask the user to input a weight (kilograms or pounds), convert it into a float.
# Pass these values into your Python function. Your function should do the following: 
# Make sure to check your input for suspicious/bad input values
# Calculate a BMI value for the data provided
# Round your calculated BMI to one decimal place (e.g., 28.7 instead of 28.6987838578923)
# Now Classify the rounded BMI values using the table returning a string corresponding to the ranges listed above. 
# You should return all four items (height, weight, BMI, classification) as a Python list.
# Print the returned BMI information with an appropriate message.
# Hints

# Error Checking:

# Your bmi() function will produce correct answers when reasonable parameters are provided, however unreasonable values need to be managed by the developer.
# What if a user enters a height of 84 inches into a bmi() function expecting meters?  That would be very tall for a human.  
# Add a control structure to the top of your bmi() function to check for nonsense values being passed into your bmi() function.
# Check for values that are zero, negative, or are super big (taller than 3 meters or 10 feet or weight greater than 1000 pounds.)
# Check both height and weight parameters.  When you detect goofy values, return None.  Don't print anything inside of your bmi() function.  
# Let the main code decide what to do.

# Logic:

# Make sure to incorporate the following logic into your application:

# while (input("You you like to calculate BMI? Please Select Y for Yes or N for No ")) == "Y"):
#     metricFlag = input("You you like to use Metric system? Please Select Y for Yes or N for No ")
#     if metricFlag == "Y":
#         height = get height from the user
#         weight = get weight from the user
#         bmi = calculateBMI(height, weight, metricFlag)
#     elif metricFlag == "N":
#         height = get height from the user
#         weight = get weight from the user
#         bmi = calculateBMI(height, weight, metricFlag)

# Print the bmi

 

# Also, pay attention to the logic within each if/elif condition.  Within a single conditional, check for boundary conditions to make sure you are either including 
# an endpoint: “x <= cutoff” or excluding an endpoint: “x < cutoff”.  When looking across all of the conditionals together, check if there are any single expressions 
# that have already been checked.  If you find any, remove the redundant ones.

# Return Values:

# Python functions can only return nothing (None) or one (1) thing.  So how can you return more than one thing?  By using a container!  
# Create a function that returns a Python-style list with these things in it.  Remember, lists are indexed from 0, 1, 2, 3 ..., so when adding items to a list 
# the order is important: 

# The height entered as a float
# The weight entered as a float
# The calculated BMI (rounded to one decimal place) as a float
# The classification as a string
# What do I turn In?

# Submit a copy of your source code, which should be a simple text file ending with 
# “project1_<your name>.py”, like "project_Ali_Naqvi.py".  

# You are welcome to open a thread in the General Discussion forum to discuss this and other assignments, if you have questions you don’t mind making public. 
# You are also welcome to email me with any questions or problems that you may have.

#------------------------------------------Answer-------------------------------------------

#Define variables
height = 0.0
weight = 0.0
bmi = 0.0

#Validating height input from user.
def error_checking_height(height, metricFlag):
    try:
        float_height = float(height)
        if metricFlag == "y":
            # validate against metricy
            if float_height > 3.0:
                print("Height must be under 3 meters.")
            
        elif metricFlag == "n":
            # validate against imperial
            if float_height > 120.0:
                print("Height must be under 120 inches.")
        else:
            print("Please enter Y or N.")
        return True

    except:
        print("Please enter height in correct format.")
        return False
    
#Validating weight input from user.    
def error_checking_weight(weight, metricFlag):
    try:
        float_weight = float(weight)
        if metricFlag == "y":
            # validate against metric
            if float_weight > 454.0:
                print("Weight must be under 454 kilograms.")
            
        elif metricFlag == "n":
            # validate against imperial
            if float_weight > 1000.0:
                print("Weight must be under 1000 pounds.")
        else:
            print("Please enter Y or N.")
        return True

    except:
        print("Please enter weight in correct format.")
        return False

#Calculateing bmi.  
def calculateBMI(height, weight, metricFlag):
    _height = height
    _weight = weight
    _metricFlag = metricFlag
    if error_checking_height(_height, _metricFlag) == True and error_checking_weight(_weight, _metricFlag) == True:
        if _metricFlag == "y":    # metric formula
            bmi = float(_weight)/(float(_height)*float(_height))
        else:
            bmi = (float(_weight)*703)/(float(_height)*float(_height))    # imperial formula
        bmi = round(bmi, 1)
    
        #Printing bmi and classification.
        if bmi < 18.5:
            print("3. Your bmi is " + str(bmi)+".")
            print("4. You are underweight.")
        elif (bmi > 18.5) and (bmi < 25.0):
            print("3. Your bmi is " + str(bmi)+".")
            print("4. You are healthy.")
        elif (bmi > 25.0) and (bmi < 30.0):
            print("3. Your bmi is " + str(bmi)+".")
            print("4. You are overweight")
        elif bmi > 30.0:
            print("3. Your bmi is " + str(bmi)+".")
            print("4. You are obese.")



#Asking details from user.
def ask_details_from_user():
    if input("Would you like to calculate BMI? Please Select Y for Yes or N for No: ").lower() == "y":
        metricFlag = input("Would you like to use Metric system? Please Select Y for Yes or N for No: ").lower()
        if metricFlag == "y":
            height = input("1. Enter your height in meter. ")
            weight = input("2. Enter your weight in kilogram. ")
            bmi = calculateBMI(height, weight, metricFlag)
        elif metricFlag == "n":
            height = input("1. Enter your height in inches. ")
            weight = input("2. Enter your weight in pounds. ")
            bmi = calculateBMI(height, weight, metricFlag)
    else:
        print("Thank You.")
    
def main():
    ask_details_from_user()

main()


"""
Question 10:
Create a program that asks the user for a string
and checks if it contains the substring "Python".
If it does, print "Contains Python"; otherwise, print "Does not contain Python."
"""


def check_string(str1):
    # if "python" in str1:
    #     return "Contains Python"
    # else:
    #     return "Dose not contain python"

    for i in range(len(str1) - len("python")+1):
        if str1[i:i+len("python")] == "python":
            return "Contain python"
    return "Dose not contain python"


string1 = input("Enter your string : ").lower()
print(check_string(string1))

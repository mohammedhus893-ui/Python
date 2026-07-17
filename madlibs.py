# ==========================================
# Script Name: Security Incident Report
# Description: A simple script to generate 
# a security report based on user input.
# ==========================================

# Gathering input data from the user
system_name = input("Enter the system name: ")
threat_level = input("Enter the threat level: ")
vulnerability_type = input("Enter the vulnerability type: ")
action_taken = input("Enter the action taken: ")

# Printing the formatted report
print("\n" + "="*30)
print("   SECURITY INCIDENT REPORT")
print("="*30)
print(f"System Name        : {system_name}")
print(f"Severity Level     : {threat_level}")
print(f"Vulnerability Type : {vulnerability_type}")
print(f"Resolution Action  : {action_taken}")
print("="*30)
print("   End of Report\n")
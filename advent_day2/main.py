
max_change = 3

# Get list of reports
with open("input.txt") as file:
    report_list = file.readlines()

# Delete the spaces between numbers
for index in range(0,len(report_list)):
    report_list[index] = report_list[index].split()

# Transform the strings to integers
report_list_int = []
for report in report_list:
    report_list_int.append([int(level) for level in report])

# Function to determine if a report is Safe/Unsafe
def verify_report(report):
    # Calculate the difference between the levels
    diff = []
    for index in range(0,len(report) - 1):
        diff.append(report[index + 1] - report[index])

    # Logic to determine if Safe or Unsafe
    if all(item < 0 for item in diff) or all(item > 0 for item in diff):
        if all(abs(item) <= max_change for item in diff):
            status = 'Safe'
        else:
            status = 'Unsafe'
    else:
        status = 'Unsafe'

    return status

def dampener(report):
    original_report = report
    for index in range(0,len(original_report)):
        temp_report = [x for i,x in enumerate(original_report) if i!=index]
        status = verify_report(temp_report)
        if status == 'Safe':
            return status
        else:
            continue

    return 'Unsafe'


report_evaluation = []
for report in report_list_int:
    report_evaluation.append(verify_report(report))

print(f"The number of safe reports is {report_evaluation.count('Safe')}")


report_evaluation_damped = []
for report in report_list_int:
    status = verify_report(report)
    if status == 'Safe':
        report_evaluation_damped.append(verify_report(report))
    else:
        report_evaluation_damped.append(dampener(report))

print(f"The number of safe reports after the Dampener is {report_evaluation_damped.count('Safe')}")
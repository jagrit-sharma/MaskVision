import os

def clearAttendanceFiles():
    # Clear Attendance.csv
    attendance_file = 'Attendance.csv'
    if os.path.exists(attendance_file):
        with open(attendance_file, 'w') as f:
            f.write('Name,Entry Time,Exit Time\n')
        print(f'[INFO] Cleared {attendance_file}')

    # Clear Output.csv
    output_file = 'output.csv'
    if os.path.exists(output_file):
        with open(output_file, 'w') as f:
            f.write('Student Name,Status\n')
        print(f'[INFO] Cleared {output_file}')

# Run the function to clear files
clearAttendanceFiles()
# ========================
# STUDENT ATTENDANCE MANAGEMENT SYSTEM
# ========================

class AttendanceSystem:
    def __init__(self):
        self.students = {}
        self.attendance_records = []
        
    # ===== 1. STUDENT REGISTRATION =====
    def register_student(self):
        print("\n" + "="*40)
        print("      STUDENT REGISTRATION")
        print("="*40)
        
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        
        # Age validation
        if age < 16:
            print("❌ Registration Failed: Too young for college admission")
            return
        elif age > 60:
            print("❌ Registration Failed: Age exceeds maximum limit")
            return
        
        # Course validation
        available_courses = ["bca", "bcom", "Business", "Medicine"]
        if course not in available_courses:
            print("❌ Registration Failed: Course not available")
            return
        
        # Register student
        self.students[student_id] = {
            'name': name,
            'age': age,
            'course': course,
            'registration_date': '2024-01-01'
        }
        print(f"✅ Registration Successful! {name} registered in {course}")
    
    # ===== 2. DAILY ATTENDANCE MARKING =====
    def mark_attendance(self):
        print("\n" + "="*40)
        print("      DAILY ATTENDANCE MARKING")
        print("="*40)
        
        student_id = input("Enter Student ID: ")
        
        # Check if student exists
        if student_id not in self.students:
            print("❌ Student not found! Please register first.")
            return
        
        date = input("Enter date (YYYY-MM-DD): ")
        time_in = input("Enter check-in time (HH:MM): ")
        time_out = input("Enter check-out time (HH:MM): ")
        
        # Convert time to calculate hours
        in_hour, in_min = map(int, time_in.split(':'))
        out_hour, out_min = map(int, time_out.split(':'))
        
        total_hours = out_hour - in_hour
        total_minutes = out_min - in_min
        
        # Calculate total time spent
        if total_minutes < 0:
            total_hours -= 1
            total_minutes += 60
        
        # Determine attendance status
        status = ""
        if total_hours >= 8:
            status = "Present Full Day"
        elif total_hours >= 4:
            status = "Present Half Day"
        elif total_hours > 0:
            status = "Late (Short Day)"
        else:
            status = "Absent"
        
        # Late arrival check
        late_message = ""
        if in_hour > 9 or (in_hour == 9 and in_min > 15):
            late_by = (in_hour - 9) * 60 + (in_min - 15)
            late_message = f" - Late by {late_by} minutes"
            status += late_message
        
        # Early departure check
        early_message = ""
        if out_hour < 17:
            left_early = (17 - out_hour) * 60 - out_min
            early_message = f" - Left early by {left_early} minutes"
            if "Late" not in status:
                status += early_message
            else:
                status += f" and left early by {left_early} minutes"
        
        # Save attendance record
        record = {
            'student_id': student_id,
            'name': self.students[student_id]['name'],
            'date': date,
            'time_in': time_in,
            'time_out': time_out,
            'status': status,
            'hours_attended': total_hours,
            'minutes_attended': total_minutes
        }
        
        self.attendance_records.append(record)
        print(f"✅ Attendance marked for {self.students[student_id]['name']}")
        print(f"📊 Status: {status}")
        print(f"⏰ Hours attended: {total_hours}h {total_minutes}m")
    
    # ===== 3. ATTENDANCE ANALYTICS & REPORTS =====
    def generate_report(self):
        print("\n" + "="*40)
        print("      ATTENDANCE ANALYTICS & REPORTS")
        print("="*40)
        
        if not self.attendance_records:
            print("❌ No attendance records found!")
            return
        
        student_id = input("Enter Student ID for report: ")
        
        # Filter records for this student
        student_records = [r for r in self.attendance_records if r['student_id'] == student_id]
        
        if not student_records:
            print("❌ No attendance records found for this student!")
            return
        
        # Calculate statistics
        total_days = len(student_records)
        present_days = len([r for r in student_records if "Present" in r['status']])
        absent_days = len([r for r in student_records if "Absent" in r['status']])
        half_days = len([r for r in student_records if "Half Day" in r['status']])
        late_days = len([r for r in student_records if "Late" in r['status']])
        
        attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0
        
        # Performance categorization
        if attendance_percentage >= 90:
            performance = "Excellent 🎉"
            color = "🟢"
        elif attendance_percentage >= 80:
            performance = "Good 👍"
            color = "🟡"
        elif attendance_percentage >= 75:
            performance = "Satisfactory ✅"
            color = "🟠"
        elif attendance_percentage >= 60:
            performance = "Needs Improvement ⚠️"
            color = "🔴"
        else:
            performance = "Poor ❌"
            color = "💀"
        
        # Generate alerts
        alerts = []
        if attendance_percentage < 75:
            if attendance_percentage < 60:
                alerts.append("🚨 CRITICAL: Attendance below 60% - Immediate action required!")
            else:
                alerts.append("⚠️  WARNING: Attendance below 75% - Improvement needed")
        
        if late_days >= 3:
            alerts.append("⏰ Alert: Frequent late coming detected")
        
        # Display report
        student_name = self.students[student_id]['name']
        print(f"\n📊 ATTENDANCE REPORT FOR: {student_name}")
        print(f"📅 Total Days Recorded: {total_days}")
        print(f"✅ Present Days: {present_days}")
        print(f"❌ Absent Days: {absent_days}")
        print(f"⏰ Half Days: {half_days}")
        print(f"🚨 Late Days: {late_days}")
        print(f"📈 Attendance Percentage: {attendance_percentage:.1f}%")
        print(f"🏆 Performance: {performance} {color}")
        
        # Show alerts
        if alerts:
            print("\n🔔 ALERTS:")
            for alert in alerts:
                print(f"   {alert}")
        else:
            print("\n✅ No alerts - Good attendance!")
        
        # Show recent records
        print(f"\n📋 RECENT ATTENDANCE RECORDS:")
        print("-" * 50)
        for record in student_records[-5:]:  # Last 5 records
            print(f"📅 {record['date']}: {record['status']}")
    
    # ===== MAIN MENU =====
    def main_menu(self):
        while True:
            print("\n" + "="*50)
            print("    STUDENT ATTENDANCE MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Register New Student")
            print("2. Mark Daily Attendance")
            print("3. Generate Attendance Report")
            print("4. View All Students")
            print("5. View All Attendance Records")
            print("6. Exit")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.register_student()
            elif choice == "2":
                self.mark_attendance()
            elif choice == "3":
                self.generate_report()
            elif choice == "4":
                self.view_all_students()
            elif choice == "5":
                self.view_all_records()
            elif choice == "6":
                print("Thank you for using Attendance Management System! 👋")
                break
            else:
                print("❌ Invalid choice! Please enter 1-6")
    
    def view_all_students(self):
        print("\n" + "="*40)
        print("      ALL REGISTERED STUDENTS")
        print("="*40)
        if not self.students:
            print("No students registered yet!")
            return
        for sid, info in self.students.items():
            print(f"ID: {sid} | Name: {info['name']} | Course: {info['course']} | Age: {info['age']}")
    
    def view_all_records(self):
        print("\n" + "="*40)
        print("      ALL ATTENDANCE RECORDS")
        print("="*40)
        if not self.attendance_records:
            print("No attendance records found!")
            return
        for record in self.attendance_records:
            print(f"📅 {record['date']} | {record['name']} | {record['status']}")

# ===== RUN THE SYSTEM =====
if __name__ == "__main__":
    system = AttendanceSystem()
    system.main_menu()
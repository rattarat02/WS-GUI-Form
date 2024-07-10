import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Form submitted")

def cancel_form():
    print("Form cancelled")

root = tk.Tk()
root.title("สมัครสมาชิก")

root.configure(bg="#e0f7fa")

Information = tk.LabelFrame(root, text="ข้อมูลส่วนตัว", padx=10, pady=10, bg="#F5F5DC", fg="#000000", font=("Helvetica",12, "bold"))
Information.pack(padx=10, pady=10)


label_ = tk.Label(Information, text="คำนำหน้า:", bg="#F5F5DC")
label_.grid(row=0, column=0, sticky="e")
combo_ = ttk.Combobox(Information, values=["กรุณาเลือก", "นาย", "นาง", "นางสาว"])
combo_.grid(row=0, column=1)


name = tk.Label(Information, text="ชื่อ:", bg="#F5F5DC")
name.grid(row=1, column=0, sticky="e")
name_1 = tk.Entry(Information)
name_1.grid(row=1, column=1)


surname = tk.Label(Information, text="นามสกุล:", bg="#F5F5DC")
surname.grid(row=1, column=2, sticky="e")
surname_1 = tk.Entry(Information)
surname_1.grid(row=1, column=3)


dob = tk.Label(Information, text="วันเดือนปีเกิด:", bg="#F5F5DC")
dob.grid(row=2, column=0, sticky="e")
dob_1= tk.Entry(Information)
dob_1.grid(row=2, column=1)


gender = tk.Label(Information, text="เพศ:", bg="#F5F5DC")
gender.grid(row=3, column=0, sticky="e")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(Information, text="ชาย", variable=gender_var, value="ชาย", bg="#F5F5DC")
female_radio = tk.Radiobutton(Information, text="หญิง", variable=gender_var, value="หญิง", bg="#F5F5DC")
male_radio.grid(row=3, column=1)
female_radio.grid(row=3, column=2)


email = tk.Label(Information, text="อีเมล:", bg="#F5F5DC")
email.grid(row=4, column=0, sticky="e")
email_1 = tk.Entry(Information)
email_1.grid(row=4, column=1, columnspan=3, sticky="we")


number = tk.Label(Information, text="เบอร์โทรศัพท์:", bg="#F5F5DC")
number.grid(row=5, column=0, sticky="e")
number_1 = tk.Entry(Information)
number_1.grid(row=5, column=1, columnspan=3, sticky="we")


address = tk.Label(Information, text="ที่อยู่ปัจจุบัน:", bg="#F5F5DC")
address.grid(row=6, column=0, sticky="ne")
address_text = tk.Text(Information, height=4, width=30)
address_text.grid(row=6, column=1, columnspan=3, sticky="we")


district = tk.Label(Information, text="อำเภอ:", bg="#F5F5DC")
district.grid(row=7, column=0, sticky="e")
district_1 = tk.Entry(Information)
district_1.grid(row=7, column=1)


province = tk.Label(Information, text="จังหวัด:", bg="#F5F5DC")
province.grid(row=7, column=2, sticky="e")
province_1 = tk.Entry(Information)
province_1.grid(row=7, column=3)


postcode = tk.Label(Information, text="รหัสไปรษณีย์:", bg="#F5F5DC")
postcode.grid(row=8, column=0, sticky="e")
postcode_1 = tk.Entry(Information)
postcode_1.grid(row=8, column=1)


age = tk.Label(Information, text="อายุ:", bg="#F5F5DC")
age.grid(row=9, column=0, sticky="e")
age_1 = ttk.Combobox(Information, values=["กรุณาเลือก"] + list(range(1, 101)))
age_1.grid(row=9, column=1)


hobbies = tk.Label(Information, text="งานอดิเรก:", bg="#F5F5DC")
hobbies.grid(row=10, column=0, sticky="ne")
hobbies_1 = tk.Frame(Information, bg="#F5F5DC")
hobbies_1.grid(row=10, column=1, columnspan=3, sticky="w")
hobbies_vars = {
    "อ่านหนังสือ": tk.IntVar(),
    "เล่นเกม": tk.IntVar(),
    "ดูหนัง": tk.IntVar(),
    "ฟังเพลง": tk.IntVar(),
    "ปลูกต้นไม้": tk.IntVar(),
    "ท่องเที่ยว": tk.IntVar()
}
for i, (hobby, var) in enumerate(hobbies_vars.items()):
    tk.Checkbutton(hobbies_1, text=hobby, variable=var, bg="#F5F5DC").grid(row=i//3, column=i%3, sticky="w")


user_frame = tk.LabelFrame(root, text="ข้อมูลผู้ใช้", padx=10, pady=10, bg="#F5F5DC", fg="#00695c", font=("Helvetica", 12, "bold"))
user_frame.pack(padx=10, pady=10)


username_label = tk.Label(user_frame, text="Username:", bg="#F5F5DC")
username_label.grid(row=0, column=0, sticky="e")
username_entry = tk.Entry(user_frame)
username_entry.grid(row=0, column=1)


password_label = tk.Label(user_frame, text="Password:", bg="#F5F5DC")
password_label.grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(user_frame, show="*")
password_entry.grid(row=1, column=1)


buttons_frame = tk.Frame(root, bg="#e0f7fa")
buttons_frame.pack(padx=10, pady=10)


submit_button = tk.Button(buttons_frame, text="สมัครสมาชิก", command=submit_form, bg="#00796b", fg="white")
submit_button.grid(row=0, column=0, padx=5)


cancel_button = tk.Button(buttons_frame, text="ยกเลิก", command=cancel_form, bg="#d32f2f", fg="white")
cancel_button.grid(row=0, column=1, padx=5)

root.mainloop()
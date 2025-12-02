print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
def reverse_file_contents(file_path):
    """Đọc file và in nội dung của từng dòng theo thứ tự đảo ngược."""
    try:
        with open(file_path, 'r') as input_file:
            for line in input_file:
                # Dùng slicing để đảo ngược chuỗi
                reversed_line = line.rstrip('\n')[::-1]
                print(reversed_line)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'F:/a.txt' 
reverse_file_contents(file_duong_dan)

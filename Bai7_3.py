print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
def read_entire_file(file_path):
    """Đọc và in ra toàn bộ nội dung của tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'a.txt'
read_entire_file(file_duong_dan)

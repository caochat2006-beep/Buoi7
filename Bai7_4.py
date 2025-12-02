print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
def read_first_n_lines(file_path, n):
    """Đọc và in ra n dòng đầu tiên của tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    # Dừng nếu đã hết file trước khi đạt đến n dòng
                    break
                print(line, end='') # In dòng, giữ nguyên ký tự xuống dòng
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'F:/b.txt'
so_dong = 3
read_first_n_lines(file_duong_dan, so_dong)

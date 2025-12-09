print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
def read_last_n_lines(file_path, n):
    """Đọc và in ra n dòng cuối cùng của tệp."""
    try:
        # Đọc tất cả các dòng vào một danh sách
        with open(file_path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()     
        # Lấy n dòng cuối cùng
        # Nếu n lớn hơn số dòng thực tế, nó sẽ lấy toàn bộ
        last_n_lines = all_lines[-n:]    
        # In các dòng cuối cùng ra màn hình
        for line in last_n_lines:
            print(line, end='')           
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'b.txt'
so_dong = 3
read_last_n_lines(file_duong_dan, so_dong)

print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
def count_file_stats(file_path):
    """Đọc file và tính số ký tự, số từ, và số dòng."""
    char_count = 0
    word_count = 0
    line_count = 0  
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line_count += 1
                char_count += len(line)      
                # Loại bỏ khoảng trắng thừa và ký tự xuống dòng
                words = line.strip().split()
                word_count += len(words)
        print(f"Số ký tự (bao gồm khoảng trắng và ký tự xuống dòng) là: {char_count}")
        print(f"Số từ là: {word_count}")
        print(f"Số dòng là: {line_count}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'F:/a.txt'
count_file_stats(file_duong_dan)

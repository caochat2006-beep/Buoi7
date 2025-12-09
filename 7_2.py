print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
def count_stats(filename='a.txt'):
    """Đếm số ký tự, số từ và số dòng trong tệp."""
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read() # Đọc toàn bộ nội dung
            
            # Đếm ký tự (bao gồm khoảng trắng và ký tự xuống dòng)
            char_count = len(content)
            
            # Đếm từ (dùng split() để tách theo khoảng trắng)
            word_count = len(content.split())
            
        # Mở lại tệp để đếm số dòng
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = len(file.readlines())
        
        # In kết quả
        print("---------------------------------")
        print(f"Thống kê Tệp '{filename}':")
        print(f"Số ký tự (chars): {char_count}")
        print(f"Số từ (words): {word_count}")
        print(f"Số dòng (lines): {line_count}")
        print("---------------------------------")
        
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy tệp '{filename}'.")

# count_stats()

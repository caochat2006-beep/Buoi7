
print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
def reverse_file_content(filename='a.txt'):
    """
    Đọc tệp, đảo ngược từng dòng, và in ra chuỗi đã nối (giống Bài 1: Đọc file và in đảo ngược kết quả).
    """
    
    final_reversed_string = "" # Khởi tạo chuỗi kết quả (Không đặt trong vòng lặp)
    
    try:
        # Sử dụng 'with open' để đảm bảo tệp được đóng tự động và xử lý file ở đây
        with open(filename, 'r', encoding='utf-8') as input_file:
            
            for line in input_file:
                # 1. Loại bỏ ký tự xuống dòng '\n'
                clean_line = line.strip("\n")
                
                # 2. Đảo ngược dòng (sử dụng cú pháp slicing gọn gàng hơn)
                # Ví dụ: "ABCE" [::-1] sẽ ra "ECBA"
                reversed_line = clean_line[::-1]
                
                # 3. Nối chuỗi đã đảo ngược vào chuỗi kết quả cuối cùng
                final_reversed_string += reversed_line
                
                # Nếu bạn muốn in kết quả đảo ngược của TỪNG dòng, dùng print(reversed_line) ở đây.
                
        # In kết quả cuối cùng ra màn hình sau khi đã xử lý hết tệp
        print("---------------------------------")
        print("Kết quả xử lý toàn bộ tệp (chuỗi đã đảo ngược):")
        print(final_reversed_string)
        print("---------------------------------")
        
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy tệp '{filename}'.")
        print("Vui lòng đảm bảo file a.txt nằm cùng thư mục với file Python đang chạy.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")

# Chạy chương trình
reverse_file_content()

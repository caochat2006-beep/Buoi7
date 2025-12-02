print("sv:Cao Van Chat")
print("msv:245752021610122")
print("###########################")
#################################
import shutil
def copy_file_contents(source_path, destination_path):
    """Sao chép nội dung từ tệp nguồn sang tệp đích."""
    try:
        # Sử dụng shutil.copyfile để sao chép hiệu quả
        shutil.copyfile(source_path, destination_path)
        print(f"Đã sao chép nội dung thành công từ:")
        print(f"  Nguồn: {source_path}")
        print(f"  Đích: {destination_path}")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tệp nguồn hoặc đường dẫn không hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình sao chép: {e}")
copy_file_contents('F:/a.txt', 'F:/b.txt')

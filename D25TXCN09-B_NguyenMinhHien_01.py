import json
student = []
LINE = "="*60
LINEWITHMINUS = "-"*60

def load_data_json(file_name = "data.json"):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            student = json.load(f)
            return student
    except FileNotFoundError:
        print("Không tìm thấy file dữ liệu !")
        return []
def save_data_json(student_list, file_name = "data.json"):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(
            student_list,
            f,
            ensure_ascii=False,
            indent=4
        )
def check_is_list_empty(student_list):
    if len(student_list) == 0:
        return True
    return False 

def show_student_list(student_list):
    if( check_is_list_empty(student_list)):
        print("Danh sách sinh viên trống !")
    else:
        print("-"*112)
        print(" DANH SÁCH SINH VIÊN ".center(112, "="))
        print(f"| {"MÃ SV":<10} | {"TÊN":<25} | {"TOÁN":<10} | {"LÝ":<10} | {"HÓA":<10} | {"ĐTB":<10} | {"XẾP LOẠI":<15} |")
        print("-"*112)
        for sv in student_list:
            print(
                f"| {sv['ma_sv']:<10} | "
                f"{sv['ten']:<25} | "
                f"{sv['toan']:<10.1f} | "
                f"{sv['ly']:<10.1f} | "
                f"{sv['hoa']:<10.1f} | "
                f"{sv['diem_tb']:<10.2f} | "
                f"{sv['xep_loai']:<15} |"
            )
        print("-"*112)
def check_point_is_over_ten_or_under_zero(point):
    if(point < 0 or point > 10):
        return True
    return False 
def find_student_by_id(student_list, id_wanna_find):
    return next((i for i, value in enumerate(student_list) if (value["ma_sv"] == id_wanna_find) ), -1)

def find_student_by_id_and_name(student_list, input_wanna_find):
    return next((i for i, value in enumerate(student_list) if (value["ma_sv"] == input_wanna_find or input_wanna_find.lower() in value["ten"].lower()) ), -1)

def caculate_avg_and_rank(math, physic, chemistry):
    point_result = (math + physic + chemistry) / 3
    if(point_result >= 8.0):
        rank_result = "Giỏi"
    elif(point_result  >= 7.0):
        rank_result = "Khá"
    elif(point_result  >= 5.0):
        rank_result = "Trung bình"
    else:
        rank_result = "Yếu"
    return (point_result, rank_result)
def add_student(student_list):
    while True:
        id_student_to_add = input("Vui lòng nhập mã sinh viên muốn thêm: ").strip().upper()
        if(not id_student_to_add):
            print("Id không được để trống !")
            continue 
        if(find_student_by_id(student_list, id_student_to_add) != -1):
            print("ID đã tồn tại !")
            continue 
        break 
    print("-"*112)
    print(" THÊM MỚI SINH VIÊN ".center(112, "="))
    while True:
        name_student = input("Vui lòng nhập tên của học sinh: ").strip().title()
        if(not name_student):
            print("Tên học sinh không được để trống !")
            continue 
        break 
    while True: 
        try:
            math_point = float(input("Vui lòng nhập điêm toán: "))
        except:
            print("Lỗi ! điểm toán không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(math_point)):
            print("Điểm toán phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break
    while True: 
        try:
            physic_point = float(input("Vui lòng nhập điêm Lý: "))
        except:
            print("Lỗi ! điểm Lý không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(physic_point)):
            print("Điểm Lý phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break
    while True: 
        try:
            chemistry_point = float(input("Vui lòng nhập điêm Hóa: "))
        except:
            print("Lỗi ! điểm Hóa không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(chemistry_point)):
            print("Điểm Hóa phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break 
    avg_student, rank_student = caculate_avg_and_rank(math_point, physic_point, chemistry_point)
    student_list.append({
        "ma_sv": id_student_to_add,
        "ten": name_student,
        "toan": math_point,
        "ly": physic_point,
        "hoa": chemistry_point,
        "diem_tb": avg_student,
        "xep_loai": rank_student
    })
    save_data_json(student_list)
    print(f"Đẫ thêm thành công sinh viên mã {id_student_to_add}")
    
def update_student(student_list):
    while True:
        id_student_to_update = input("Vui lòng nhập mã sinh viên muốn cập nhật: ").strip().upper()
        if(not id_student_to_update):
            print("Id không được để trống !")
            continue 
        if(find_student_by_id(student_list, id_student_to_update) == -1):
            print("ID không tồn tại !")
            continue 
        break 
    find_index = find_student_by_id(student_list, id_student_to_update)
    print("-"*112)
    print("Đã tìm thấy sinh viên cũ: ", student_list[find_index])
    print(" CẬP NHẬT SINH VIÊN SINH VIÊN ".center(112, "="))
    while True: 
        try:
            new_math_point = float(input("Vui lòng nhập điêm toán: "))
        except:
            print("Lỗi ! điểm toán không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(new_math_point)):
            print("Điểm toán phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break
    while True: 
        try:
            new_physic_point = float(input("Vui lòng nhập điêm Lý: "))
        except:
            print("Lỗi ! điểm Lý không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(new_physic_point)):
            print("Điểm Lý phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break
    while True: 
        try:
            new_chemistry_point = float(input("Vui lòng nhập điêm Hóa: "))
        except:
            print("Lỗi ! điểm Hóa không phù hợp với dữ liệu !")
            continue 
        if(check_point_is_over_ten_or_under_zero(new_chemistry_point)):
            print("Điểm Hóa phải nằm trong khoảng [0.0 - 10.0] !")
            continue 
        break 
    avg_student, rank_student = caculate_avg_and_rank(new_math_point, new_physic_point, new_chemistry_point)
    student_list[find_index].update({
        "toan": new_math_point,
        "ly": new_physic_point,
        "hoa": new_chemistry_point,
        "diem_tb": avg_student,
        "xep_loai": rank_student
    })
    save_data_json(student_list)
    print(f"Đã cập nhật điểm thành công cho học sinh {id_student_to_update}")
def delete_student(student_list):
    while True:
        id_student_to_delete = input("Vui lòng nhập mã sinh viên muốn XÓA: ").strip().upper()
        if(not id_student_to_delete):
            print("Id không được để trống !")
            continue 
        if(find_student_by_id(student_list, id_student_to_delete) == -1):
            print("ID không tồn tại !")
            continue 
        break 
    find_index = find_student_by_id(student_list, id_student_to_delete)
    while True:
        yes_or_no = input(f"Bạn có chắc muốn xóa sinh viên {student_list[find_index]["ten"]}? (y/n): ").lower().strip()
        if(not yes_or_no):
            print("Không được để trống !")
            continue 
        if(yes_or_no not in ["y", "n"]):
            print("chỉ được y - yes, n - no !")
            continue 
        break 
    if(yes_or_no == "y"):
        student_list.pop(find_index)
        print("Xóa sinh viên thành công !")
        save_data_json(student_list)
    else:
        print("Đã hủy thao tác xóa !")
    return 
def show_find_studet_by_id(student_list):
    while True:
        id_student_to_find = input("Vui lòng nhập mã hoặc tên sinh viên muốn TÌM: ").strip().upper()
        if(not id_student_to_find):
            print("Id hoặc tên không được để trống !")
            continue 
        if(find_student_by_id_and_name(student_list, id_student_to_find) == -1):
            print("ID không tồn tại !")
            continue 
        break 
    find_index = find_student_by_id_and_name(student_list, id_student_to_find)
    print("-"*112)
    print(" DANH SÁCH TÌM KIẾM ".center(112, "="))
    print(f"| {"MÃ SV":<10} | {"TÊN":<25} | {"TOÁN":<10} | {"LÝ":<10} | {"HÓA":<10} | {"ĐTB":<10} | {"XẾP LOẠI":<15} |")
    print("-"*112)
    print(
        f"| {student_list[find_index]['ma_sv']:<10} | "
        f"{student_list[find_index]['ten']:<25} | "
        f"{student_list[find_index]['toan']:<10.1f} | "
        f"{student_list[find_index]['ly']:<10.1f} | "
        f"{student_list[find_index]['hoa']:<10.1f} | "
        f"{student_list[find_index]['diem_tb']:<10.2f} | "
        f"{student_list[find_index]['xep_loai']:<15} |"
    )
    print("-"*112)
def count_gioi_kha_trungbinh_yeu(student_list):
    count_gioi = 0
    count_kha = 0
    count_tb = 0
    count_yeu = 0
    for item in student_list:
        if(item["xep_loai"] == "Giỏi"):
            count_gioi += 1
        elif(item["xep_loai"] == "Khá"):
            count_kha += 1
        elif(item["xep_loai"] == "Trung Bình"):
            count_tb +=1 
        else:
            count_yeu+=1
    return (count_gioi, count_kha, count_tb, count_yeu)
def show_count_good_awsome_weak(student_list):
    gioi, kha, trungbinh, yeu = count_gioi_kha_trungbinh_yeu(student_list)
    print("-"*112)
    print(" THỐNG KÊ ĐIỂM TRUNG BÌNH ".center(112, "="))
    print("-"*112)
    print(
        f"Số học sinh loại giỏi: {gioi} \n"
        f"Số học sinh loại khá: {kha} \n"
        f"Số học sinh loại Trung bình: {trungbinh} \n"
        f"Số học sinh loại Yếu: {yeu}"
    )
    print("-"*112)
    
def sort_student(student_list):
    if(check_is_list_empty(student_list)):
        print("Danh sách sinh viên trống !")
        return  
    print("\n==== SẮP XẾP DANH SÁCH ===")
    print("[1]. Điểm TB giảm dần")
    print("[2]. Tên tăng dần (A - Z)")
    try:
        choice =  int(input("Lựa chọn: "))
    except ValueError:
        print("Vui lòng nhập số !")
        return 
    match choice:
        case 1:
            student_list.sort(
                key=lambda sv: sv["diem_tb"],
                reverse=True
            )
            print("Đã sắp xếp theo điểm TB giảm dần!")
        case 2:
            student_list.sort(
                key=lambda sv: sv["ten"].lower()
            )
            print("Đã sắp xếp theo tên A-Z!")
        case _:
            print("Lựa chọn không hợp lệ")
            return
    show_student_list(student_list)

def show_student_higest_lowest(student_list):
    max_dtb = max(sv["diem_tb"] for sv in student_list)
    min_đtb = min(sv["diem_tb"] for sv in student_list)
    highest = [
        sv for sv in student_list
        if sv["diem_tb"] == max_dtb
    ]
    lowest = [
        sv for sv in student_list
        if sv["diem_tb"] == min_đtb
    ]
    print("\n SINH VIÊN CÓ ĐIỂM CAO NHẤT ===")
    
    for sv in highest:
        print(
            f"{sv['ma_sv']} - "
            f"{sv['ten']} - "
            f"ĐTB: {sv['diem_tb']:.2f}"
        )

    print("\n===== SINH VIÊN ĐIỂM THẤP NHẤT =====")

    for sv in lowest:
        print(
            f"{sv['ma_sv']} - "
            f"{sv['ten']} - "
            f"ĐTB: {sv['diem_tb']:.2f}"
        )
def show_rank_student(student_list):
    if( check_is_list_empty(student_list)):
        print("Danh sách sinh viên trống !")
    else:
        print("-"*112)
        print(" DANH SÁCH HỌC LỰC SINH VIÊN ".center(112, "="))
        print(f"| {"MÃ SV":<10} | {"TÊN":<25} | {"TOÁN":<10} | {"LÝ":<10} | {"HÓA":<10} | {"ĐTB":<10} | {"XẾP LOẠI":<15} |")
        print("-"*112)
        for sv in student_list:
            print(
                f"| {sv['ma_sv']:<10} | "
                f"{sv['ten']:<25} | "
                f"{sv['toan']:<10.1f} | "
                f"{sv['ly']:<10.1f} | "
                f"{sv['hoa']:<10.1f} | "
                f"{sv['diem_tb']:<10.2f} | "
                f"{sv['xep_loai']:<15} |"
            )
        print("-"*112)
def show_menu():
    return int(input(
        f"{LINEWITHMINUS} \n"
        f"{" MENU QUẢN LÝ HỌC SINH ".center(60, "=")} \n"
        f"{"[1]. Hiển thị danh sách sinh viên".ljust(60, " ")} \n"
        f"{"[2]. Thêm mới sinh viên".ljust(60, " ")} \n"
        f"{"[3]. Cập nhật thông tin sinh viên".ljust(60, " ")} \n"
        f"{"[4]. Xóa sinh viên".ljust(60, " ")} \n"
        f"{"[5]. Tìm kiếm sinh viên".ljust(60, " ")} \n"
        f"{"[6]. Sắp xếp danh sách sinh viên".ljust(60, " ")} \n"
        f"{"[7]. Thống kê điểm TB".ljust(60, " ")} \n"
        f"{"[8]. Liệt kê sinh viên có điểm TB cao nhất / Thấp nhất".ljust(60, " ")} \n"
        f"{"[9]. Phân loại học lực sinh viên".ljust(60, " ")} \n"
        f"{"[10]. Thoát chương trình".ljust(60, " ")} \n"
        f"{LINE} \n"
        f">>> Lựa chọn của bạn: "
        ))


def main():
    student = load_data_json()
    while True:
        try:
            choose =  show_menu()
            
        except:
            print("Chức năng không phù hợp với dữ liệu là số !")
            continue 
        match choose:
            case 1:
                print()
                show_student_list(student)
                print()
            case 2:
                print()
                add_student(student)
                
                print()
            case 3:
                print()
                update_student(student)
                print()
            case 4:
                print()
                delete_student(student)
                print()
            case 5:
                print()
                show_find_studet_by_id(student)
                print()
            case 6:
                print()
                sort_student(student)
                print()
            case 7:
                print()
                show_count_good_awsome_weak(student)
                print()
            case 8:
                print()
                show_student_higest_lowest(student)
                print()
            case 9:
                print()
                show_rank_student(student)
                print()
            case 10:
                print()
                print("Cảm ơn bạn vì đã sử dụng chương trình !")
                print()
                break 
            case _:
                print("Phải chọn chức năng từ [0 - 9] !")
                
if __name__ == "__main__":
    main()

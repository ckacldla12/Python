import pickle
# 202025736 신동원 파일실행 될 시 파일을 불러오고 파일 저장을 누르면 저장이되고 종료됨
def main():
   print("파일을 불러왔습니다")
   with open("./addressData.bin", "rb") as f:
       address_book = pickle.load(f)
       print(address_book)

   while True:
       user = display_menu();
       info = []
       if user == 1:
          name, number, addr = get_contact()
          info.append(number)
          info.append(addr)
          address_book[name] = info
          print(address_book)
       elif user == 2:                  # 삭제
          name = get_contact_name()
          address_book.pop(name)		# name을 키로 가지고 항목을 삭제한다.
       elif user == 3:                  # 검색
           name = get_contact_name()
           for key in sorted(address_book):
               if name == key:
                   print(key, "의 전화번호:", address_book[key][0])
                   print(key, "의 주소:", address_book[key][1])

       elif user == 4:                  # 출력
           for key in sorted(address_book):
               print(key, "의 전화번호:", address_book[key][0])
               print(key, "의 주소:", address_book[key][1])
       elif user == 5:  # 파일 저장하기
           f = open("./addressData.bin", "wb")
           pickle.dump(address_book, f)
           f.close()
           print("파일이 저장되었습니다!")
           break

# 이름과 전화번호를 입력받아서 반환한다.
def get_contact():
    name = input("나의 이름: ")
    number = input("나의 전화번호 :")
    addr = input("나의 주소 :")
    return name, number, addr		# 튜플로 반환한다.

def get_contact_name():
    name = input("나의 이름: ")
    return name

# 메뉴를 화면에 출력한다.
def display_menu() :
   print("1. 연락처 추가")
   print("2. 연락처 삭제")
   print("3. 연락처 검색")
   print("4. 연락처 출력")
   print("5. 연락처 파일 저장")
   select = int(input("메뉴 항목을 선택하시오: "))
   return select

main()
my_name = "조우식"

def print_name(name):
    print("내 이름은",name,"입니다!")
    print(f"내이름은 {name} 입니다! 이건 백틱같은거지!")
    
    
print_name(my_name)



my_name_input = input("이름을 입력해주세요 : ")

def print_input_name(name):
    print("내 이름은",name,"입니다!")
    print(f"내이름은 {name} 입니다! 이건 백틱같은거지!")
    
    
print_input_name(my_name_input)

# 나의 성씨는 문 이구요 나의 이름은 혜림 입니다.


last_name = input("성씨를 입력해주세요(예 : 김, 이, 조, 문) : ")
middle_name = input("성함이 어떻게 되시나요? (예: 우식, 욱재) : ")

def combine_name(last_name, middle_name):
    print(f"내 이름은 {last_name} {middle_name} 입니다")
    
combine_name(last_name, middle_name)
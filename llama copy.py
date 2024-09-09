import subprocess
import os
import json  # JSON 모듈을 사용하여 딕셔너리를 문자열로 변환

def create_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    while True:
        user_input = input("입력하세요 (종료하려면 'exit' 입력): ")

        if user_input.lower() == 'exit':
            break

        command = [r"C:\Users\Administrator\AppData\Local\Programs\Ollama\ollama.exe", "run", "llama3.1", user_input]

        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            response = result.stdout.strip()
            error = result.stderr.strip()

            # 응답 및 오류 메시지를 딕셔너리로 저장
            obj = {
                "user_input": user_input,
                "response": response,
            }
            
            # 딕셔너리를 JSON 문자열로 변환
            obj_str = json.dumps(obj, ensure_ascii=False, indent=4)
            
            # 파일에 내용 작성
            create_file("example.json", obj_str)
            
            # 출력 결과 및 오류 메시지 표시
            print("LLaMA의 응답: ", response)
            if error:
                print("오류 발생:", error)
                
        except FileNotFoundError:
            print("지정된 파일을 찾을 수 없습니다. 경로와 명령어를 확인해 보세요.")
        except UnicodeDecodeError as e:
            print("문자 인코딩 오류 발생:", e)

if __name__ == "__main__":
    main()

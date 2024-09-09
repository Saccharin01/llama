import subprocess

def main():
    while True:
        user_input = input("입력하세요 (종료하려면 'exit' 입력): ")

        if user_input.lower() == 'exit':
            break

        command = [r"C:\Users\Administrator\AppData\Local\Programs\Ollama\ollama.exe", "run", "llama3.1", user_input]

        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            stdout, stderr = process.communicate()
            print("LLaMA의 응답: ", stdout)
            if stderr:
                print("오류 발생:", stderr)
        except FileNotFoundError:
            print("지정된 파일을 찾을 수 없습니다. 경로와 명령어를 확인해 보세요.")
        except UnicodeDecodeError as e:
            print("문자 인코딩 오류 발생:", e)

if __name__ == "__main__":
    main()

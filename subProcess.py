import subprocess

# 명령어와 인자를 문자열로 전달
process = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 표준 출력과 표준 에러 읽기
stdout, stderr = process.communicate()

# 표준 출력과 표준 에러 출력
print("Standard Output:")
print(stdout)

print("Standard Error:")
print(stderr)

# 종료 상태 코드
print("Return Code:")
print(process.returncode)

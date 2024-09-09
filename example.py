import argparse

# ArgumentParser 객체 생성
parser = argparse.ArgumentParser(description="A simple CLI tool")

# 인자 추가
parser.add_argument('name', type=str, help='Your name')
parser.add_argument('age', type=int, help='Your age')

# 인자 파싱
args = parser.parse_args()

# 인자 사용
print(f"Hello, {args.name}! You are {args.age} years old.")

import ollama
import json


def main():
  conversationLog = []
  file_path = "test.json"
  while True:
      user_input = input("라마에게 뭐라고 물어볼래요? (종료하려면 'exit' 입력): ")
      
      if user_input.lower() == 'exit':
        with open(file_path, "w", encoding="utf-8")as file:
          json.dump(conversationLog, file, ensure_ascii=False, indent=2)
          file.write(conversationLog)
          break
      
      try:
          response = ollama.chat(model='llama3.1', messages=[
              {
                  "role": "user",
                  "content": user_input
              }
          ])
          print("LLaMA의 응답:", response['message']['content'])
          conversationLog.append({
            "user_input" : user_input,
            "response" : response["message"]['content'],
            "create_date" : response["created_at"]
          })
          print(conversationLog)
      except Exception as e:
          print("오류 발생:", e)

if __name__ == "__main__":
    main()

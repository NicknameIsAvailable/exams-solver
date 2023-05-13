import time
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

print('Подготовьте файл с билетами: \n 1. Скопируйте все билеты с вопросами в файл формата .txt \n 2. Сотрите всю '
      'нумерацию билетов и оставьте на их месте пустую строку (строки с надписями типа Экзаменационный билет №n \n 3. '
      'Все вопросы должны занимать только одну строку \n')
examsFile = input('Введите полный путь к файлу .txt ')
print('Ждите, скоро в папке, в которой был исходный файл появится файл с ответами, который будет постепенно '
      'заполняться ответами')

with open(examsFile, 'r') as file:
    file_content = file.read()
    line_count = 0
    for line in file:
        line_count += 1

with open(examsFile.replace(".txt", " ответы.txt"), 'w') as file:
    file.write('\nОтветы')

questions = file_content.split('\n')

i = 0


def answer(__question__):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": __question__ + 'расскажи максимально коротко, чтобы можно было использовать как шпаргалку'
            }
        ]
    )

    response = completion.choices[0].message.content

    with open(examsFile.replace(".txt", " ответы.txt"), 'a') as file:
        file.write("\n " + question.split(".")[0] + ". " + response)


i = 0

for question in questions:

    if question == "":
        i += 1
        with open(examsFile.replace(".txt", " ответы.txt"), 'a') as file:
            file.write("\n\nбилет №" + str(i))

    else:
        time.sleep(20)
        answer(question)

print("Все готово")

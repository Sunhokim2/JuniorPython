from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def home():
    return '<h1 style="text-align:center">Hello, World!</h1>'\
            '<p> 0에서 9사이의 숫자를 맞춰보세요! 업다운 게임입니다 </p>'\
            '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjE'\
           'xNWhiMXA1eDYzY3ZxYXZ5Z3F2Y2FjczhrOWh6enllb2ozZ20ydHBuYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/nuufz'\
           'tgCvyJZIuSkgd/giphy.gif" width=600>'

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color:purple'>너무 큰 수에요!</h1>"\
 "<img src='https://media.giphy.com/media/cJ4yFzi04lF7i/giphy.gif?cid=ecf05e47syasmit1stjaq1ewb3ixlmsglza3u40ikqg1m2fw&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=600>"
    elif guess < random_number:
        return "<h1 style='color:red'>작은 수를 하셨네요...</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=600>"
    else:
        return "<h1 style='color:blue'>최고에요! 열심히하셨군요</h1>"\
                "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmFsNnFuNzUyZGFqNXo0dzUzMXdsZng2eDhrbmR6bXAwYXo3Z29nZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif' width=600>"

@app.route("/username/<path:name>/<int:number>")
@make_underlined
def greet(name,number):
    print(name)
    name = name+ '12'
    return f"hello ss {name}! you are number {number}"


if __name__ == '__main__':
    app.run(debug=True)
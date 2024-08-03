import pgzrun
WIDTH=870
HEIGHT=800
score=0
timeleft=10
gameover=False
questions=[]
questioncount=0
questionindex=0

answerbox1=Rect(0,0,300,150)
answerbox1.move_ip(20,300)
answerbox2=Rect(0,0,300,150)
answerbox2.move_ip(20,460)
answerbox3=Rect(0,0,300,150)
answerbox3.move_ip(330,460)
answerbox4=Rect(0,0,300,150)
answerbox4.move_ip(330,300)
questionbox=Rect(0,0,650,150 )
questionbox.move_ip(20,100)
timerbox=Rect(0,0,150,150)
timerbox.move_ip(680,100)
skipbox=Rect(0,0,150,310)
skipbox.move_ip(660,300)
answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]


def draw():
    screen.fill('coral')
    screen.draw.filled_rect(questionbox,'black')
    for box in answerboxes:
         screen.draw.filled_rect(box,'gray')
    screen.draw.filled_rect(timerbox,'brown')
    screen.draw.filled_rect(skipbox,'pink')
    screen.draw.textbox('skip',skipbox,color='brown')
    screen.draw.textbox(question[0].strip(),questionbox,color='gray')
    index=1
    for i in answerboxes:
         screen.draw.textbox(question[index].strip(),i,color='brown')
         index=index+1
    screen.draw.textbox(str(timeleft),timerbox,color='black')



def update():
    pass


def readquestionfile():
    global questioncount, questions
    q_file=open('questions.txt','r')
    for i in q_file:
        questions.append(i)
        questioncount=questioncount+1
    q_file.close()


def correctanswer():
     global score, question, questions
     score=score+1
     if questions:
          question=readnextquestion()
     else:
          game_over()

def game_over():
    global question, gameover
    message='game over'
    question=[message,'-','-','-','-',3]
    gameover=True


def readnextquestion():
    global questionindex
    questionindex=questionindex+1
    return questions.pop(0).split(',')

def on_mouse_down(pos):
    global question
    index=1
    for box in answerboxes:
        print(box)
        if box.collidepoint(pos):
             if index is int(question[5]):
                  correctanswer()
             else:
                  game_over()
        index=index+1

readquestionfile()

question=readnextquestion()

            
             
    


for box in answerboxes:
        print(box)
















pgzrun.go()

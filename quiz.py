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
    screen.draw.filled_rect(answerbox1,'gray')
    screen.draw.filled_rect(answerbox2,'gray')
    screen.draw.filled_rect(answerbox3,'gray')
    screen.draw.filled_rect(answerbox4,'gray')
    screen.draw.filled_rect(timerbox,'brown')
    screen.draw.filled_rect(skipbox,'pink')
def update():
    pass

def readquesionfile():
    global questioncount, questions
    q_file=open('questions.txt','r')
    for i in q_file:
        questions.append(i)
        questioncount=questioncount+1
    q_file.close()

readquesionfile()



















pgzrun.go()

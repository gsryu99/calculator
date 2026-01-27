# ch 5.2.1 ctrl.py

class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):   # calculate 메소드 추가, 내용은 추후 작성
        pass

    def connectSignals(self):
#        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn1.clicked.connect(self.calculate)     # 버튼1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage)

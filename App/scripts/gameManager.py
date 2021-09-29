
class GameManager():
    """
    This class controls the whole game and create the questions
    """

    def __init__(self):
        self.gameStep = 0

    def getStep(self):
        """
        Returns current game step
        """
        return self.gameStep

    def advanceStep(self):
        """
        Advance one game step
        """
        self.gameStep += 1

class QuestionsBuild():
    """
    This class build the questions
    """

    questions = []

    def __init__(self):
        self.questions.append(Question(1,"Pergunta numero 1","(a) primeira alternativa","(b) segunda alternativa"))
        self.questions.append(Question(2,"Pergunta numero 2","(a) primeira alternativa","(b) segunda alternativa"))
        self.questions.append(Question(3,"Pergunta numero 3","(a) primeira alternativa","(b) segunda alternativa"))

    def getQuestionText(self,id):
        for question in self.questions:
            if question.getId() == id:
                return question.getText()
        return

    def getQuestionAnswers(self,id):
        for question in self.questions:
            if question.getId() == id:
                return question.getAnswerText()
        return

class Question():
    """
    Questions Root class
    """

    answerIdSelected = 0

    def __init__(self, objectId, text, answer1, answer2):
        self.objectId = objectId
        self.text = text
        self.answer1 = answer1
        self.answer2 = answer2

    def getId(self):
        return self.objectId

    def setAnswer(self,answer):
        self.answerIdSelected = answer

    def getAnswerText(self):
        return self.answer1 + "\n" + self.answer2

    def getAnswerSelected(self):
        return self.answerIdSelected

    def getText(self):
        return self.text
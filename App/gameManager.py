from datetime import date

class GameManager():
    """
    This class controls the whole game and create the questions
    """

    def __init__(self):
        self.gameStep = 1

    def getStep(self):
        """
        Returns current game step
        """
        return self.gameStep

    def advanceStep(self, step):
        """
        Advance game step
        """
        self.gameStep = step

    def saveAnswer(self, questionId, answer):
        """
        Saves user answers
        """
        try:
            self.file = open("log.txt","a")
            data_atual = date.today()
            today_date = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
            self.file.write("[ Pergunta " + str(questionId) + " ] -> Resposta -> " + str(answer) + " [ " +  today_date + " ]\n")
        finally:
            self.file.close()
        

class QuestionsBuild():
    """
    This class build the questions
    """

    questions = []

    def __init__(self):

        self.questions.append(Question(1,
                                       "Ja se passaram horas, o sol ainda bate forte no ceu. Sem agua, sem sombra, o calor esta\ncomecando a afetar sua cabeca. Ao longe, voce ve a silhueta de uma cidade.\n",
                                       "|1| -> Correr ate ela."))
        self.questions[0].addNextQuestions(2)
        self.questions.append(Question(2,
                                       "E uma pequena cidade de beira de estrada. Mas voce nao lembra de ter ouvido sobre\nela. Ha pessoas na rua, eles parecem estar comemorando algo. Voce localiza o bar.\n",
                                       "|1| -> Pedir uma agua"))
        self.questions[1].addNextQuestions(3)
        self.questions.append(Question(3,
                                       "Antes de voce conseguir alguma coisa. um velho se aproxima de voce, ele diz ser o\nxerife da cidade. Bem-vindo garoto, voce chegou bem na hora. A corrida esta prestes\na comecar. Voce tenta se explicar, mas o homem ja esta lhe entregando uma mochila\ne um mapa.\n\nOlha, tudo que voce precisa fazer e ir daqui ate o Olho d Cobra, bem aqui. - disse o velho\napontando no mapa um lago pequeno no meio do deserto. Ele ja esta te empurrando para\nfora do bar. Centenas de pessoas estao na rua, gritando e comemorando. Eles gritam para\nvoce correr.\n",
                                       "|1| -> Correr"))
        self.questions[2].addNextQuestions(4)
        self.questions.append(Question(4,
                                       "Ja distante da cidade, voce ve um homem esquisito saindo dela. Examinando a\nmochila voce encontra agua, corda e um isqueiro.\n\nTomando sombra numa pedra um tiro acerta a meros centimetros da sua cabeca,\nestilhacos da pedra cortam seu rosto. Ha um homem nao muito longe de voce com um\nrifle.\n",
                                       "|1| -> Dar a volta e tentar surpreender o atirado.", "|2| -> Fugir."))
        self.questions[3].addNextQuestions(5)
        self.questions[3].addNextQuestions(41)
        self.questions.append(Question(41,
                                       "Voce ziguezagueia na esperança de desviar dos tiros. Rochas explodem em seu\ncaminho quando as balas as atingem. Voce e atingido na perna. Voce sente \no sangueescorrendo. A dor e forte. Você consegue se arrastar para uma area coberta por\npedras e os disparos param. Você remenda a ferida com pedaço da sua camiseta.\n\nO sol se pôs. Você encontra um lugar para se abrigar.\n",
                                       "|1| -> Dormir"))
        self.questions[4].addNextQuestions(61)
        self.questions.append(Question(5,
                                       "Voce circula de volta. Obtendo cobertura das rochas. Enquanto voce se arrasta em\ndirecao ao atirador pronto para embosca-lo, ele se foi. Nao ha nada la, apenas os\nprojeteis das balas que ele atirou em voce.\n\nVoce caminha em direcao as rochas. O sol se pos, a noite nasceu. Voce encontra um\nlugar para descansar.\n",
                                       "|1| -> Dormir"))
        self.questions[5].addNextQuestions(6)
        self.questions.append(Question(6,
                                       "Cansado e exausto, voce se deita perto de uma grande pedra. Voce tenta entender\ntudo o que esta acontecendo, mas nao consegue pensar direito. Voce fecha os olhos,\nnao demora muito para adormecer.\n\nUma pequena luz te acorda. Voce abre os olhos e ha uma bomba e seu fusivel esta\nqueimando rapido.\n",
                                       "|1| -> Correr.", "|2| -> Jogar a bomba longe."))
        self.questions[6].addNextQuestions(7)
        self.questions[6].addNextQuestions(8)
        self.questions.append(Question(61,
                                       "Cansado e exausto, voce se deita perto de uma grande pedra. Voce tenta entender\ntudo o que esta acontecendo, mas nao consegue pensar direito. Voce fecha os olhos,\nnao demora muito para adormecer.\n\nUma pequena luz te acorda. Voce abre os olhos e ha uma bomba e seu fusivel esta\nqueimando rapido.\n",
                                       "|1| -> Correr.", "|2| -> Jogar a bomba longe."))
        self.questions[7].addNextQuestions(66)
        self.questions[7].addNextQuestions(81)
        self.questions.append(Question(66,
                                       "Voce se levanta em um frenesi, tenta correr para longe da bomba, mas sua perna\nmachucada o retarda. Voce foi pego na explosao.\n\nO caçador vence.\n\n|0| -> Sair",
                                       ""))
        self.questions[8].addNextQuestions(0)
        self.questions.append(Question(7,
                                       "Sem tempo a perder, voce dispara em uma corrida, na esperanca de nao ser pego\npela explosao. BOOM. A bomba explode, jogando voce para o lado, voce atinge uma\narvore. Ao olhar para tras, agora ha uma cratera onde antes ficava seu acampamento\nimprovisado. Do outro lado voce o ve, parado do outro lado da explosao,\nameacadoramente pairando sobre a fumaca.\n",
                                       "|1| -> Prosseguir para o Olho d' Cobra."))
        self.questions[9].addNextQuestions(9)
        self.questions.append(Question(8,
                                       "Voce se levanta em um piscar de olhos, pegando a bomba do chao. Voce joga o mais\nlonge que puder. BOOM. A explosao o derruba. Voce pega sua mochila. Quando voce\nolha para tras, para a cratera que agora foi criada, voce ve um homem saindo do\nburaco, voce sabe que ele e o homem que estao cacando voce. Ele encara voce. \n",
                                       "|1| -> Sair da area e continuar indo em direcao ao Olha d Cobra."))
        self.questions[10].addNextQuestions(9)
        self.questions.append(Question(81,
                                       "Voce se levanta em um piscar de olhos, pegando a bomba do chao. Voce joga o mais\nlonge que puder. BOOM. A explosao o derruba. Voce pega sua mochila. Quando voce\nolha para tras, para a cratera que agora foi criada, voce ve um homem saindo do\nburaco, voce sabe que ele e o homem que estao cacando voce. Ele encara voce.\n",
                                       "|1| -> Sair da area e continuar indo em direcao ao Olha d' Cobra. "))
        self.questions[11].addNextQuestions(91)
        self.questions.append(Question(91,
                                       "O sol apareceu novamente. Voce se apoia em uma pedra para verificar o mapa. Sua\nperna ainda esta doendo, mas esta ficando mais facil de mover. O Olho d' Cobra nao\nfica longe, um pouco mais ao norte e voce esta la. Voce nao pode esperar para chegar\nla. Para entender toda essa loucura.\n",
                                       "|1| -> Seguir ao norte."))
        self.questions[12].addNextQuestions(10)
        self.questions.append(Question(9,
                                       "O sol apareceu novamente. Voce se apoia em uma pedra para verificar o mapa. Sua\nperna ainda esta doendo, mas esta ficando mais facil de mover. O Olho d' Cobra nao\nfica longe, um pouco mais ao norte e voce esta la. Voce nao pode esperar para chegar\nla. Para entender toda essa loucura.\n",
                                       "|1| -> Seguir ao norte "))
        self.questions[13].addNextQuestions(10)
        self.questions.append(Question(10,
                                       " Voce observa os passaros voando acima de sua cabeca. Parece que quanto mais\nperto voce chega do Olho d' Cobra, mais vivo o deserto se torna. Um barulho\nrepentino afasta todos eles. Voce se vira e ve um jipe vindo a toda velocidade ate\nvoce, o cacador o encontrou mais uma vez.\n",
                                       "|1| -> Tentar despista-lo entra as pedras."))
        self.questions[14].addNextQuestions(11)
        self.questions.append(Question(11,
                                       "Voce espera que o desgracado nao seja tao bom dirigindo. Seu coracao esta batendo\nmais rapido. E a terceira vez que voce esta correndo para salvar sua vida. De repente,\nha uma sombra sobre voce. Voce olha para cima. Os passaros formaram uma nuvem\nacima de voce. Eles mergulham em direcao ao jeep. Alguns segundos perdendo o\ncontrole fazem o cacador bate. Entao BOOM, uma explosao.\n",
                                       "|1| -> Checar o veiculo.", "|2| -> Continuar se movendo."))
        self.questions[15].addNextQuestions(12)
        self.questions[15].addNextQuestions(67)
        self.questions.append(Question(67,
                                       "Voce espera que aquela explosao tenha sido o suficiente para acabar com o bastardo.\nEle esta cacando voce ha 2 dias e voce nem sabe por que. De repente o cacador pula\nde uma pedra, te jogando no chao, voce luta, mas nao consegue se orientar, ele esta\nem cima de voce e e forte, voce nao consegue se levantar, ele te acerta na cabeca\ncom uma pedra te deixando desorientado. Ele puxa uma faca e a crava em seu\ncoracao.\n\nVoce esta morto. \n\n|0| -> Sair",
                                       ""))
        self.questions[16].addNextQuestions(0)
        self.questions.append(Question(12,
                                       "Voce se aproxima do veiculo, o fogo esta queimando forte. Fora das chamas voce o\nve, cambaleando das chamas. Ele e um homem alto e magro. Seu cabelo castanho\nesta queimado, suas roupas rasgadas. Voce o olha nos olhos.\n",
                                       "|1| -> Atacar. "))
        self.questions[17].addNextQuestions(13)
        self.questions.append(Question(13,
                                       "Voce pula nele chutando e socando tudo. Ele nao faz um esforco. Voce consegue\njoga-lo em uma pedra, seguindo com uma joelhada na cabeca. Ele esta no chao, voce\ncoloca as maos em volta do pescoco.\n",
                                       "|1| -> Matar o cacador. "))
        self.questions[18].addNextQuestions(14)
        self.questions.append(Question(14,
                                       "A raiva toma conta de voce.  Voce pode ver a vida sendo exterminada de seu corpo.\nDe repente, ele sorri, e se desfaz em poeira se misturando com a areia deserto.\nConfuso, voce se levanta. Nada que acontece nessa cidade faz sentido.\n",
                                       "|1| -> Seguir em frente. "))
        self.questions[19].addNextQuestions(15)
        self.questions.append(Question(15,"O sol esta alto. Suas roupas estao encharcadas de suor. Voce esta com sede. Voce\nesta caminhando ha horas.\n\nUm passaro gorjeia a sua direita. Ate que voce finalmente o encontra. Um oasis, o\nOlho d' Cobra. Voce tenta correr em direcao a ela, mas cai. Se arrastando pela areia,\nvoce consegue sentir os graos queimando sua mao voce alcanca, voce se inclina\nsobre a agua pronto para matar sua sede, mas algo o impede. Seu reflexo na agua,\nvoce o viu antes, ele tentou te matar muitas vezes ate que voce finalmente alcancou a\nvitoria. Mas como isso e possivel?\n",
                                       "|1| -> Se jogar na agua. "))
        self.questions[20].addNextQuestions(100)
        self.questions.append(Question(100,"Neste jogo o maior vencedor e aquele que luta ate ao fim.Parabens!!! ", "|0| -> Sair"))

    def getQuestionText(self,id):
        print(type(id))
        for question in self.questions:
            if question.getId() == id:
                return question.getText()
        return

    def getQuestionAnswers(self,id):
        for question in self.questions:
            if question.getId() == id:
                return question.getAnswerText()
        return

    def getQuestion(self,id):
        for question in self.questions:
            if question.getId() == id:
                return question

    def getNextQuestion(self,id,answer):
        for question in self.questions:
            if question.getId() == id:
                if(answer == 1):
                    return question.questionPosition(0)
                else:
                    return question.questionPosition(1)
                   

class Question():
    """
    Questions Root class
    """
    answerIdSelected = 0

    def __init__(self, objectId, text, answer1, answer2 = " ", isAdeath = False, isBdeath = False):
        self.objectId = objectId
        self.text = text
        self.answer1 = answer1
        self.answer2 = answer2
        self.isAdeath = isAdeath
        self.isBdeath = isBdeath
        self.nextQuestions = []

    def addNextQuestions(self, id):
        self.nextQuestions.append(id)


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

    def getIsAdeath(self):
        return self.isAdeath

    def getIsBdeath(self):
        return self.isBdeath

    def questionPosition(self, pos):
        return self.nextQuestions[pos]
            
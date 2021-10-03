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
                                       "Já se passaram horas, o sol ainda bate forte no céu. Sem água, sem sombra, o calor está\ncomeçando a afetar sua cabeça. Ao longe, você vê a silhueta de uma cidade.\n", [2],
                                       "(a) Correr até ela."))
        self.questions.append(Question(2,
                                       "É uma pequena cidade de beira de estrada. Mas você não lembra de ter ouvido sobre\nela. Há pessoas na rua, eles parecem estar comemorando algo. Você localiza o bar.\n", [3],
                                       "(a) Pedir uma água"))
        self.questions.append(Question(3,
                                       "Antes de você conseguir alguma coisa. um velho se aproxima de você, ele diz ser o\nxerife da cidade. Bem-vindo garoto, você chegou bem na hora. A corrida está prestes\na começar. Você tenta se explicar, mas o homem já está lhe entregando uma mochila\ne um mapa.\n\nOlha, tudo que você precisa fazer é ir daqui até o Olho d' Cobra, bem aqui. - disse o velho\napontando no mapa um lago pequeno no meio do deserto. Ele já está te empurrando para\nfora do bar. Centenas de pessoas estão na rua, gritando e comemorando. Eles gritam para\nvocê correr.\n", [4],
                                       "(a) Correr"))
        self.questions.append(Question(4,
                                       "Já distante da cidade, você vê um homem esquisito saindo dela. Examinando a\nmochila você encontra água, corda e um isqueiro.\n\nTomando sombra numa pedra um tiro acerta a meros centímetros da sua cabeça,\nestilhaços da pedra cortam seu rosto. Há um homem não muito longe de você com um\nrifle.\n", [5,41],
                                       "(a) Dar a volta e tentar surpreender o atirado.", "(b) Fugir."))
        self.questions.append(Question(41,
                                       "Você ziguezagueia na esperança de desviar dos tiros. Rochas explodem em seu\ncaminho quando as balas as atingem. Você é atingido na perna. Você sente o sangueescorrendo. A dor é forte. Você consegue se arrastar para uma área coberta por\npedras e os disparos param. Você remenda a ferida com pedaço da sua camiseta.\n\nO sol se pôs. Você encontra um lugar para se abrigar.\n", [61],
                                       "a) Dormir"))
        self.questions.append(Question(5,
                                       "Você circula de volta. Obtendo cobertura das rochas. Enquanto você se arrasta em\ndireção ao atirador pronto para emboscá-lo, ele se foi. Não há nada lá, apenas os\nprojéteis das balas que ele atirou em você.\n\nVocê caminha em direção às rochas. O sol se pôs, a noite nasceu. Você encontra um\nlugar para descansar.\n", [6],
                                       "(a) Dormir"))
        self.questions.append(Question(6,
                                       "Cansado e exausto, você se deita perto de uma grande pedra. Você tenta entender\ntudo o que está acontecendo, mas não consegue pensar direito. Você fecha os olhos,\nnão demora muito para adormecer.\n\nUma pequena luz te acorda. Você abre os olhos e há uma bomba e seu fusível está\nqueimando rápido.\n", [7,8],
                                       "(a) Correr.", "(b) Jogar a bomba longe."))
        self.questions.append(Question(61,
                                       "Cansado e exausto, você se deita perto de uma grande pedra. Você tenta entender\ntudo o que está acontecendo, mas não consegue pensar direito. Você fecha os olhos,\nnão demora muito para adormecer.\n\nUma pequena luz te acorda. Você abre os olhos e há uma bomba e seu fusível está\nqueimando rápido.\n", [66,81],
                                       "(a) Correr.", "(b) Jogar a bomba longe."))
        self.questions.append(Question(66,
                                       "Você se levanta em um frenesi, tenta correr para longe da bomba, mas sua perna\nmachucada o retarda. Você foi pego na explosão.\n\nO caçador vence.\n", [0],
                                       ""))
        self.questions.append(Question(7,
                                       "Sem tempo a perder, você dispara em uma corrida, na esperança de não ser pego\npela explosão. BOOM. A bomba explode, jogando você para o lado, você atinge uma\nárvore. Ao olhar para trás, agora há uma cratera onde antes ficava seu acampamento\nimprovisado. Do outro lado você o vê, parado do outro lado da explosão,\nameaçadoramente pairando sobre a fumaça.\n", [9],
                                       "(a) Prosseguir para o Olho d' Cobra."))
        self.questions.append(Question(8,
                                       "Você se levanta em um piscar de olhos, pegando a bomba do chão. Você joga o mais\nlonge que puder. BOOM. A explosão o derruba. Você pega sua mochila. Quando você\nolha para trás, para a cratera que agora foi criada, você vê um homem saindo do\nburaco, você sabe que ele é o homem que estão caçando você. Ele encara você.\n", [9],
                                       "(a) Sair da área e continuar indo em direção ao Olha d' Cobra."))
        self.questions.append(Question(81,
                                       "Você se levanta em um piscar de olhos, pegando a bomba do chão. Você joga o mais\nlonge que puder. BOOM. A explosão o derruba. Você pega sua mochila. Quando você\nolha para trás, para a cratera que agora foi criada, você vê um homem saindo do\nburaco, você sabe que ele é o homem que estão caçando você. Ele encara você.\n", [91],
                                       "(a) Sair da área e continuar indo em direção ao Olha d' Cobra."))
        self.questions.append(Question(91,
                                       "O sol apareceu novamente. Você se apoia em uma pedra para verificar o mapa. Sua\nperna ainda está doendo, mas está ficando mais fácil de mover. O Olho d' Cobra não\nfica longe, um pouco mais ao norte e você está lá. Você não pode esperar para chegar\nlá. Para entender toda essa loucura.\n", [10],
                                       "(a) Seguir ao norte"))
        self.questions.append(Question(9,
                                       "O sol apareceu novamente. Você toma um momento para verificar o mapa. O Olho d' Cobra\nnão fica longe, um pouco mais ao norte e você está lá. Você não pode esperar\npara chegar lá. Para fugir de toda essa loucura.\n", [10],
                                       "(a) Seguir ao norte."))
        self.questions.append(Question(10,
                                       "Você observa os pássaros voando acima de sua cabeça. Parece que quanto mais\nperto você chega do Olho d' Cobra, mais vivo o deserto se torna. Um barulho\nrepentino afasta todos eles. Você se vira e vê um jipe vindo a toda velocidade até\nvocê, o caçador o encontrou mais uma vez.\n", [11],
                                       "(a) Tentar despistá-lo entra as pedras."))
        self.questions.append(Question(11,
                                       "Você espera que o desgraçado não seja tão bom dirigindo. Seu coração está batendo\nmais rápido. É a terceira vez que você está correndo para salvar sua vida. De repente,\nhá uma sombra sobre você. Você olha para cima. Os pássaros formaram uma nuvem\nacima de você. Eles mergulham em direção ao jeep. Alguns segundos perdendo o\ncontrole fazem o caçador bate. Então BOOM, uma explosão.\n", [12,67],
                                       "(a) Checar o veículo.", "(b) Continuar se movendo."))
        self.questions.append(Question(67,
                                       "Você espera que aquela explosão tenha sido o suficiente para acabar com o bastardo.\nEle está caçando você há 2 dias e você nem sabe por quê. De repente o caçador pula\nde uma pedra, te jogando no chão, você luta, mas não consegue se orientar, ele está\nem cima de você e é forte, você não consegue se levantar, ele te acerta na cabeça\ncom uma pedra te deixando desorientado. Ele puxa uma faca e a crava em seu\ncoração.\n\nVocê está morto.\n", [0],
                                       ""))
        self.questions.append(Question(12,
                                       "Você se aproxima do veículo, o fogo está queimando forte. Fora das chamas você o\nvê, cambaleando das chamas. Ele é um homem alto e magro. Seu cabelo castanho\nestá queimado, suas roupas rasgadas. Você o olha nos olhos.\n", [13],
                                       "(a) Atacar."))
        self.questions.append(Question(13,
                                       "Você pula nele chutando e socando tudo. Ele não faz um esforço. Você consegue\njogá-lo em uma pedra, seguindo com uma joelhada na cabeça. Ele está no chão, você\ncoloca as mãos em volta do pescoço.\n", [14],
                                       "(a) Matar o caçador."))
        self.questions.append(Question(14,
                                       "A raiva toma conta de você.  Você pode ver a vida sendo exterminada de seu corpo.\nDe repente, ele sorri, e se desfaz em poeira se misturando com a areia deserto.\nConfuso, você se levanta. Nada que acontece nessa cidade faz sentido.\n", [15],
                                       "(a) Seguir em frente."))
        self.questions.append(Question(15,"O sol está alto. Suas roupas estão encharcadas de suor. Você está com sede. Você\nestá caminhando há horas.\n\nUm pássaro gorjeia à sua direita. Até que você finalmente o encontra. Um oásis, o\nOlho d' Cobra. Você tenta correr em direção a ela, mas cai. Se arrastando pela areia,\nvocê consegue sentir os grãos queimando sua mão você alcança, você se inclina\nsobre a água pronto para matar sua sede, mas algo o impede. Seu reflexo na água,\nvocê o viu antes, ele tentou te matar muitas vezes até que você finalmente alcançou a\nvitória. Mas como isso é possível?\n", [-1],
                                       "(a) Se jogar na água."))

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
                    try:
                        return question.questionPosition(1)
                    except:
                        return "Opção inválida"

class Question():
    """
    Questions Root class
    """

    answerIdSelected = 0

    nextQuestions = []

    def __init__(self, objectId, text, nextIds, answer1, answer2 = " ", isAdeath = False, isBdeath = False):
        self.objectId = objectId
        self.text = text
        self.answer1 = answer1
        self.answer2 = answer2
        self.isAdeath = isAdeath
        self.isBdeath = isBdeath
        for q in nextIds:
            self.nextQuestions.append(nextIds)

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
        return self.nextQuestions.index(pos)
            
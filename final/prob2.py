class Card:
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply

class Hand:
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        if self.cards:
            reply = ""
            for card in self.cards:
                reply += str(card) + "  "
        else:
            reply = "<empty>"
        return reply
    def __getitem__(self, cad):
        return self.cards.__getitem__(cad)
    
    def clear(self):
       self.cards = []

    def add(self, card):
      self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

#플레이어 객체 생성
class Player(Hand):
    def __init__(self,name): #플레이어 생성자임
        self.name = name  #플레이어의 이름
        self.card = [] #플레이어 카드
        self.len = 2 #플레이어가 가진 카드 수
        self.arrsum = 0 #플레이어 카드 값 합계
        self.turn = True #플레이어 버스트 유무
        self.chips = 10
        self.bat = 1
    
    def clear(self):
        self.card = []

    def printcard(self): #플레이어의 카드 출력
        print(self.name,":",self.card, "(",self.arrsum,") ",end='')
        print("total $ =",self.chips,"bat($)=", self.bat)
    
    #히트 함수, 버스트 (21초과시)
    def Hit(self, YorN):
        if(YorN == "y" or YorN == "Y"):
            hands = [self.card]
            deck.deal(hands, per_hand = 1)
            self.len +=1
        elif(YorN == "n" or YorN == "N"):
            #카드 뽑지 않는 것 턴 소모
            return
    
    def resultsum(self):
        cnt = 0
        sum = []
        sum.append(list(map(str ,self.card)))
        result = 0
        #print(sum[0][0][0:1])
        for i in range(self.len):
            if(len(sum[0][i]) == 3):
                result += int(sum[0][i][0:2])
            elif(len(sum[0][i]) == 2): #k q j는 10을 더해준다.
                if(sum[0][i][0:1] == 'K' or sum[0][i][0:1] == 'Q' or sum[0][i][0:1] == 'J'):
                    result += 10
                elif(sum[0][i][0:1] == "A"):
                    result += 1
                else:
                    result += int(sum[0][i][0:1])
        self.arrsum = result

#딜러 객체 생성
class Dealer(Hand):
    def __init__(self,name):
        self.name = name
        self.card = []
        self.face = False
        self.len = 2 #딜러가 가진 카드 수
        self.arrsum = 0 #딜러 카드 값 합계
        self.turn = True #딜러 버스트 유무
    
    def clear(self):
        self.card = []

    def printcard(self): #딜러 카드 출력
        if(self.face == False):
            print(dealer.name,": XX",dealer.card[1])
        elif(self.face == True):
            print(self.name,":",self.card)
    
    #딜러 히트턴은 ai로 해야하니 15이하라면 뽑기
    #뽑기전 자신의 카드를 공개해야한다.
    def resultsum(self):
        cnt = 0
        sum = []
        sum.append(list(map(str ,self.card)))
        result = 0
        for i in range(self.len):
            if(len(sum[0][i]) == 3):
                result += int(sum[0][i][0:2])
            elif(len(sum[0][i]) == 2): #k q j는 10을 더해준다.
                if(sum[0][i][0:1] == 'K' or sum[0][i][0:1] == 'Q' or sum[0][i][0:1] == 'J'):
                    result += 10
                elif(sum[0][i][0:1] == "A"):
                    result += 1
                else:
                    result += int(sum[0][i][0:1])
        self.arrsum = result

    def Hit(self):
        self.face = True #딜러카드 오픈
        self.resultsum()
        num = self.arrsum
        print(dealer.name,":",dealer.card,"(",dealer.arrsum,")")
        if(num <= 15):
            hands = [self.card]
            deck.deal(hands, per_hand = 1)
            self.len +=1
            self.resultsum()
            print(dealer.name,":",dealer.card,"(",dealer.arrsum,")")
        else:
            return 0

class Chip(Hand):
    #매 게임당 1개 칩을 걸어야한다.
    #플레이어 승리시 딜러는 플레이어가 배팅한 칩만큼 추가로 칩을준다 (2개 배팅 (승리) -> 4개 반환)
    #플레이어가 버스트 시 배팅칩 딜러가 가져감
    # 칩은 1달러만 사용
    #칩 클랫 정의 게임 시작시 chip 인스턴트 생성 딜러 플레이어에게 배분
    #총 금액과 배팅 금액으로 나뉨 초반에!
    def __init__(self):
        type = 'dollar'
        amount = 1
    def bat(self, p, n):
        p -= n

deck = Deck()
deck.populate()
deck.shuffle() #전체적인 덱을 형성중.

print("\t\tWelcome to Blackjack!\n")
playnum = int(input("How many players? <1 - 7>: ")) #플레이어 수
p = [] #플레이어 이름 클래스 저장
for i in range(playnum):
    save = input("Enter player name: ")
    p.append(save)
    p[i] = Player(save) #플레이어 이름 저장
    p[i].card = Hand() #카드 저장소

dealer = Dealer("dealer")
dealer.card = Hand()
na = 0
while True:
#각 플레이어들에게 카드 분배
    if(na > 0):
        for i in range(playnum):
            p[i].card = Hand() #카드 저장소
            p[i].len = 2 #플레이어가 가진 카드 수
            p[i].arrsum = 0 #플레이어 카드 값 합계
            p[i].turn = True #플레이어 버스트 유무
        dealer.card = Hand()
        dealer.face = False
        dealer.len = 2 #딜러가 가진 카드 수
        dealer.arrsum = 0 #딜러 카드 값 합계
        dealer.turn = True #딜러 버스트 유무
        na = 0
    
    hands = []


    for i in range(playnum):
        hands.append(p[i].card)
    hands.append(dealer.card)
    deck.deal(hands, per_hand = 2) #hands에 있는 존재들에게 카드 부여

    chp = Chip()

    for i in range(playnum):
        print(p[i].name,"",end='')
        p[i].bat = int(input("How much will you bat($)? : "))
        chp.bat(p[i].chips ,p[i].bat)


    for i in range(playnum):
        p[i].resultsum()
        p[i].printcard()
    dealer.printcard() #해당 부분에서 딜러가 히트 전까지 첫번째 카드 비공개해야함.
    print()
    #여기 까지 카드 배정 -------------------------------------------------------

    for i in range(playnum):
        if(p[i].turn == True):#false는 버스트 난거
            print(p[i].name,", do you want a hit? <Y/N> : ",sep='',end='')
            saving = input()
            p[i].Hit(saving)
            p[i].resultsum()
            print(p[i].name,":",p[i].card,"(",p[i].arrsum,")")
            if(p[i].arrsum > 21): #Bust
                p[i].turn = False
                print(p[i].name,"busts.")
                print(p[i].name,"loses.")
            print()

    dealer.resultsum()
    dealer.Hit()
    if(dealer.arrsum > 21): #dealer bust
        dealer.turn = False
        print(dealer.name, "busts.")
        print(dealer.name, "loses.")

    temp = 0
    idxtemp = 0
    draw = [] #비긴 사람들을 저장
    for i in range(playnum):
        if(temp == p[i].arrsum):
            draw.append(i)
        elif(temp < p[i].arrsum and p[i].turn == True):
            temp = p[i].arrsum
            idxtemp = i
            draw = []
    tot = 0
    if(len(draw) > 0 and dealer.arrsum <= p[draw[0]].arrsum):
        print("Draw")#비겼으니 유지.
    elif(dealer.turn == True):
        if(temp > dealer.arrsum):
            tot = p[idxtemp].bat * 2
            p[idxtemp].chips += tot
            print(p[idxtemp].name,"Wins.")
            print(p[idxtemp].name,"Get",tot,"Chips")
            print("Now",p[idxtemp].name,"Chips :",p[idxtemp].chips)
            for i in range(playnum):
                if(i != idxtemp):
                    p[i].chips -= p[i].bat
                    print("\nNow",p[i].name,"Chips :",p[i].chips)
        elif(temp < dealer.arrsum):
            print(dealer.name,"Wins.")
            for i in range(playnum):
                p[i].chips -= p[i].bat
                print("Take away Chips",p[i].name)
                print("Now Chips : ",p[i].chips)
    else:
        print(p[idxtemp].name,"Wins.")
        tot = p[idxtemp].bat * 2
        p[idxtemp].chips += tot
        print(p[idxtemp].name,"Wins.")
        print(p[idxtemp].name,"Get",tot,"Chips")
        print("Now",p[idxtemp].name,"Chips :",p[idxtemp].chips)
        for i in range(playnum):
            if(i != idxtemp):
                p[i].chips -= p[i].bat
                print("\nNow",p[i].name,"Chips :",p[i].chips)
    
    for i in range(playnum):
        if(p[i].chips <= 0):
            print(p[i].name, "don't have a chips!")
            print(p[i].name, "Lose")
            again = 0
            break
        else:
            again = int(input("Do you play again? -> 1(again) 0(exit) : "))
            break
    na += 1
    if(again == 0) : break

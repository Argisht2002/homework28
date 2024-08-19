"""1․ Գրել BankUser class, որը․
   # - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
   # - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
   #   -- անունը և ազգանունը - տառերից բաղկացած,
   #   -- տարիքը - բնական թիվ,
   #   -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
   #   -- գումարը - դրական թիվ,
   #   -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
   # - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
   # - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
   # - կունենա մեթոդ, որը կվերադարձնի մարդու անունը, ազգանունը և տարիքը,
   # - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
   # - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
   # - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
   # - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված,
   # - կունենա մեթոդ, որի միջոցով կվերականգնվի հասանելիությունը անունը, ազգանունը և հաշվեհամարի վերջին 4 թվանշանները մուտքագրելուց հետո։"""


class BankUser:
    def __init__(self,name,surname,age,card_number,money,password):
        if BankUser.check_name(name + surname):
            self._name = name
            self._surname = surname
            self.access = True
        else:
            raise ValueError
        if BankUser.check_age(age):
            self._age = age
        else:
            raise ValueError
        if BankUser.check_card_number(card_number):
            self.__card_number = card_number
        else:
            raise ValueError
        if BankUser.check_money(money):
            self.__money = money
        else:
            raise ValueError
        if BankUser.check_password(password):
            self.__password = password
        else:
            raise ValueError

    @staticmethod
    def check_name(name):
        for i in name:
            if i.low() not in "abcdefghijklmnopqrstuvwxyz":
                return False
        return True

    @staticmethod
    def check_age(age):
        return isinstance(age,int) and 18<=age<=150

    @staticmethod
    def check_card_number(card_number):
        flag = True
        for i in str(card_number):
            if i not in "0123456789" or len(str(card_number)) != 16:
                flag = False
        if flag:
            return True
        for i in str(card_number).split(' '):
            if len(i) != 4 or len(str(card_number).split(' ')) != 4:
                return False
            for j in i:
                if j not in '0123456789':
                    return False
        return True

    @staticmethod
    def check_money(money):
        return money >= 0

    @staticmethod
    def check_password(password):
        return isinstance(password, str) and len(password) >= 8

    def info(self):
        if self.access:
            return self._name,self._surname,self._age
        print("You are Blocked!!")

    def add_monet(self, summa):
        if self.access == False:
            print("You are blocked !!!")
            return
        if summa < 0:
            return
        self.__money += summa

    def take_money(self, summa):
        if self.access == False:
            print("You are blocked !!!")
            return
        if summa<0 or self.__money < summa:
            print("Nice attempt, but not with us")
            return

        self.__money -= summa

    def code_money_info(self):
        if self.access == False:
            print("You are blocked !!!")
            return
        for i in range(3):
            p = input("input your password")
            if p == self.__password:
                return self.__card_number, self.__money
            print(f'wrong password you have {2 - i} attempt left\nplease try again')
        print("too many try,,, you are blocked")
        self.access = False

    def return_access(self):
        n = input("Please input your name: ")
        if n != self._name:
            print("Wrong name!!")
            return
        s = input("Please input your surname: ")
        if n != self._surname:
            print("Wrong surname!!")
            return
        cod = input("Please input last 4 numbers on your card: ")
        if cod != str(self.__card_number)[-4:]:
            print("Wrong numbers!!")
            return
        print("Your access is back!!")
        self.access = True















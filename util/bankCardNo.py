# coding=utf-8
import random


class BankNoUtil():

    def getStr(self, len):
        str = '0123456789'
        st = []
        for i in range(len):
            st.append(random.choice(str))
            randstr = ''.join(st)
        return randstr

    def getGsBankNO(self):  # 工商银行
        cardBin = ['620302', '620402', '620403', '620407', '620404']
        cardNo = random.choice(cardBin) + self.getStr(12)
        return cardNo


if __name__ == '__main__':
    pc = BankNoUtil()
    bankno = pc.getGsBankNO()
    print(bankno)

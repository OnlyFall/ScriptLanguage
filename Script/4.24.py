import random

optical = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card = ['크로바', '다이아몬드', '하트', '스페이스']

randomChooseOp = random.randint(0, 12)
randomChooseCard = random.randint(0, 3)

print("당신이 뽑을 카드는",card[randomChooseCard], optical[randomChooseOp], "입니다.")


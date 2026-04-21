import random

print("=== 미니 배그 ===")
hp = 100
enemy_hp = 50
gun = False

while True:
    print("\n1. 파밍하기")
    print("2. 적 공격하기")
    print("3. 회복하기")
    print("4. 상태보기")

    choice = input("선택: ")

    if choice == "1":
        item = random.choice(["총", "붕대", "아무것도 없음"])
        print("획득:", item)
        if item == "총":
            gun = True
        elif item == "붕대":
            hp += 20
            if hp > 100:
                hp = 100

    elif choice == "2":
        if gun:
            damage = random.randint(15, 30)
            enemy_hp -= damage
            print("적에게", damage, "데미지!")
        else:
            print("총이 없습니다!")

        if enemy_hp <= 0:
            print("치킨 디너! 승리했습니다!")
            break

        enemy_attack = random.randint(5, 20)
        hp -= enemy_attack
        print("적의 공격!", enemy_attack, "데미지!")

    elif choice == "3":
        hp += 15
        if hp > 100:
            hp = 100
        print("체력을 회복했습니다.")

    elif choice == "4":
        print("내 체력:", hp)
        print("적 체력:", enemy_hp)
        print("총 보유:", gun)

    if hp <= 0:
        print("사망했습니다... 게임 오버")
        break
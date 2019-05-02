
#엘리베이터 = [현재층, 타고 있는 사람 수]
a = [1,0]
b = [1,0]
c = [1,0]

#어떤 엘리베이터를 움직일 지 나타내기 위해 생성하는 변수 지정
moving_elevator = 0

#엘리베이터의 움직임을 시각적으로 표현하기 위해 생성하기 위해 시간함수를 불러옴 
import time
print("10층까지 운행하며 10명을 태울 수 있는 엘리베이터입니다.")

#종료를 입력하지 않는 이상 엘리베이터는 계속 입력을 대기함
while True:

    #현재 사용자가 있는 층을 입력 받음
    floor_from = int(input("현재 계신 층을 입력하세요, 종료하시려면 0을 입력하세요: "))
    if floor_from == 0:
        break

    #1~10층의 제한을 벗어날 경우 다시 변수를 입력하라고 요구
    while (floor_from>10) or (floor_from<1):
        print("잘못 누르셨습니다.")
        print("10층까지 운행하며 10명을 태울 수 있는 엘리베이터입니다.")
        floor_from = int(input("현재 계신 층을 입력하세요, 종료하시려면 exit을 입력하세요: "))

    #현재 엘리베이터를 이용하려는 사람들의 수를 입력받음
    people = int(input("탑승 인원을 입력하세요: "))

    #1~10명의 제한을 벗어날 경우 다시 변수를 입력하라고 요구 
    while (people<1) or (people>30):
        print("잘못 누르셨습니다.")
        people = int(input("탑승 인원을 입력하세요: "))

    #사용자들이 가려고 하는 엘리베이터의 층수를 입력 받음, 이 때 모두 같은 층을 가려고 한다는 것을 전제
    floor_to = int(input("가시려는 층을 입력하세요: "))

    #1~10층의 제한을 벗어날 경우 다시 변수를 입력하라고 요구
    while (floor_to<1) or (floor_to>10):
        print("잘못 누르셨습니다.")
        floor_to = int(input("가시려는 층을 입력하세요: "))

    #어떤 엘리베이터가 가장 가까운지를 알기 위해 절댓값함수 사용
    if (abs(a[0]-floor_from)<=abs(b[0]-floor_from)) and (abs(a[0]-floor_from)<=abs(c[0]-floor_from)):
        moving_elevator = "a"
    elif (abs(b[0]-floor_from)<=abs(a[0]-floor_from)) and (abs(b[0]-floor_from)<=abs(c[0]-floor_from)):
        moving_elevator = "b"
    else:
        moving_elevator = "c"
    time.sleep(0.5)
    print()
    print(moving_elevator,"엘리베이터가 배정되었습니다.")
    time.sleep(0.5)
    print("엘리베이터가 출발하였습니다.")
    print()
    
    #가장 가까운 엘리베이터가 a일 때
    if moving_elevator is "a":
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        for i in range(abs(a[0]-floor_from)):
            time.sleep(0.5)

            #엘리베이터가 올라갈지 내려갈지 결정
            if floor_from>a[0]:
                a[0] +=1
                print(a,b,c)
            else:
                a[0] -=1
                print(a,b,c)
        print()
        time.sleep(0.5)
        print("엘리베이터가 출발지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에 탑니다")
        time.sleep(0.5)
        print("엘리베이터가 출발합니다")
        time.sleep(0.5)
        print()
        a[1] = people
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        time.sleep(0.5)
        print(a, b, c)
        for i in range(abs(a[0]-floor_to)):
            time.sleep(0.5)

            #엘리베이터가 내려갈지 올라갈지 결정
            if floor_to>a[0]:
                a[0] +=1
                print(a,b,c)
            else:
                a[0] -=1
                print(a,b,c)   
        print()
        time.sleep(0.5)
        print("엘리베이터가 목적지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에서 내립니다.")
        print()
        a[1] = 0
        time.sleep(0.5)
        print()
        print("현재 엘리베이터 상태")
        time.sleep(0.5)
        print(a,b,c)
        print()
        
    #가장 가까운 엘리베이터가 b일때
    if moving_elevator is "b":
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        for i in range(abs(b[0]-floor_from)):
            time.sleep(0.5)
            
            #엘리베이터가 내려갈지 올라갈지 결정
            if floor_from>b[0]:
                b[0] +=1
                print(a,b,c)
            else:
                b[0] -=1
                print(a,b,c)
        print()
        time.sleep(0.5)
        print("엘리베이터가 출발지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에 탑니다")
        time.sleep(0.5)
        print("엘리베이터가 출발합니다")
        time.sleep(0.5)
        print()
        b[1] = people
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        time.sleep(0.5)
        print(a, b, c)
        for i in range(abs(b[0]-floor_to)):
            time.sleep(0.5)
            
            #엘리베이터가 내려갈지 올라갈지 결정
            if floor_to>b[0]:
                b[0] +=1
                print(a,b,c)
            else:
                b[0] -=1
                print(a,b,c)   
        print()
        time.sleep(0.5)
        print("엘리베이터가 목적지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에서 내립니다.")
        print()
        b[1] = 0
        time.sleep(0.5)
        print()
        print("현재 엘리베이터 상태")
        time.sleep(0.5)
        print(a,b,c)
        print()
        
    #가장 가까운 엘리베이터가 c일때
    if moving_elevator is "c":
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        for i in range(abs(c[0]-floor_from)):
            time.sleep(0.5)
            
            #엘리베이터가 내려갈지 올라갈지 결정
            if floor_from>c[0]:
                c[0] +=1
                print(a,b,c)
            else:
                c[0] -=1
                print(a,b,c)
        print()
        time.sleep(0.5)
        print("엘리베이터가 출발지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에 탑니다")
        time.sleep(0.5)
        print("엘리베이터가 출발합니다")
        time.sleep(0.5)
        print()
        c[1] = people
        time.sleep(0.5)
        print("   a  ","   b  ","   c  ")
        time.sleep(0.5)
        print(a, b, c)
        for i in range(abs(c[0]-floor_to)):
            time.sleep(0.5)
            
            #엘리베이터가 내려갈지 올라갈지 결정
            if floor_to>c[0]:
                c[0] +=1
                print(a,b,c)
            else:
                c[0] -=1
                print(a,b,c)   
        print()
        time.sleep(0.5)
        print("엘리베이터가 목적지에 도착했습니다")
        time.sleep(0.5)
        print("사람들이 엘리베이터에서 내립니다.")
        print()
        c[1] = 0
        time.sleep(0.5)
        print()
        print("현재 엘리베이터 상태")
        time.sleep(0.5)
        print(a,b,c)
        print()

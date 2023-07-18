import random as r
arr = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]] # 모형 항생제 배지, 0은 검은색, 1은 흰색
anti_germ = 5; natural_germ = 25 # anti_germ은 항생제 내성 세균의 수, natural_germ은 야생 세균
res = []


for _ in range(8):
    temp = [anti_germ, natural_germ]
    res.append(temp) # 현재 항생제 내성 세균의 수와 야생 세균의 수를 결과에 저장

    for _ in range(anti_germ):
        integer = r.randint(0, 36)
        double = r.randint(0, 10)
        num = float(str(str(integer) + '.' + str(double))) # 임의의 소수값 0부터 36까지 소수점 아래 첫째자리까지 표현
        if int(num) - num == 0: # 만일 랜덤한 값이 정수라면(바둑알이 칸 안에 안착했다면)
            if arr[integer // 5 - 1][integer % 5 - 1] == 0: # 그리고 만일 바둑알이 떨어진 지점이 검은색이라면
                anti_germ -= 1 # 항생제 내성 세균을 제거

    for _ in range(natural_germ):
        integer = r.randint(0, 36)
        double = r.randint(0, 10)
        num = float(str(str(integer) + '.' + str(double)))
        if int(num) - num == 0 and arr[integer // 5 - 1][integer % 5 - 1] == 1: # 만일 바둑알이 칸 안에 안착하였고 그 지점이 흰색이라면
            continue # 계속해라
        else: # 아니면 (검은색에 조금이라도 닿았다면)
            natural_germ -= 1 # 야생 세균을 제거

    anti_germ *= 2; natural_germ *= 2 # 남은 세균의 개수에 2배씩 더함

print(res) # 결과 출력하기

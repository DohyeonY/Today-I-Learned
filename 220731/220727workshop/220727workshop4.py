fake = Faker("fr_FR")  In [22]:  fake1 = Faker("ko_KR")
Faker.seed(87654321) # 클래스 메서드
# Faker 클래스 내부의 난수 생성 값을 클래스 변수로 설정
# 설정한 후 생성된 모든 인스턴스가 해당 클래스 변수를 공유
print(fake1.name())

fake2 = Faker("ko_KR")

print(fake2.name())  Out [22]:  이진호
강은주
 In [44]:  fake1 = Faker("ko_KR")
fake1.seed_instance(87654321) # seed_instance 는 인스턴스 변수를 수정하는 메서드
# 인스턴스 메서드이다.

print(fake1.name())

fake2 = Faker("ko_KR")

print(fake2.name())  Out [44]:  이진호
양경희
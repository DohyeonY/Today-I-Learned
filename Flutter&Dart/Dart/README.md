# Flutter 와 dart 공부 디렉토리

## Dart

### 변수
- 타입을 적고 변수명과 데이터를 적기 
    ```
    int i = 12;
    var name = 'la';
    i = 32141251;
    name = "dohyeon";
    ```
- 변수값을 한번만 선언하고 싶을때
    ```
    final name = "dohyeon";
    name = "dushfoa"; // 불가능
    ```

- 조심스럽게 쓰는 dynamic 어떤 데이터가 들어올지 모를때
    ```
    dynamic name;
    name = "125125";
    name = 12;
    name = true;
    ```

- 컴파일 할때 값을 알고 있는 변수 
    ```
    const api_key = "1251361616";
    // final은 런타임 const는 컴파일 하기 전에 알고있어야함
    
    ```
- null safty 
    ```
    String name = "dohyeon";
    name = null; // 불가능 원래는
    
    String? name = "dohyeon";
    name.isEmpty;
    ```
- late : 나중에 값을 선언하고 싶을때, 반드시 사용전에 데이터를 넣어야함, api로 값을 가져올때 유용  
    ```
    late final String name;
    name = "dohyeon";
    print(name);
    ```

### 자료형
- dd
    ```
    void main() {
        String name = "dohyeon";
        bool alive = true;
        int age = 12;
        double money = 69.11;

        num x = 12;
        x = 1.1;
    }
    ```
    - collection if
    ```
    void main() {
        var giveMeFive = true;
        List<int> numbers = [1,
        2,
        3,
        4,
        if (giveMeFive){
            numbers.add(5)
        },
        ];
        numbers.add(1);
    }
    ```
    - String Interpolation
    ```
    void main() {
        var name = "dohyeon"
        var age = 10;
        var greeting = "hello everyone, my name is $name, and I'm ${age + 2}"; // $ 뒤에 변수 작성하면 오케이, 계산은 {}안에 넣어주기
        print(greeting) // hello everyone, my name is dohyeon, I'm 12
    }
    ```
    - collection for
    ```
    void main() {
        var oldFriends = ["a", "b"];
        var newFriends = [
            'c',
            'd',
            'e',
            for (var friend in oldFriends) "heart $friend"
        ];
        print(newFriends); // ['c','d','e','hearta','heartb']
    }
    ```
    - maps
    ```
    void main() {
        var player = {
            "name" = "dohyeon",
            "xp" : 10.00,
            "superpower" : false,
        };
        Map<int, bool> player = {
            1:true,
            2:false,
            3:true,
        };
        Map<List<int>, bool> player = {
            [1,2,3,5] :true,
        }
    }
    ```
    - sets
    ```
    void main() {
        var numbers = {1, 2, 3, 4};
        Set<int> numbers = {1, 2, 3, 4};  // 속한 아이템들이 유니크하다
        numbers.add(1);
        numbers.add(1);
        numbers.add(1);
        numbers.add(1);
        numbers.add(1);
        print(numbers) // {1, 2, 3, 4} // 1이 여러개 추가되지 않는다
    }
    ```
    - function
    ```
    String sayHello(String name) => "hello $name nice to meet you";

    num plus(num a, num b) => a + b;

    void main() {
        print(sayHello('dohyeon'));
    }
    ```

    - name parameters
    ```
    String sayHello({String name = "anon", int age = "99", String country = "wakanda"}){
        return "Hello $name, you are $age, and you come from $country";
    }
    void main(){
        print(sayHello(
            age: 12,
            country : "korea",
            name: "dohyeon",
            ))
    }
    ```
    ```
        String sayHello({required String name, required int age, required String country}){
        return "Hello $name, you are $age, and you come from $country";
    }
    void main(){
        print(sayHello(
            age: 12,
            country:'korea',
            name:"dd"
        ))
    }
    ```
    - QQ operator
    ```
    String capitalizeName(String? name) => name?.toUpperCase() ?? 'ANON';
    }
        capitalizeName("dohyeon");
        capitalizeName(null);
    }
    ``` 
    ```
    void main() {
        String? name;
        name ??= "nico";
        name = null;
        name ??= "another";
        print(name)
    }
    ```
    - typedef
    ```
    typedef ListOfInts = List<int>;

    ListOfInts reverseListOfNumbers(ListOfInts list) {
        var reversed = list.reversed;
        return reversed.toList();
    }

    void main() {
        print(reverseListOfNumbers([1,2,3,])); // [3,2,1]
    }
    ```

    - class
    ```
    class Player {
        final String name = "dohyeon";
        int xp = 1500;

        void sayHello() {
            print("Hi my name is $name");
        }
    }
    void main() {
        var player = Player();
        player.sayHello();
    }
    ```
    - constructors
    ```
    class Player {
        final String name;
        int xp;

        Player(this.name, this.xp);

        void sayHello() {
            print("Hi my name is $name");
        }
    }
    void main() {
        var player = Player("dohyeon", 2000);
        player.sayHello();
        var player2 = Player("ddd", 100);
        Player.sayHello();
    }
    ```

    - named constructors parameters
    ```
    class Player {
        final String name;
        int xp, age;
        String team;
        
        Player({
            required this.name, 
            required this.xp, 
            required this.team,
             required this.age
             });
        Player.createBluePlayer({
            required String name,
            required int age,
        }) : this.age = age,
            this.name = name,
            this.team = 'blue',
            this.xp = 0;

        Player.createRedPlayer(String name, int age) :
            this.age = age,
            this.name = name,
            this.team = "red",
            this.age = 0;

        void sayHello() {
            print("Hi my name is $name");
        }
    }

    void main() {
        var player = Player.createBluePlayer(
            name : "dohyeon",
            xp : 2000,
            );
        player.sayHello();
        var player2 = Player.createRedPlayer(
            "ddd",
            100,
            );
        Player.sayHello();
    }
    ```



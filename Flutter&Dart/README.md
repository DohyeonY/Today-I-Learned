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

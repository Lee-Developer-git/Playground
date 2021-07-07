## Typescript 🚁

1. 타입스크립트를 사용하는 이유?  
: typescript -> javascript로 전환해서 사용  
: 그런데 왜 사용하는걸까?
```javascript
function add(num1, num2){
    console.log(num1+num2);
}

add();
add(1);
add(1,2);
// 파라미터가 두 개여야하는 함수인데 모두 에러없이 출력

function showItems(arr){
    arr.forEach((item)=>{
        console.log(item);
    });
}
showItems([1, 2, 3]); //제대로 출력
showItems(1, 2, 3); // 오류가 나면서 실행 X
```
* javascript는 동적언어이고, **런타임**에 타입 결정하고 오류를 발견한다.
* typescript는 정적언어. **컨파일 타임**에 타입 결정하고 오류를 발견한다.  
=> 따라서 타입스크립트는 실행시키지 않아도 에러를 발견하기 쉽다.   
위 코드를 타입스크립트로 작성한 코드는 다음과 같다.
```typescript
function add(num1:number, num2:number){
    console.log(num1+num2);
}

add(1, 2);
```
    
2. 기본타입

```typescript
let age:number = 30;
let isAdult:boolean = true;
let a:number[] = [1,2,3];
let a2:Array<number> = [1,2,3];

let week:string[] = ['mon', 'tue', 'wed'];
let week2:Array<string> = ['mon', 'tue', 'wed'];
// a, a2 와 week, week2 모두 같은 배열 할당
```

튜플(Tuple)
void는 아무 것도 반환하지 않을 때 사용한다.  
never는 항상 에러를 반환하거나, 영원히 끝나지 않는 타입의 함수로 사용이 가능하다. 
```typescript
let b:[string, number];

b = ['z',1];

b[0].toLowerCase();

//void, never
function sayHello():void{
    console.log('hello');
}

function showError():never{
    throw new Error();
}

function infLoop():never{
    while(true){
        //
    }
}
``` 

enum은 javascript에서는 사용하지 않는 타입이다. 비슷한 타입끼리 묶어준 것이다.

```typescript
enum Os{
    Window = 3,
    Ios = 10,
    Android
}

console.log(Os['Ios']);

let myOs:Os;
// 타입을 이렇게 설정해주면 Win, Ios, And 만 입력할 수 있음
myOs = Os.Window
// 특정값만 입력할 수 있고 그 값들이 공통점이 있을 때 enum을 사용하면 좋음

//null, undefined
let a:null = null;
let b:undefined = undefined;
```

3. 인터페이스(Interface)  
인터페이스를 사용하면 어떠한 객체가 무슨 프로퍼티나 메소드를 가졌는지 알 수 있다.
```typescript
let user:object;
user = {
    name :'xx',
    age : 30
}
console.log(user.name) // 에러가 뜬다.
// 이럴 때 사용해 주는 것이 인터페이스~~~

type Score = 'A' | 'B' | 'C' | 'F';

interface User {
    name : string;
    age : number;
    gender? : string; //입력해도 되고, 안해도 되는 속성을 표시할 때 ?를 친다.
    readonly birthYear : number; //읽기전용인 속성
    [grade:number] : Score; // enum형식으로 타입 설정
}

let user : User = {
    name : 'xx',
    age : 30
    birthYear : 2000,
    1 : 'A',
    2 : 'B'
}
user.age = 10;
user.gender = 'male';
```
인터페이스 함수를 만들어보자.
```typescript
// 1번
interface Add {
    (num1:number, num2:number): number; // 더한 숫자를 리턴해준다.
}
const add : Add = function(x, y){
    return x + y;
}

add(10, 20); //30

// 2번
interface IsAdult {
    (age:number) : boolean;
}
const a:IsAdult = (age) =>{
    return age > 19;
}

a(33); //True

//Implements
interface Car {
    color: string;
    wheels: number;
    start(): void;
}

interface Benz extends Car{ //Car 인터페이스에서 확장해준다.
    door: number;
    stop(): void;
}
```
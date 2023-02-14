const minuteEl = document.getElementById('minute');
const secondEl = document.getElementById('second');

function fillZero(num) {
return String(num).padStart(2, "0"); //문자열이 2자리수가 되도록 0을 앞에 붙이기
}

var num = 299; // 몇분을 설정할지의 대한 변수 선언
var myVar;

function time(){
    myVar = setInterval(alertFunc, 1000); 
}
time();

function alertFunc() {
    var min = num / 60; 
    min = Math.floor(min);

    var sec = num - (60 * min);

    minuteEl.innerText = fillZero(min)
    secondEl.innerText = fillZero(sec)

    if(num == 0){
    clearInterval(myVar) // num 이 0초가 되었을대 clearInterval로 타이머 종료
    }
    num--;
}
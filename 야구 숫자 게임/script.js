let nums = [];
let counterlimit = Math.random() * 10;

window.onload=function () {

    let i = 0;
    while (i < 3) {
        let n = Math.floor(Math.random() * 10) ;
        if (! sameNum(n)) {
            nums.push(n);
            i++;
        }
    }
    function sameNum (n) {    return nums.find((e) => (e === n));  }

    console.log(nums)
    num1 = nums[0];
    num2 = nums[1];
    num3 = nums[2];


    document.querySelector('.result-display').innerHTML = '';
}

function check_numbers() {
    let input1 = document.getElementById("number1").value;
    let input2 = document.getElementById("number2").value;
    let input3 = document.getElementById("number3").value;
    console.log(input3);

    if (input1 === '' || input2 === '' || input3 === '') {
        console.log("error");
        input1.value = '';
        input2.value = '';
        input3.value = '';
        return;
    }

    let inputs = [];
    inputs.push(input1, input2, input3)

    let s = 0;
    let b = 0;

    for (let i = 0; i <3; i++) {
        for (let j =0; j<3; j++) {
            if (nums[i] == inputs[j]) {
                if (i == j) {
                    s++;
                } else {
                    b++;
                }
            }
        }
    }

    const container = document.createElement('div');
    container.classList.add('check-result');

    const result = document.createElement('div');
    result.className= 'left';
    result.textContent = input1 + " " + input2 + " " +input3;
    container.appendChild(result);

    const rightCon = document.createElement('div');
    rightCon.className= 'right';

    if (s === 0 && b === 0) {
        rightCon.classList.add('out', 'num-result');
        rightCon.textContent = "O";
        container.appendChild(rightCon);
    } else {
        console.log(s)
        rightCon.classList.add('strike', 'num-result');
        rightCon.textContent = s +' S';
        container.appendChild(rightCon);
        console.log(container)
        const rightCon2 = document.createElement('div');
        rightCon2.classList.add('ball', 'num-result');
        rightCon2.textContent = b + ' b';
        container.appendChild(rightCon2);
        console.log(container)

    }

    //입력 초기화
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';;
    document.getElementById("number3").value = '';;

    const displayer = document.querySelector('.result-display');
    console.log(container);
    console.log(displayer);
    displayer.appendChild(container);

    if (s === 3) {
        let elementById = document.getElementById('game-result-img');

        elementById.src = 'success.png';
        document.querySelector(".submit-button").disabled = true;
    } else {
        counterlimit--;
        if (counterlimit === 0) {
            let elementById = document.getElementById('game-result-img');
            elementById.src = 'fail.png';
        }
    }


}


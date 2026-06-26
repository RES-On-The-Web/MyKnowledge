
function pickComputerMove(){
    let randomNumber = Math.floor(Math.random()*3)+1
    if (randomNumber === 1){
        computerMove = 'Rock';
    } else if (randomNumber === 2){
        computerMove = 'Paper';
    } else if (randomNumber === 3){
        computerMove = 'Scissors';
    }
    return computerMove;
}

function pickResult( Rock, Paper, Scissors, computerMove){
    let result = ''
    if (computerMove === 'Rock'){
        result = Rock;
    } else if (computerMove === 'Paper'){
        result = Paper;
    } else if (computerMove === 'Scissors'){
        result = Scissors;
    }
    return result
}

function reportDict(result){
    let reportDictVar = JSON.parse(localStorage.getItem("reportDictVar"))
    if(reportDictVar === '"null"' || reportDictVar === 'null' || reportDictVar === null) {
        reportDictVar = {
            win: 0,
            loose: 0,
            Tie: 0
        }
    }
    if (result === 'win'){
        reportDictVar["win"] += 1;
    } else if (result === 'loose'){
        reportDictVar["loose"] += 1;
    } else if (result === 'Tie'){
        reportDictVar["Tie"] += 1;
    }
    localStorage.setItem("reportDictVar", JSON.stringify(reportDictVar))
    return reportDictVar
}

function playGame(userMove){
    const computerMove = pickComputerMove();
    let result = ''
    if (userMove === 'Rock'){
        result = pickResult(Rock='Tie', Paper='loose', Scissors='win', computerMove)
    } else if (userMove === 'Paper'){
        result = pickResult(Rock='win', Paper='Tie', Scissors='loose', computerMove)
    } else if (userMove === 'Scissors'){
        result = pickResult(Rock='loose', Paper='win', Scissors='Tie', computerMove)
    }
    showResult = reportDict(result)
    document.querySelector(".resultresult").innerText = `'${result}' `

    
    document.querySelector(".result").innerHTML = `You: <img src="./${userMove}-image.png" class="sizere"> Computer: <img src="./${computerMove}-image.png" class="sizere">,     \n     win: ${showResult["win"]}, loose: ${showResult["loose"]}, Tie: ${showResult["Tie"]}`
}

function resetScore(){
    localStorage.removeItem('reportDictVar');
    document.querySelector(".resultresult").innerText = `---`
    document.querySelector('.result').innerText = `\n win: 0, loose: 0, Tie: 0`
}



























/* *************************************************************** */

(function Learn(){
    console.log(true ? "truthy" : "falsey")

const a = (true ? "truthy2" : "falsey2")
console.log(a);

false && console.log("false-log")
true && console.log("true-log-&&")

let b1 = false && "false-var"
let b2 = "false" && "false-var"
console.log(b1,b2);

false || console.log("false-log-||")
true || console.log("true-log")

// optional choose on sits
const currency = 'EUR' || 'USD'
const currency2 = undefined || 'USD'
console.log(currency, currency2);


let d = {
    name: 'hamed',
    ['hello']: 'hi',
    [`${a}`]: 1,
    'say': 'no',
    [a]: 'sdfad'
}
console.log(d['name'], d['hello'], d[`${a}`]);
console.log(d);

function bibi(){
    console.log("klsndlf");
}
let d2 = {
    name: 'shirt',
    'delivery': '1 day',
    rating: {
        star: 4.5,
        count: 87
    },
    func1: function function1(){
        console.log('function inside object');
    },
    h: bibi
}
d2['func1']()
d2.func1()

d2.h()


function function1(){
    console.log('functions');
}
const aa = {
    "aaa": function1
}
aa.aaa();


console.log(JSON.stringify(d2));
d2String = JSON.stringify(d2);
console.log(JSON.parse(d2String));


// const name = d2['name']
// console.log(name);
const { name, rating } = d2;
console.log(name, rating);

// const ob = {
//     //name : name,
//     //rating : rating
    // func: function func(){ console.log("hello");}
// }
const ob = {
    name,
    rating,
    func(){ console.log("hello")}
}
console.log(ob);







})();
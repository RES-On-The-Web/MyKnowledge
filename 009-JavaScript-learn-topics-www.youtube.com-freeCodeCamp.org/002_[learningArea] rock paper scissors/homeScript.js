function changeTheSubscribeText(){
    subscribeButton = document.querySelector(".subscribe");
    if (subscribeButton.innerText === 'subscribe'){
        subscribeButton.innerText = 'subscribed';
        subscribeButton.classList.add("subscribed")
    }else if (subscribeButton.innerText === 'subscribed'){
        subscribeButton.innerText = 'subscribe';
        subscribeButton.classList.remove("subscribed")
    }
}

function calcCost(){
    inputCost = document.querySelector(".input-cost")
    if (inputCost.value < 40){
        cost = Number(inputCost.value) + 10
    }else {
        cost = inputCost.value
    }
    showText = document.querySelector(".show-cost")
    showText.innerText = `$${cost}`;
}
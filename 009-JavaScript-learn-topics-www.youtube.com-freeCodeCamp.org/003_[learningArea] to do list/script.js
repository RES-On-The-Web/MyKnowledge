let todoList = []

function addTodo(){
    const inputNameElement = document.querySelector(".js-name-input")
    todoList.push(inputNameElement.value)
    inputNameElement.value = ''
    console.log(todoList)
    listGenerator()
}

function listGenerator(){
    let listItems = ''
    for(let i = 0; i < todoList.length; i++){
        listItems += `<p>${todoList[i]}</p>`
    }
    listBody = document.querySelector(".list-body")
    listBody.innerHTML = listItems
}
listGenerator()
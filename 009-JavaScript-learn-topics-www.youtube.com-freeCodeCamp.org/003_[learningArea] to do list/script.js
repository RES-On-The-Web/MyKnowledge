let todoList = [
    {
        name: 'a1sdfsdfasdf',
        dueDate: '123412342134'
    },
    {
        name: 'a2sdfasdfasdf',
        dueDate: '345234534'
    },
    {
        name: 'a3sdfasdf43253qdfsgsdfg',
        dueDate: '34532453245'
    }]

function addTodo(){
    const inputNameElement = document.querySelector(".js-name-input")
    const inputDueDateElement = document.querySelector(".js-due-date-input")
    todoList.push({
        name: inputNameElement.value,
        dueDate: inputDueDateElement.value
    })
    inputNameElement.value = ''
    inputDueDateElement.value = ''
    console.log(todoList)
    listGenerator()
}

function listGenerator(){
    let listItems = ''
    for(let i = 0; i < todoList.length; i++){
        listItems += `
        <div>${todoList[i].name}</div>
        <div>${todoList[i].dueDate}</div>
        <button onclick="
            todoList.splice(${i},1);
            listGenerator();
        " class="normal-button delete-button">Delete</button>`
    }
    listBody = document.querySelector(".list-body")
    listBody.innerHTML = listItems
}
listGenerator()




// //******************************************************** */


const [a,b,c] = [1,2,3]
console.log(a,b,c);

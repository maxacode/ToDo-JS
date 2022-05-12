
/* TODO:
 DONE: add support for Hover over X/Undo and show tooltip of what it does
1. add text-decoration: line-through

2. Add another X in deleted for permanent removal. 

3. Add alert Dialog like in Book Tracker. 

4. Validate that Input is not empty. 

5. CTRL  + F doesnt bring up a browser dialog but the one built into the app.

*/

function cj(variable) {
    return console.log(JSON.stringify(variable, true, 3));
};
function ct(variable) {
    return console.table(variable);
}
function cl(variable) {
    return console.log(variable);
}

//my name diff color. 
var myname = document.getElementById('my-name');
myname.style.color = 'pink';
myname.style.fontWeight = 'bold';
var form = document.getElementById('addForm');
var itemList = document.getElementById('items');
var textBox = document.getElementById('textBox');
var itemsCompleted = document.getElementById('itemsCompleted');
var searchBox = document.getElementById('filter');
var allItems = document.getElementsByClassName('list-group-item');
 

class UI {
    static getToDo() {
        const toDo = Storage.getToDo();
        

        toDo.forEach((singleTodo) =>
            UI.addItemToUI(singleTodo, "complete", ''));
    }

    static addItemToUI(singleTodo, completedORundo, checkedOrNoCheck) {
            //creating new item with li
        var newLi = document.createElement('li');
            newLi.className = 'list-group-item';
            newLi.style = "color:rgb(3, 75,231); font-size:25px";
            
        var completedButton = document.createElement('input');
            completedButton.type = 'checkbox';
            //Adding del button element to new item.
            completedButton.className = `form-check-input ${completedORundo}`;
            completedButton.checked = checkedOrNoCheck;
            completedButton.title = "Mark Completed";

        var deleteButton = document.createElement('input');
            deleteButton.type = 'Submit';
            deleteButton.value = "X";
            deleteButton.className = 'btn btn-danger delete';
            deleteButton.title = "Delete ToDo"
        
        //newLi.appendChild(document.createTextNode(itemToAdd));
        //adding text node. 
        //newLi.innerText = singleTodo;
        newLi.appendChild(completedButton);
        newLi.appendChild(deleteButton);
        newLi.appendChild(document.createTextNode(singleTodo));
        //adding new Li to Ul TODO or Completed:
        if (completedORundo == "complete") {
            itemList.appendChild(newLi);
            
            // Storage.addItemToStorageDeleted(singleTodo);
            // Storage.removeToDo(singleTodo);

        } else if (completedORundo == "undo") {
            itemsCompleted.appendChild(newLi);
            // Storage.addItemToStorage(singleTodo);
            // Storage.removeToDoDeleted(singleTodo);
          

        }
        textBox.value = "";

    }

    static getToDoDeleted() {
        const toDoDeleted = Storage.getToDoDeleted();
        

        toDoDeleted.forEach((singleTodo) =>
            UI.addItemToUI(singleTodo, 'undo', 'checked'));
    }
    
    // static addItemToUIDeletedExisting(e) {
    //     var li = e.target.parentElement;
    //     console.log("LI" + e.target);
    
    //     // console.log('singleTodo:' + singleTodo+ " \n LI: " + li)

    //     itemList.removeChild(li);
        
    //     li.style.textDecoration = 'line-through';
    //     //console.log(e.target.className); 
    //     //changing to UNDO instead of delete and undo in button Text. 
    //     e.target.className = 'btn btn-danger btn-sm float-right undo';
    //     e.target.innerText = 'Undo';
        
    
    //     //ading to Delted Items on top of list. with Line Through. 
    //     itemsCompleted.insertBefore(li, itemsCompleted.firstChild);
    //     const singleTodo = e.target.parentElement.innerText.slice(0,-5)
    //     Storage.removeToDo(singleTodo);
    //     Storage.addItemToStorageDeleted(singleTodo);

    //     //UI.addItemToUIDeleted(singleTodo)
    // }
    static addItemToUIDeleted(singleTodo) {
        //if(e.target.classList.contains('delete')){
        //if(confirm('Are you sure you want to delete')){
        var newLiForDeleted = document.createElement('li');
        newLiForDeleted.className = 'list-group-item';
        //adding text node. 
        newLiForDeleted.innerHTML = `${singleTodo} <button class= "btn btn-danger btn-sm float-right undo">Undo</button></li>`;
        newLiForDeleted.style.textDecoration = 'line-through';

        itemsCompleted.insertBefore(newLiForDeleted, itemsCompleted.firstChild);       

    }

}


//storage

class Storage {
    static getToDo() {
        let toDo;
        if(localStorage.getItem('todo') === null) {
            toDo = [];
        } else {
            toDo = JSON.parse(localStorage.getItem('todo'));
        }
        return toDo;
    }

    static addItemToStorage(todoItem) {
        const toDo = Storage.getToDo();
        toDo.push(todoItem);
        localStorage.setItem('todo', JSON.stringify(toDo));

    }

    static removeToDo(todoItem) {
        const toDo = Storage.getToDo();
        console.log("Storage.removeToDo" + toDo + " - TodoItem Var -" + todoItem);
        toDo.forEach((indivual, index) => {
            console.log("Indivual: '" + indivual + "' - toDoItem: '" + todoItem + "'");
            if (indivual == todoItem) {
                console.log("Indivual: " + indivual + " - toDoItem: " + todoItem);
                toDo.splice(index, 1);

            }
        });
        localStorage.setItem('todo', JSON.stringify(toDo));
    }

    //dellete storage
    static getToDoDeleted() {
        let toDoDeleted;
        //console.log("Storage.getToDoDeleted" + localStorage.getItem('todo'));
        if(localStorage.getItem('todoDeleted') === null) {
            toDoDeleted = [];
        } else {
            toDoDeleted = JSON.parse(localStorage.getItem('todoDeleted'));
        }
        return toDoDeleted;
    }

    static addItemToStorageDeleted(todoItemDeleted) {
        const toDoDeleted = Storage.getToDoDeleted();
        toDoDeleted.push(todoItemDeleted);
        localStorage.setItem('todoDeleted', JSON.stringify(toDoDeleted));

    }

    static removeToDoDeleted(todoItemDeleted) {
        const toDoDeleted = Storage.getToDoDeleted();
        console.log("Storage.removeToDo" + toDoDeleted+ " - TodoItem Var -" + todoItemDeleted);
        toDoDeleted.forEach((indivual, index) => {
            console.log("Indivual: '" + indivual + "' - toDoItem: '" + todoItemDeleted + "'");
            if (indivual == todoItemDeleted) {
                console.log("Indivual: " + indivual + " - toDoItem: " + todoItemDeleted);
                toDoDeleted.splice(index, 1);

            }
        });
        localStorage.setItem('todoDeleted', JSON.stringify(toDoDeleted));
    }

    
}
function returnToDoFromDeleted(e) {
    if (e.target.classList.contains('undo')){
        const todoItem = e.target.parentElement.innerText.slice(0,-5);

        //console.log("todoItem: " + todoItem);
        Storage.addItemToStorage(todoItem);
        Storage.removeToDoDeleted(todoItem);
        var li = e.target.parentElement;
        li.style.textDecoration = 'none';
        //console.log(e.target.className);
        // chanign back to delete class and X letter in button 
        e.target.className = 'btn btn-danger btn-sm float-right delete';
        e.target.innerText = 'X';

        itemsCompleted.removeChild(li);
        itemList.appendChild(li);
        
    }
}


// if completed button is clicked in Item List
itemList.addEventListener('click', (e) => {
    if(e.target.classList.contains('complete')){
        //getting the parrent of the clicked element and the inner text of it.
        singleTodo = e.target.parentElement.innerText;

        itemList.removeChild(e.target.parentElement);
        

        UI.addItemToUI(singleTodo, "undo", "checked");

        //Storage.addItemToStorage(singleTodo);
            // Storage.removeToDoDeleted(singleTodo);
        Storage.addItemToStorageDeleted(singleTodo);
        Storage.removeToDo(singleTodo);


    }

});

function deleteToDoFully(e) {
    // cl(e.target.parentElement);
    // cl(uncheckedOrChecked);
  
    if(e.target.classList.contains('delete')){
        const eParent  = String(e.target.previousElementSibling.classList);
        singleTodo = e.target.parentElement.innerText;

        cl(eParent)
        if (eParent.includes('complete')) {
            cl("complete");
            itemList.removeChild(e.target.parentElement);
            Storage.removeToDo(singleTodo);

        } else if (eParent.includes('undo')) {
            itemsCompleted.removeChild(e.target.parentElement);
            Storage.removeToDoDeleted(singleTodo);

        } else { cl("Nothing")};
    //     //getting the parrent of the clicked element and the inner text of it.
    //     singleTodo = e.target.parentElement.innerText;
    //     cl(`Deleting permenatly this todo: ${singleTodo}`);

    //     if (uncheckedOrChecked == "itemList"){
    //         itemList.removeChild(e.target.parentElement);
    //         Storage.removeToDo(singleTodo);
    //     } else if (uncheckedOrChecked == "itemsCompleted") {
    //         itemsCompleted.removeChild(e.target.parentElement);
    //         Storage.removeToDoDeleted(singleTodo);
    //     } else {raiseError("FAIL!")}
    }
}

document.querySelectorAll<"ul">addEventListener('click', (e) => {
    deleteToDoFully(e);
});
// // if delete button is clicked in BOTH? 
// itemList.addEventListener('click', (e) => {
//     deleteToDoFully(e, "itemList")}, false );


// if completed button is clicked completed list
itemsCompleted.addEventListener('click', (e) => {
    if(e.target.classList.contains('undo')){
        //getting the parrent of the clicked element and the inner text of it.
        singleTodo = e.target.parentElement.innerText;

        itemsCompleted.removeChild(e.target.parentElement);
        
        UI.addItemToUI(singleTodo, "complete", "");

        Storage.addItemToStorage(singleTodo);
        Storage.removeToDoDeleted(singleTodo);
            
        // Storage.addItemToStorageDeleted(singleTodo);
        // Storage.removeToDo(singleTodo);


    }

});





function filter() {
    userInput = searchBox.value;
    //console.log(allItems.length); 
    for (x = 0; x < allItems.length; x++) {
        if (allItems[x].innerText.toLowerCase().indexOf(userInput.toLowerCase()) == '-1') {
            //allItems[x].style.display = 'block'
            allItems[x].style.display = 'none';
        } else { 
            allItems[x].style.display = 'block';
        }
        
    }
}






textBox.addEventListener('click', (e) => {
    if(textBox.value == 'Enter Here') {
        textBox.value = "";
    }
});
textBox.addEventListener('mouseout', () => { 
    if (textBox.value == "") {
        textBox.value = "Enter Here";
}
});

// filter key down event. 
searchBox.addEventListener('input', filter);

//item from the completed section 
//itemsCompleted.addEventListener('click', 23);

//load saved and unsaved items. 
document.addEventListener('DOMContentLoaded', UI.getToDo);
document.addEventListener('DOMContentLoaded', UI.getToDoDeleted);

// when submit is pressed
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const itemToAdd = textBox.value;
    //console.log(itemToAdd);
    //sending it to UI to create the new item elemnet
    UI.addItemToUI(itemToAdd, 'complete', '');
    //storing as a string just the text
    Storage.addItemToStorage(itemToAdd);
});

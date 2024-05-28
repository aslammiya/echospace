let menuButton = document.querySelector("#menu-button")
menuButton.addEventListener('click', function(){
    document.querySelector('#menu-items').classList.toggle("hidden")
});

document.querySelector(".container").addEventListener('click', function(){
    if (document.querySelector('#menu-items').classList.contains("hidden") == true){
        
    }else{
        document.querySelector('#menu-items').classList.toggle("hidden")
    }
})

let drawarToggle = document.querySelector("#drawarToggle")
drawarToggle.addEventListener('click', function(){
    document.querySelector('#friendsDrawar').classList.toggle("hidden")
    drawarToggle.classList.toggle("hidden")
});

let closeDrawar = document.querySelector(".closeDrawar")
closeDrawar.addEventListener('click', function(){
    document.querySelector('#friendsDrawar').classList.add("hidden")
    drawarToggle.classList.toggle("hidden")
});

let chatToggle = document.querySelector('#chatToggle')
chatToggle.addEventListener('click', function(){
    document.querySelector('#chatWindow').classList.toggle("hidden");
    chatToggle.classList.toggle('hidden');
})

let closeChat = document.querySelector(".closeChat")
closeChat.addEventListener('click', function(){
    document.querySelector('#chatWindow').classList.toggle("hidden");
    chatToggle.classList.toggle('hidden');
});
let userIcons = document.getElementsByName('userIcon');
let userMenuBtns = document.querySelectorAll('#userMenuBtn');
let userMenus = document.getElementsByName('userMenu');

// Convert NodeLists to arrays to use forEach
userIcons = Array.from(userIcons);
userMenuBtns = Array.from(userMenuBtns);
userMenus = Array.from(userMenus);

userIcons.forEach((icon, index) => {
    const menuBtn = userMenuBtns[index];
    const menu = userMenus[index];

    icon.addEventListener('mouseover', () => {
        menuBtn.classList.remove('hidden');
    });

    icon.addEventListener('mouseout', () => {
        menuBtn.classList.add('hidden');
    });
    
    menuBtn.addEventListener('click', function() {
        // Hide all other menus
        userMenus.forEach((m, i) => {
            if (i !== index) {
                m.classList.add('hidden');
            }
        });
        // Toggle the current menu
        menu.classList.toggle('hidden');
    });
    
    menu.addEventListener('mouseleave', () => {
        menu.classList.add('hidden');
    });
});

document.querySelector("#showAnswer").addEventListener('click', ()=>{
    document.querySelector("#answerDialog").classList.toggle('hidden');
});

let editbutton = document.querySelector('#edit-button');
editbutton.addEventListener('click', () => {
    let inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.classList.toggle('pointer-events-none');
        input.toggleAttribute('readonly');
        input.focus();
    });
});
editbutton.addEventListener('click', ()=>{
    if(document.querySelector("#editSave").innerHTML == "Save"){
        document.querySelector("#editSave").innerHTML = "Edit";   
    }else{
        document.querySelector("#editSave").innerHTML = "Save";
    }  
})

document.querySelector("#closeProfile").addEventListener('click', ()=>{
    profileInfo.classList.toggle("hidden");
})

document.querySelector("#showProfile").addEventListener('click', ()=>{
    profileInfo.classList.toggle("hidden");
    document.querySelector("#showProfile").classList.toggle('profileOpen');
})

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

document.addEventListener('DOMContentLoaded', function() {
    let users = Array(30).fill({ name: 'Aslam Miya', username: 'aslammiya', imageUrl: 'images/dp.png' });

    let userList = document.getElementById('user-list');

    users.forEach(user => {
        let userCard = `
            <div class="my-4">
                <div class="w-full px-3 py-2 shadow-md rounded-2xl userCard flex justify-between items-center">
                    <div class="block relative" id="menu-button">
                        <img class="w-11 h-12 rounded-full object-top" src="{% static 'images/dp.png' %}" alt="User Image" />
                    </div>
                    <div class="flex flex-col ml-3">
                        <span class="block font-medium">${user.name}</span>
                        <span class="block text-gray-500">@${user.username}</span>
                    </div>
                    <div class="w-2 h-2 bg-red-600 rounded-full"></div>
                    <button type="button" class="hover:bg-zinc-900 hover:border-zinc-900 border-solid border-2 px-2 rounded-full hover:text-white">
                        <i class="fa-solid fa-user-plus"></i>
                    </button>
                </div>
            </div>
        `;
        userList.innerHTML += userCard;
    });
});

document.addEventListener('DOMContentLoaded', ()=>{
    let loby = document.getElementById('loby')
    for (let index = 0; index <= 100; index++) {
        let userIcon = `
        <div name="userIcon" class="flex flex-wrap h-fit relative justify-center">
               <img class="border-4 border-blue-500 rounded-full w-20 h-20 p-0.5 object-cover sm:w-20 sm:h-20 md:w-24 md:h-24" src="https://plus.unsplash.com/premium_photo-1708110770188-3e4216b93119?q=80&w=1386&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Profile Image">
               <div class="absolute rounded-2xl px-2 h-fit w-fit bg-black flex justify-center items-center opacity-25 self-end mb-2 hidden" id="userMenuBtn">
                  <i class="fas fa-ellipsis-h text-2xl text-white"></i>
               </div>
               <div name="userMenu" class="absolute left-12 bottom-6 mt-2 w-fit opacity-90 bg-white rounded-xl shadow-lg z-10 hidden">
                  <ul class="py-1">
                     <li class="px-2 py-1 hover:bg-gray-200 cursor-pointer bg-white rounded-lg">Mute</li>
                     <li class="px-2 py-1 hover:bg-gray-200 cursor-pointer bg-white rounded-lg">Kickout</li>
                  </ul>
            </div>
        `
        loby.innerHTML += userIcon;
    }
});

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



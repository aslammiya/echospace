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
    const users = Array(30).fill({ name: 'Aslam Miya', username: 'aslammiya', imageUrl: 'images/dp.png' });

    const userList = document.getElementById('user-list');

    users.forEach(user => {
        const userCard = `
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

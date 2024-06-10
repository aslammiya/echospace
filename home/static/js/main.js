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

document.querySelector("#closeProfile").addEventListener('click', ()=>{
    profileInfo.classList.toggle("hidden");
})

document.querySelector("#showProfile").addEventListener('click', ()=>{
    profileInfo.classList.toggle("hidden");
    document.querySelector("#showProfile").classList.toggle('profileOpen');
})

setTimeout(function() {
    document.getElementById("changeGuestPaswd").style.display = "none";
  }, 5000);

  function enableNameFields(){
    let name_label = document.getElementById("name_label");
    let first_name = document.getElementById("first_name");
    let last_name = document.getElementById("last_name");
    name_label.classList.add('hidden');
    document.getElementById('edit_name').style.display = 'none';
    document.querySelector("#name_feild").classList.remove("hidden");
    first_name.removeAttribute('readonly');
    last_name.removeAttribute('readonly');
    document.querySelector("#save-button").classList.remove('hidden');
}

function enableFieldUsername(){
    let username_label = document.querySelector("#username_label")
    username_label.classList.add('hidden');
    document.getElementById('edit_username').style.display = 'none';
    document.querySelector("#username").classList.remove("hidden");
    document.querySelector("#username").removeAttribute('readonly');
    document.querySelector("#save-button").classList.remove('hidden');
}
function changeProfileImage() {
    document.getElementById('changeProfileImageFile').click();
    }
    
    function showUploadedMessage(input) {
        if (input.files && input.files[0]) {
        document.querySelector("#save-button").classList.remove('hidden');
        dpEditIcon = document.getElementById('dpEditIcon');
        dpEditIcon.classList.remove('fa-edit')
        dpEditIcon.classList.add("fa-check")
    }
}

document.getElementById('username').addEventListener('input', function() {
    var username = this.value.trim();
    if (username !== '') {
      if (username.indexOf(' ') !== -1) {
        document.getElementById('username').classList.add("red-border");
        document.getElementById('username').classList.remove("green-border");
      } else {
        checkUsernameAvailability(username);
      }
    } else {
      document.getElementById('username').classList.remove("green-border", "red-border");
    }
  });

function checkUsernameAvailability(username) {
    fetch('/check_username/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({'username': username})
    })
    .then(response => response.json())
    .then(data => {
        if (data.available) {
            document.getElementById('username').classList.remove("red-border");
            document.getElementById('username').classList.add("green-border");
        } else {
            document.getElementById('username').classList.remove("green-border");
            document.getElementById('username').classList.add("red-border");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    if (document.getElementById('username').classList.contains('red-border')) {
        alert('Please choose a different username as the current one is already taken.');
    } else {
        this.submit();
    }
});

document.getElementById('new_password').addEventListener('input', function() {
    var new_password = this.value.trim();
    if (new_password.length < 8) {
      this.classList.add("red-border");
    } else {
      this.classList.remove("red-border");
      this.classList.add("green-border");
    }
});

document.querySelector("#closeChangePassword").addEventListener('click', ()=>{
    document.getElementById("changePasswordDiv").classList.toggle("hidden");
})

document.querySelector("#change-password-button").addEventListener('click', ()=>{
    document.querySelector("#profileInfo").classList.add('hidden');
    document.getElementById("changePasswordDiv").classList.toggle("hidden");
})

document.querySelector("#changePassPopup").addEventListener("click", ()=>{
    document.getElementById("changePasswordDiv").classList.toggle("hidden");
})
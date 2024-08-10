var roomName = document.getElementById('roomName').textContent.trim().slice(1);
var ws = new WebSocket('ws://' + window.location.host + '/ws/ac/room/' + roomName + '/');
ws.onopen = function(){
    console.log("Ws open..")
}
ws.onmessage = function(event){
    console.log("Msg reci ",event.data);
    const data = JSON.parse(event.data);           
    chatData = `
    <div class="flex items-start mb-4">
        <img class="w-10 h-10 rounded-full object-cover mr-4" src="${data.userProfileImage}" alt="Profile Image" />
        <div>
            <p class="text-sm font-semibold">${data.username}&nbsp;&nbsp;<span class="font-thin text-xs">${data.timeString}</span></p>
            <p class="text-sm">${data.msg}</p>
        </div>
    </div>
    `
    document.querySelector("#chatAppendArea").insertAdjacentHTML('beforeend', chatData)
}
ws.onclose = function(){
    console.log("Ws close..")
}
document.getElementById("sendTextMsg").onclick = function(event) {
    event.preventDefault();
    let inputElement = document.getElementById('msgTextInput');
    const dataContainer = document.getElementById('data-container');
    const userName = dataContainer.getAttribute('data-user-name');
    const userProfileImage = dataContainer.getAttribute('data-user-profile-image');
    const now = new Date();

    let hours = now.getHours();
    const minutes = now.getMinutes();
    const isPM = hours >= 12;

    // Convert to 12-hour format
    hours = hours % 12;
    hours = hours ? hours : 12; // if hours is 0, set to 12
    const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const ampm = isPM ? 'PM' : 'AM';

    // Format time string
    const timeString = `${hours.toString().padStart(2, '0')}:${formattedMinutes} ${ampm}`;

    console.log(timeString)
    let input = inputElement.value;
    ws.send(JSON.stringify({
        'msg': input,
        'timeString': timeString,
        'username': userName,
        'userProfileImage': userProfileImage
    }));
    inputElement.value = '';
};


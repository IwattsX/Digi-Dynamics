

//Base function for a call check
function myFunction() {
    alert("Hello change!");
}

//navbar

//navbar variable
let home = document.getElementById("home");
let games = document.getElementById("games");
let dlc = document.getElementById("dlc");
let demo = document.getElementById("demo");
let music = document.getElementById("music");
let user = document.getElementById("user");

//On Home Click
function homeBtn(){
    home.classList.add("font-effect-fire");
}
 
//On Title Click
function titleChange(){
    alert("hi");
    document.getElementById("title").classList.add("font-effect-fire");
}

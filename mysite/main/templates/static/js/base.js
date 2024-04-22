//Base function for a call check
function myFunction() {
    alert("Hello change!");
}

//navbar variable
let home = document.getElementById("home");
let games = document.getElementById("games");
let dlc = document.getElementById("dlc");
let demo = document.getElementById("demo");
let music = document.getElementById("music");
let user = document.getElementById("user");

//Active Nav Bar
function homeActive(){
    home.classList.add("font-effect-neon");
    home.classList.remove("font-effect-fire");
    
}
function gamesActive(){
    games.classList.add("font-effect-neon");
    games.classList.remove("font-effect-fire");
    
}
function dlcActive(){
    dlc.classList.add("font-effect-neon");
    dlc.classList.remove("font-effect-fire");
    
}
function demoActive(){
    demo.classList.add("font-effect-neon");
    demo.classList.remove("font-effect-fire");
    
}
function musicActive(){
    music.classList.add("font-effect-neon");
    music.classList.remove("font-effect-fire");
    
}
function userActive(){
    user.classList.add("font-effect-neon");
    user.classList.remove("font-effect-fire");
    
}

var LikedForm = document.getElementById("likeGames");


/* Games Like Function */
function likeFunction(event, games_id, url_games) {
    event.preventDefault();
    document.getElementById(games_id).style.color = "rgb(0, 238, 255)";
    $.ajax({
        type:'POST',
        url: url_games,
        data:
        {
        liked: games_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        //alert('AJAX REQUEST');
        console.log("Ajax post request coming in");
    }
    })
}

/* DLC Like Function */
function likeFunction(event, games_id, url_games) {
    event.preventDefault();
    document.getElementById(games_id).style.color = "rgb(0, 238, 255)";
    $.ajax({
        type:'POST',
        url: url_games,
        data:
        {
        liked: games_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        //alert('AJAX REQUEST');
        console.log("Ajax post request coming in");
    }
    })
}

/* Music Like Function */
function likeFunction(event, music_id, url_music) {
    event.preventDefault();
    document.getElementById(music_id).style.color = "rgb(0, 238, 255)";
    $.ajax({
        type:'POST',
        url: url_music,
        data:
        {
        liked: music_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        //alert('AJAX REQUEST');
        console.log("Ajax post request coming in");
    }
    })
}

/* Demo Like Function */
function likeFunction(event, games_id, url_games) {
    event.preventDefault();
    document.getElementById(games_id).style.color = "rgb(0, 238, 255)";
    $.ajax({
        type:'POST',
        url: url_games,
        data:
        {
        liked: games_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
    success:function(){
        //alert('AJAX REQUEST');
        console.log("Ajax post request coming in");
    }
    })
}



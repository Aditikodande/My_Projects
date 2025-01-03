/*var audio=document.createElement('audio');
audio.setAttribute('src','sound.mp3');
audio.loop=true;
audio.play();*/

var audio = document.createElement('audio');
audio.setAttribute('src', 'sound.mp3');
audio.loop = true;

document.body.addEventListener('click', function() {
    audio.play().catch(function(error) {
        console.error('Error playing audio:', error);
    });
});

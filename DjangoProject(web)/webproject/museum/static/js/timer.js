let currentTime = new Date().getTime();
let savedTime = localStorage.getItem('countdownStartTime');

if (savedTime && currentTime < savedTime){
    startCountdown(savedTime);
} 
else{
    var startTime = currentTime + 60 * 60 * 1000; 
    startCountdown(startTime);
}


function startCountdown(startTime) {
    var countdownElement = document.getElementById('countdown');
    countdownElement.style.margin = '10px';
    countdownElement.style.fontWeight = '700';
    countdownElement.style.fontSize = '18px';
    countdownElement.style.breakBefore = 'Timer: ';
    
    var countdownInterval = setInterval(function() {
        let now = new Date().getTime();
        let distance = startTime - now;

        let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownElement.innerHTML = "Time left:" + hours + "h " + minutes + "min " + seconds + "sec ";
        if (distance < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = "Countdown completed";
            localStorage.removeItem('countdownStartTime');
        }
      }, 1000);

    localStorage.setItem('countdownStartTime', startTime);
}
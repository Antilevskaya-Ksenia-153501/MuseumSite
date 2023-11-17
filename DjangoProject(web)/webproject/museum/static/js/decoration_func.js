function changeTextColor(newColor){
    var paragraphs = document.querySelectorAll('.policy-text p');
    for (var i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.color = newColor; 
  }
}

function changeTextSize(newSize){
    var paragraphs = document.querySelectorAll('.policy-text p');
    for (var i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.fontSize = newSize; 
    }
}